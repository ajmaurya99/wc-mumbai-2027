# Prompt: tier card

A sponsorship tier row for WordCamp Mumbai 2027: a core Columns block, wide
alignment, blockGap preset 30, three Columns. Each holds a Group with the
classes wcm-card and wcm-tier, background preset accent-5 (base on sky-wash
sections), radius 16px, padding preset 40, blockGap preset 20, containing:
an Image (the tier icon, 96px wide, radius 16px); a Group with gap 0 holding
an uppercase small eyebrow Paragraph in accent-2 ("Platinum") and an H3 at
size large (the tier name); a Group with gap 0 holding the price as a
Paragraph at xx-large, weight 700, accent-1, and a small accent-4 line with
the dollar figure; one Paragraph saying who the tier is for; a List block
with the class wcm-check (tier-card.css turns bullets into teal ticks); then
either a bold link "All <tier> benefits →" (short version) or a small
accent-4 "Best for:" line (full version); and a Buttons block with one
outline button at 100% width. The headline tier gets a 2px border in
accent-1 via the Group's border setting and the extra class wcm-tier--featured.
Hover comes from card.css.
