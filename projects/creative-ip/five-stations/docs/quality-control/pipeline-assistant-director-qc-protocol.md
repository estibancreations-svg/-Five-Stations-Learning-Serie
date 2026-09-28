# Pipeline Assistant Director: final Quality Control protocol

The Pipeline Assistant Director is the final evidence coordinator for an episode or batch. It does not silently approve work. It asks the questions below, attaches evidence, records the answer, assigns an owner to every failure, and sends the complete Q&A log with the delivered package.

## Q&A record

Every delivery gets one immutable record with:

`delivery_id · project · series · season · episode · revision · question · answer · evidence · status · owner · next_action · timestamp`

Allowed statuses: `verified`, `verified_with_hold`, `needs_revision`, `blocked`, `not_applicable`.

## Final check sequence

### 1. Inventory and scope

1. What exactly was requested?
2. What files, records, prompts, scripts, media assets and reports were actually created?
3. Does the direct source count match the manifest count?
4. Which seasons, episodes or asset classes are absent?
5. Are any totals projections rather than completed work?

Evidence: creation inventory, source record count, manifest, file hashes and repository commit.

### 2. Story and curriculum

1. Does the episode have a clear question, problem, investigation, evidence and resolution?
2. Is the target age and grade band explicit?
3. Is the learning claim accurate and age appropriate?
4. Does the on-screen text match the approved literacy or science content?
5. Does the fantasy action remain clearly separate from the factual explanation?

Evidence: approved objective, curriculum review, screenplay revision, checked overlays and reviewer initials.

### 3. Character and world continuity

1. Are the approved character references used for every shot?
2. Are names, colors, proportions, voices, props and locations consistent?
3. Does the episode belong to the correct station, season and learning language?
4. Are any visual elements borrowed, imitative or unlicensed?

Evidence: reference asset IDs or hashes, continuity sheet, shot list, rights notes and regeneration log.

### 4. Generation and edit

1. What model, settings, references and prompt revision produced each shot?
2. Which outputs were accepted, rejected or partially usable?
3. Is the motion physically and narratively coherent?
4. Were scenes stitched in the approved order with usable duration recorded?
5. Were generation cost, retries and external service usage recorded?

Evidence: generation ledger, asset IDs, task results, edit decision list, cost record and final render hash.

### 5. Accessibility, rights and platform readiness

1. Are captions accurate and synchronized?
2. Is dialogue intelligible and audio licensed or owned?
3. Are title, description, thumbnail and audience settings truthful?
4. Does the content avoid child directed commercial pressure and unsupported educational claims?
5. Are the linked adult experiences reviewed separately from the children's narrative?

Evidence: caption file, audio rights record, platform checklist, policy review and owner approval.

### 6. Delivery decision

1. Can another person reproduce the package from the repository and manifest?
2. Does every claim in the delivery report point to evidence?
3. What remains open, who owns it and what is the next action?
4. Is the package `verified`, `verified_with_hold`, `needs_revision` or `blocked`?

The Assistant Director may mark a package `verified_with_hold` only when the hold is explicit, non-misleading and assigned. It may not convert a prompt inventory into a finished media claim.

## VisionWeaver end-user view

The end user sees a project workspace in this order:

1. **Project overview:** title, purpose, current state, verified counts and open holds.
2. **World map:** the five stations, their characters, locations, visual rules and learning scope.
3. **Season map:** episodes grouped by series and season, with status badges.
4. **Episode room:** logline, objective, script, storyboard, prompt set, generated assets, rejected attempts and continuity evidence.
5. **Assistant Director panel:** the Q&A checklist, evidence links, unresolved claims and approval action.
6. **Delivery package:** final media, captions, metadata, asset manifest, QC report, Q&A log and commit or package identifier.

The user should always be able to distinguish `concept`, `script`, `approved animatic`, `generated shot`, `edited episode`, `QC verified` and `published`. The interface should show the evidence behind each status instead of presenting a single progress percentage.

## Handoff contract

The delivered package must contain:

- the creation inventory JSON and Markdown report;
- the episode and asset manifest;
- the Q&A log with every question and answer;
- the final render and caption references, when they exist;
- the open-holds list and owners;
- the repository commit or immutable package identifier;
- the owner approval record.

This is the final Quality Control section for the current development package. Its current result is `PASS_WITH_HOLDS`: the 150 source records and 600 prompt count are internally consistent, while finished media, curriculum approval, character locks, rights review and owner approval remain future gates.
