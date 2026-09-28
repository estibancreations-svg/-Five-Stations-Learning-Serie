# Character board first-run QC log

**Run:** Character board v1 generation  
**Status:** `owner_approved_for_calibration`  
**Approval:** The Architect approved the five board compositions on 2026-09-28.  
**Remaining gate:** Turnaround testing and scene continuity checks are still required before pilot automation is enabled.

| Question | Answer | Evidence | Status |
|---|---|---|---|
| Were five station boards generated? | Yes. | Five PNG assets in `assets/character-boards/`. | verified |
| Is panel order defined? | Yes. | Board README and character board lock. | verified |
| Are exact names rendered into the image? | No. Blank nameplates are intentional. | Letter Lock protocol. | verified |
| Did the owner approve the board compositions? | Yes. The Architect approved them on 2026-09-28. | This approval record and the board assets. | verified |
| Can these boards be used as final character locks now? | They are approved calibration references. Turnarounds and test scenes still determine final pilot lock. | First-run lock requires turnarounds and test scenes. | verified_with_hold |
| Can another creative system receive them? | Yes, with the board assets, lock documents and panel order. | Handoff contract in character board lock. | verified |
| Are text, phonemes and formulas allowed to come from generated pixels? | No. | Exact Text protocol requires controlled compositing and proofread. | verified |
| Can pilot mode run automatically now? | Only for repeatable draft stages after board approval. | Pilot mode gates. | verified_with_hold |
| Is ElevenLabs allowed to choose or change the script? | No. It receives approved narration, pronunciation and voice settings. | Voiceover handoff rules. | verified |

## Required next first-run actions

1. Human-review each board and mark character-level corrections.
2. Produce front, side, back and expression turnarounds for each approved character.
3. Run one single-character scene and one group scene per station.
4. Compare every result to the board and record drift or distortion.
5. Freeze the approved board asset hashes after turnaround and test-scene checks, then enable pilot automation.
