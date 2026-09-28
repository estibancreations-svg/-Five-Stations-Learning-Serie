# Letter lock and exact text protocol

## Rule

Any visible word, letter, phoneme, number, equation, diagram label, caption, title, nameplate, sign or UI text is authored in a controlled text layer. Generated imagery may supply the scene and blank surfaces. It may not be treated as proof that printed content is correct.

## Required record

Each text element receives:

`text_id · exact_string · Unicode/code points when needed · case · punctuation · font asset · language · placement · reading order · source revision · proofreader · render hash`

The exact string must be copied verbatim into compositing or typesetting. Do not retype it from an image. For phonics, store the grapheme, phoneme notation, example word and pronunciation separately. For science and mathematics, store symbols and units in a source format that can be checked before rasterization.

## Verification

The Assistant Director checks:

1. OCR or visual comparison against the source string.
2. Human proofread for spelling, punctuation, symbols, capitalization and reading order.
3. Caption transcript against the same approved script.
4. Safe-area and legibility review on phone and television views.
5. Regeneration or compositing if any character is uncertain.

An image with ambiguous lettering is `needs_revision`, even when the scene is otherwise usable. The final delivery includes the exact-text manifest and its proof record.

## Outsourced systems

When a creative system receives a prompt, it receives a `TEXT_LOCK` block and a `CHARACTER_LOCK` block. The system may place a blank surface or return a scene with text omitted for post-production. It may not paraphrase, translate, invent, stylize or alter locked text without a new revision and approval.
