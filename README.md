# Figma Prototype Decomposer

把材料所覆盖的整个产品“全部拆碎”：从体验文档、竞品调研、截图、DOCX 或 PDF 中，逐层拆出产品模块、页面层级、页面状态、按钮与图标、跳转关系、业务规则和商业化触点，再系统重组成一张可编辑的 Figma 产品结构与交互图。

这里的“拆碎”是对**整个产品现状的完整拆解**：目标是看清产品现在由什么构成、页面如何分层、用户点击哪里会到哪里，以及商业化如何嵌入产品。它不涉及可能的版本迭代，不比较旧版与新版，不整理更新日志，也不推测未来路线图。

Turn product walkthroughs, competitor research, screenshots, DOCX, and PDF evidence into an editable Figma product-structure and interaction map.

## 中文说明

### 它解决什么问题

普通竞品调研容易变成“截图堆叠”：页面很多，却看不清产品结构、按钮去向、主流程和商业化机制。

这个 Skill 的核心动作是**把产品拆碎，再按产品设计逻辑重新拼起来**：

```text
完整产品
→ 用户任务与功能模块
→ 一级/二级/三级页面与页面状态
→ 页面内按钮、图标和手势
→ 每个操作指向的内部页面
→ 背后的业务规则、商业化与产品判断
→ 可阅读、可验证、可编辑的 Figma 产品地图
```

它既能回答“这个产品有什么”，也能回答“用户点击哪里、为什么进入这里、页面之间是什么父子关系、哪里发生付费、这一整套机制如何形成闭环”。

这里的“完整”指材料能够覆盖的产品全貌，而不是只拆一个功能专题。若材料没有覆盖某些页面，就把它们列为待补证据，不用猜测补齐。来源日期仅用于追溯证据，不进入产品结构，也不作为版本分析维度。

这个 Skill 会把材料整理成四层信息：

1. **证据层**：每张截图有稳定的 `Pxx` 编号、来源和事实置信度。
2. **分类层**：使用 `MECE 模块 → 功能组`，确保页面不重不漏。
3. **结构层**：使用 `E / L1 / L2 / L3 / S` 区分准入流程、主入口、任务页、详情页和页面状态。
4. **交互层**：记录真实按钮、图标和手势，并标明 `动作 → Pxx`。

商业化不是只标支付页，而是还原完整链路：

`曝光或权限 → 商业化入口 → 价值/限制 → 计费动作 → 充值或订阅 → 成功/关闭/返回状态`

### 适用场景

- AI 陪伴、内容社区、工具类产品的竞品拆解
- 从产品体验文档还原页面结构和交互
- 审核现有 Figma 流程图是否重漏或错连
- 标注广告、虚拟货币、付费模型、订阅和创作者激励
- 将研究结果制作成可编辑、可继续维护的 Figma 交付物

### 核心原则

- MECE 解决分类，页面层级解决结构，两者不能互相替代。
- `S` 表示加载、生成、滚动续页或结果状态，不是第四级页面。
- 同一目标页的多个入口必须保留多个真实点位。
- 所有结论区分为证据事实、分析判断和未验证假设。
- 更新已有 Figma 时保留用户手动修改，只改 Skill 自己管理的图层。
- 没有回读 Figma 验证，就不能声称“已经写入”。

## English overview

### What it does

This skill fully decomposes the whole product covered by the supplied evidence. It breaks the product into its smallest meaningful product-design units—modules, page hierarchy, states, controls, destinations, business rules, and monetization touchpoints—then reconstructs them as one structured, editable Figma map.

Its purpose is to explain how the product is currently structured and how its interactions work. It does not cover possible version iterations, compare releases, create changelogs, or infer a roadmap. Source dates are retained only for evidence traceability.

It maintains two independent axes:

- **Classification:** `MECE module → functional group`
- **Information architecture:** `E → L1 → L2 → L3`, with `S` reserved for states and continuation views

It also maps each interaction as:

`source page + hotspot → action → destination page/state`

Commercialization is modeled end to end, including exposure, entry points, paid value, metered actions, checkout, subscription, and return states.

## Repository structure

```text
skills/figma-prototype-decomposer/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── decomposition-schema.md
│   └── figma-visual-system.md
└── scripts/
    └── validate_decomposition.py
examples/
└── decomposition.example.json
```

## Installation

Copy the skill directory into your personal Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/figma-prototype-decomposer ~/.codex/skills/
```

Restart Codex after installation.

## Usage

Example prompt:

```text
Use $figma-prototype-decomposer to read this product research document,
extract all screens and button-level interactions, audit it with MECE and page hierarchy,
mark the complete commercialization paths, and create an editable Figma map.
```

中文示例：

```text
使用 $figma-prototype-decomposer，读取这份产品体验文档，
整理全部页面、按钮级交互和页面层级，标注完整商业化路径，
并生成可编辑的 Figma 产品拆解图。
```

## Validate a decomposition manifest

```bash
python3 skills/figma-prototype-decomposer/scripts/validate_decomposition.py \
  examples/decomposition.example.json
```

The validator checks page-ID uniqueness, hierarchy values, parent-state relationships, interaction endpoints, hotspot conflicts, and commercialization metadata.

## Privacy

The repository contains only the reusable workflow and a synthetic example. It does not contain private research documents, product screenshots, Figma links, credentials, or company data.

## License

No license has been selected yet. Add one before publishing the repository for public reuse.
