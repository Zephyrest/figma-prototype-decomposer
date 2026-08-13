# Decomposition manifest schema

## Contents

- Required JSON structure
- Page hierarchy
- Relationship types
- Evidence rules
- Validation example

## Required JSON structure

```json
{
  "product": "Product name",
  "evidence_scope": "which parts of the whole product the supplied material covers",
  "evidence_collected_at": "optional source date for traceability only",
  "pages": [
    {
      "id": "P02",
      "title": "Page title",
      "module": "MECE module",
      "group": "Functional group",
      "level": "E",
      "parent": null,
      "kind": "page",
      "source": "document/page/image reference",
      "commercial": null,
      "confidence": "fact"
    }
  ],
  "interactions": [
    {
      "from": "P02",
      "hotspot": "Google login",
      "action": "click",
      "to": "P03",
      "commercial": false,
      "confidence": "fact"
    }
  ],
  "unknowns": []
}
```

## Page hierarchy

| Code | Meaning | Examples |
|---|---|---|
| E | Admission flow before durable workspace | Login, age gate, ad permission |
| L1 | Main navigation destination or primary workspace | Home, chat workspace, Create, My Page |
| L2 | Independent task page opened from L1 | Search, library, creation step, notification settings |
| L3 | Detail/sub-setting/modal/menu/overlay | Model picker, chat menu, recharge sheet, edit dialog |
| S | State evidence, not a deeper page level | Loading, generation, success, continued scroll, return state |

For `S`, set `parent` to the durable page whose state is shown.

`kind` should be one of: `page`, `modal`, `overlay`, `menu`, `state`, `continuation`.

## Relationship types

Use one of:

- `click`
- `gesture`
- `back`
- `close`
- `sequence`
- `generate`
- `pay`
- `subscribe`
- `ad`
- `unknown`

One source hotspot should have one primary destination. If behavior is conditional, create separate interactions and state the condition.

## Evidence rules

`confidence` must be:

- `fact`: visible in supplied evidence
- `analysis`: reasoned product interpretation
- `hypothesis`: plausible but not verified

Commercial categories may include:

- `ad_permission`
- `ad_inventory`
- `remove_ads`
- `paid_model`
- `currency_entry`
- `currency_recharge`
- `currency_spend`
- `subscription_entry`
- `subscription_checkout`
- `subscription_return`
- `creator_incentive`

## Validation example

```bash
python3 scripts/validate_decomposition.py /absolute/path/decomposition.json
```

The validator checks unique page IDs, hierarchy codes, one primary ownership per page, valid interaction endpoints, unique hotspot destinations, and commercial metadata.
