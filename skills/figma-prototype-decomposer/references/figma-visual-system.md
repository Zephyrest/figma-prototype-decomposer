# Figma visual system

## Contents

- Reading order
- Screen card
- Interaction notation
- Functional grouping
- Commercialization
- Editing and rerun safety

## Reading order

Use a consistent left-to-right primary flow. Place branch pages beside or below their parent. Keep the most important closed loop readable without following long cross-board lines.

## Screen card

Use this order:

1. Compact badge: `P13 · L1`
2. Short verb-object title: `进入故事聊天`
3. Complete, uncropped screenshot
4. Hotspot circles located on the real control
5. Nearby action label: `选择模型 → P14`
6. Optional faint note below the screenshot

Badge and title must not collide. Prefer 12–13 px badges, 16–18 px page titles, and 12–14 px action labels when the full board is viewed as one page.

## Interaction notation

- Circle the real button/icon position.
- Show numbers only when one screen has multiple hotspots.
- Connect the circle directly to its nearby label.
- Use short horizontal/vertical orthogonal connectors.
- Put arrowheads only at destinations.
- Use `Action → Pxx` even when a visible long connector is intentionally omitted.
- Make the transparent hotspot clickable with `SCROLL_TO` when screens are nested in one long board.

Group a parent button and its modal/detail/setting page inside the same functional-group frame when practical. This visually communicates “internal page” without confusing it with the next step in the global journey.

## Functional grouping

Use one restrained boundary color for ordinary functional groups. Labels sit close to the grouped screens. Do not use a new color for every module.

MECE groups answer “which user task owns this evidence?” Page hierarchy answers “how deep is this view?” Do not replace one with the other.

## Commercialization

Reserve pink (`#F05A9D` or the user's existing pink) for commercialization:

- Pink hotspot and action label for a monetized trigger
- Subtle pink screenshot outline for a commercial page/state
- Small pink pill below the screenshot, such as `商业化｜Pieces 充值`
- Pink connector only for the commercial branch

Mark the full path:

`ad exposure/permission → recharge or subscribe trigger → paid value/limit → checkout or spend → return state`.

Do not recolor unrelated navigation merely because it occurs inside a chat module containing ads.

## Editing and rerun safety

- Use editable Figma Text, Frame, Vector, Ellipse, and Rectangle nodes.
- Group each hotspot circle, number, leader, label, and transparent click target.
- Name layers semantically.
- Keep user-created nodes outside the tool-owned naming prefix.
- On rerun, mutate known tool-owned nodes; preserve unknown/user-created nodes.
- Never flatten the final board into one image.
