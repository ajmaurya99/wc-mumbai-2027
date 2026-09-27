# Prompt: card

A three-card row for WordCamp Mumbai 2027: a core Columns block, alignment
wide, blockGap preset 30 for rows and columns, stacked on mobile. Each Column
holds a Group with the CSS class wcm-card, border radius 16px, padding preset
40 on all sides, background preset accent-5 (base when the section is
sky-wash), flow layout. Inside, in this order: an Image with aspect ratio
16:10, scale cover and radius 16px; an H3 Heading at size preset large; a one
or two line Paragraph; a Paragraph containing a single descriptive text link.
No border. `card.css` adds the hover-only shadow `0 12px 32px rgba(13,27,42,.12)`,
a 4px lift, `height: 100%` for even rows, and the focus ring, all guarded by
prefers-reduced-motion.
