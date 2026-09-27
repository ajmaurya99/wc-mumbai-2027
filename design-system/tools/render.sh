#!/bin/sh
# Render an HTML file with headless Chrome at the two review widths.
#
#   render.sh <file.html> [out-dir] [widths]
#
# Defaults: out-dir = the HTML file's folder, widths = "390 1366".
# Writes <name>-<width>.png, full page.
#
# How: headless Chrome clamps its window to 500px wide, so a phone width
# cannot be rendered directly. The page is loaded in an <iframe> of the wanted
# width inside a wider wrapper; a first pass reads the iframe's document height
# (--allow-file-access-from-files lets the wrapper read it), a second pass
# screenshots the wrapper with the window height set to that height, and sips
# crops the PNG to the iframe. The iframe is centred and sips crops from the
# centre (its --cropOffset flag is ignored on this macOS), so the crop is exact.
# vw units and media queries inside the iframe follow the iframe width, so the
# result is a faithful viewport render.
#
# Needs Google Chrome in /Applications (or set CHROME=/path/to/chrome).
# Do not add --user-data-dir: with a fresh profile Chrome 153 on macOS starts
# its updater and never exits (verified 27 Sep 2026); without it, it exits in ~1s.
set -eu
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME" >&2; exit 1; }

SRC="$1"
OUT_DIR="${2:-$(dirname "$SRC")}"
WIDTHS="${3:-390 1366}"
[ -f "$SRC" ] || { echo "no such file: $SRC" >&2; exit 1; }
SRC_DIR="$(cd "$(dirname "$SRC")" && pwd)"
SRC_FILE="$(basename "$SRC")"
NAME="$(basename "$SRC" .html)"
mkdir -p "$OUT_DIR"

WRAP="$SRC_DIR/.render-$$.html"
trap 'rm -f "$WRAP"' EXIT

for W in $WIDTHS; do
  WIN_W=$(( W + 40 )); [ "$WIN_W" -lt 520 ] && WIN_W=520
  cat > "$WRAP" <<HTML
<!doctype html><html><head><meta charset="utf-8"><title>0</title>
<style>html,body{margin:0;padding:0;background:#FFFFFF}iframe{display:block;border:0;margin:0 auto;width:${W}px;height:600px}</style>
</head><body><iframe id="f" src="${SRC_FILE}"></iframe><script>
document.getElementById('f').addEventListener('load',function(){
  var d=this.contentDocument.documentElement;
  document.title=String(Math.ceil(Math.max(d.scrollHeight,this.contentDocument.body.scrollHeight)));
});
</script></body></html>
HTML
  H=$("$CHROME" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files \
        --window-size="${WIN_W},700" --dump-dom "file://$WRAP" 2>/dev/null \
        | sed -n 's:.*<title>\([0-9]*\)</title>.*:\1:p' | head -1)
  [ -n "$H" ] && [ "$H" -gt 0 ] || H=900
  [ "$H" -lt 200 ] && H=200
  [ "$H" -gt 24000 ] && H=24000
  sed -i '' "s/height:600px/height:${H}px/" "$WRAP"
  OUT="$OUT_DIR/${NAME}-${W}.png"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files \
        --window-size="${WIN_W},${H}" --screenshot="$OUT" "file://$WRAP" >/dev/null 2>&1
  sips -c "$H" "$W" "$OUT" --out "$OUT" >/dev/null 2>&1 || true
  echo "$OUT (${W}x${H})"
done
