#!/bin/sh
# Render an HTML file with headless Chrome at the two review widths.
#
#   render.sh <file.html> [out-dir] [widths]
#
# Defaults: out-dir = the HTML file's folder, widths = "390 1366".
# Writes <name>-<width>.png. Each render is full page: a first pass measures
# document height with --dump-dom, a second pass takes the screenshot.
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
SRC_ABS="$(cd "$(dirname "$SRC")" && pwd)/$(basename "$SRC")"
NAME="$(basename "$SRC" .html)"
mkdir -p "$OUT_DIR"

# Measuring copy: same folder so relative CSS links keep working.
MEASURE="$(dirname "$SRC_ABS")/.measure-$$.html"
sed 's#</body>#<script>document.title=String(Math.ceil(document.documentElement.scrollHeight));</script></body>#' "$SRC_ABS" > "$MEASURE"
trap 'rm -f "$MEASURE"' EXIT

for W in $WIDTHS; do
  H=$("$CHROME" --headless=new --disable-gpu --hide-scrollbars \
        --window-size="${W},400" --dump-dom "file://$MEASURE" 2>/dev/null \
        | sed -n 's:.*<title>\([0-9]*\)</title>.*:\1:p' | head -1)
  [ -n "$H" ] || H=900
  [ "$H" -lt 400 ] && H=400
  [ "$H" -gt 8000 ] && H=8000
  OUT="$OUT_DIR/${NAME}-${W}.png"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
        --window-size="${W},${H}" --screenshot="$OUT" "file://$SRC_ABS" >/dev/null 2>&1
  echo "$OUT (${W}x${H})"
done
