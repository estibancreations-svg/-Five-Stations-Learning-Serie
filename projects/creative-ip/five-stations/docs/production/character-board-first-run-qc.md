# Character board first-run QC log

**Run:** Character board v1 generation  
**Status:** `verified_with_hold`  
**Hold:** Human visual approval and turnaround testing are still required.

| Question | Answer | Evidence | Status |
|---|---|---|---|
| Were five station boards generated? | Yes. | Five PNG assets in `assets/character-boards/`. | verified |
| Is panel order defined? | Yes. | Board README and character board lock. | verified |
| Are exact names rendered into the image? | No. Blank nameplates are intentional. | Letter Lock protocol. | verified |
| Can these boards be used as final character locks now? | Not yet. | First-run lock requires human review, turnarounds and test scenes. | verified_with_hold |
| Can another creative system receive them? | Yes, as reference candidates with the lock documents and panel order. | Handoff contract in character board lock. | verified_with_hold |
| Are text, phonemes and formulas allowed to come from generated pixels? | No. | Exact Text protocol requires controlled compositing and proofread. | verified |
| Can pilot mode run automatically now? | Only for repeatable draft stages after board approval. | Pilot mode gates. | verified_with_hold |
| Is ElevenLabs allowed to choose or change the script? | No. It receives approved narration, pronunciation and voice settings. | Voiceover handoff rules. | verified |

## Required next first-run actions

1. Human-review each board and mark character-level corrections.
2. Produce front, side, back and expression turnarounds for each approved character.
3. Run one single-character scene and one group scene per station.
4. Compare every result to the board and record drift or distortion.
5. Approve a board revision and freeze its asset hashes before pilot automation.
