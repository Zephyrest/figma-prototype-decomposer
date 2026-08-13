---
name: figma-prototype-decomposer
description: Fully decompose the entire product covered by supplied evidence into user tasks, modules, screens, E/L1/L2/L3/S hierarchy, states, buttons, icons, gestures, destinations, rules, and commercialization touchpoints, then reconstruct it as one editable Figma product map. Use for product experience documents, screenshots, DOCX/PDF research, competitor walkthroughs, button-level interaction mapping, product-logic audits, commercialization analysis, safe existing-board writes, or completeness reviews. This is a whole-product teardown, not possible version iteration, release comparison, changelog, or roadmap analysis.
---

# Product Prototype Decomposition to Figma

Break the product apart, then reconstruct its product-design logic as an editable map rather than a screenshot collage. Decompose in this order:

`complete product → user tasks → modules → pages/states → controls → destinations → rules and commercialization → Figma map`.

The output must explain both what the product contains and how its parts work together. Keep two independent axes:

- Classification: `MECE module → functional group`.
- Information architecture: `E → L1 → L2 → L3`, with `S` reserved for states or continuation views.

## Scope boundary

Treat the supplied evidence as coverage of one whole product. Decompose every supported product area, not only a named feature or commercial flow. The aim is a single complete representation of product structure and interaction logic.

Do not include possible version iterations. Do not analyze historical releases, compare old and new versions, write a changelog, infer future features, or propose a roadmap. Retain source dates only as evidence metadata. If documents conflict, use source authority and freshness to select the most reliable product fact instead of turning the conflict into version analysis.

## Required companion skills

Load only what the task needs:

- DOCX input: use the available documents skill and render pages for visual verification.
- PDF input: use the available PDF skill and render pages for visual verification.
- Figma write: load `figma-use` completely before every `use_figma` call.
- Composed Figma board update: also load `figma-generate-design` completely.
- New blank Figma file: load `figma-create-new-file` before creating it.

Explicitly tell the user when one of these skills changes an action or pauses the work.

## Source contract

Before designing, establish:

1. Primary evidence source, coverage, and optional collection date for traceability.
2. Supplemental research sources.
3. Target Figma URL/file and whether to update or create separately.
4. User-edited layers that must be preserved.
5. Visual semantics already adopted, such as pink for commercialization.

Apply this authority order:

`latest user correction > latest primary document > older document > external research > analyst inference`.

Never silently merge conflicting screenshot sequences. Label every conclusion as one of:

- Evidence fact
- Analysis judgment
- Unverified hypothesis

## Workflow

### 1. Extract complete evidence

Read the complete document, including embedded images, tables, captions, notes, and final pages. Render document pages when layout or screenshot order matters.

Create one record per unique screen using the schema in [references/decomposition-schema.md](references/decomposition-schema.md). Preserve source location and original screenshot identity.

Do not claim completeness while images are missing, cropped, placeholder-only, or unreadable.

### 2. Normalize screens and interactions

Assign stable evidence IDs such as `P02–P81`. An ID identifies evidence; it is not a process-step number.

For each screen capture:

- Screen title and user goal
- Entry source
- Clickable button/icon/gesture
- Destination screen or state
- Back/close behavior
- Loading, success, empty, error, permission, and payment states
- Commercialization role
- Evidence confidence

Model each interaction as:

`source page + hotspot → action → destination page/state`.

When two buttons reach the same destination, retain both hotspots and connect both to that destination.

### 3. Build MECE classification

Classify by user task, not by UI type. Each screenshot receives exactly one primary functional-group ownership. Cross-cutting mechanisms are references, not duplicate screenshots.

Typical cross-cutting mechanisms:

- Commercialization
- Community/supply
- Identity/governance
- Safety/compliance
- AI capability/fallback

Audit for:

- No duplicate primary ownership
- No missing evidence IDs
- Functional groups collectively cover the module
- Modules collectively cover the observed product journey

### 4. Assign page hierarchy

Use the definitions in [references/decomposition-schema.md](references/decomposition-schema.md):

- `E`: admission/onboarding flow before the durable product workspace
- `L1`: main navigation destination or primary workspace
- `L2`: independent task page opened from L1
- `L3`: detail, sub-setting, modal, menu, or overlay opened from a parent page
- `S`: loading, generating, success, continued scroll, toggled state, result state, or return-state evidence

Do not force every screenshot into L1/L2/L3. `S` is not “level four.” Record the parent page separately.

### 5. Map commercialization as a complete path

Read [references/figma-visual-system.md](references/figma-visual-system.md) before marking commercialization.

Cover the entire path, not only the checkout page:

`exposure/permission → entry trigger → value promise or limit → metered action → recharge/subscription → success/close/return state`.

Include where evidenced:

- Ads and remove-ads messaging
- Paid model tiers
- Currency balance and recharge entry
- Per-action currency consumption
- Subscription entry, benefits, price, renewal
- Web/App price or channel differences
- Creator monetization or incentives

Do not infer a payment mechanism without evidence. Mark ambiguous cases as hypotheses.

### 6. Plan the Figma board before writing

Produce a decomposition manifest first. Validate it with:

```bash
python3 scripts/validate_decomposition.py decomposition.json
```

Use one editable board with this layer structure:

```text
00 Overview and conclusions
01 Functional-group frames
02 Connectors and actions
03 Screens and screenshots
04 Cross-cutting mechanisms
05 Evidence notes and tips
```

Prefer short horizontal/vertical orthogonal connectors. Avoid cross-board spaghetti lines. Express distant relationships with destination labels and clickable Figma prototype hotspots.

### 7. Write to new or existing Figma safely

Inspect the target first. If a compatible board already exists, write non-destructively:

- Preserve user-created annotations, colors, connectors, and text unless explicitly asked to replace them.
- Add or update only named, tool-owned layers.
- Never delete and rebuild merely to simplify implementation.
- Return all created/mutated node IDs.
- Load each text node's current font before editing it.
- Keep every screenshot, frame, annotation, label, and connector editable.

If direct Figma writing is blocked, do not bypass approvals. Prepare a locally validated plugin or artifact, distinguish “built” from “written,” and give one concrete run action.

### 8. Apply visual rules

Follow [references/figma-visual-system.md](references/figma-visual-system.md).

Minimum requirements:

- Use Noto Sans SC when available.
- Separate the compact `Pxx · Lx` badge from the page title.
- Put action labels next to their real hotspot: `Action → Pxx`.
- Group a parent button and its internal page inside the same functional-group frame when practical.
- Use pink consistently for the complete commercialization path.
- Use restrained colors elsewhere.
- Keep annotations close to screenshots and avoid label/line collisions.

### 9. Validate before declaring completion

Verify:

- Every extracted screenshot appears exactly once.
- Every page has a hierarchy label or justified `S` status.
- Every documented button/gesture has a destination, state effect, or explicit unknown.
- Multiple entrances to one destination remain separate.
- Commercialization coverage includes entry and return states.
- No unsupported commercial claim is presented as fact.
- No text clipping, line crossing, screenshot cropping, or hidden overflow.
- Prototype hotspots actually navigate/scroll to the intended target.
- All deliverable layers remain editable.
- User edits remain intact after rerun.

Report exact counts: screenshots, modules, functional groups, relationships, clickable hotspots, commercial pages, unresolved questions, and verification boundary.

## Output contract

Deliver:

1. Core product-structure judgment.
2. Evidence/analysis/hypothesis separation.
3. Validated decomposition manifest.
4. Editable Figma board or locally runnable non-destructive updater.
5. Completeness and interaction audit.
6. Concise instructions for the user's next action, only if needed.

Never say “written to Figma” unless the target file was read back after the write.
