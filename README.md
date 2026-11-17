# ai-skills

This repository collects Claude skills, tools, mods and plugins, grouped by type. Each item is self-contained.

→ The **[INDEX](INDEX.md)** lists everything here.

## Layout

```
ai-skills/
├── INDEX.md                    ← catalog (keep updated)
├── .claude-plugin/
│   └── marketplace.json        ← makes this repo installable as a Claude Code plugin marketplace
├── skills/<skill-name>/        ← Agent Skills (SKILL.md + references/ + agents/ + evals/)
├── plugins/<plugin-name>/      ← Claude Code plugins (.claude-plugin/plugin.json, commands, hooks…)
├── mods/<mod-name>/            ← Claude UI/behaviour mods (themes, panels, status lines)
└── tools/<tool-name>/          ← standalone scripts / CLIs / MCP servers
```

## Install

**Claude Code (plugin marketplace):**
```bash
/plugin marketplace add yaronr/ai-skills
```
```bash
/plugin install product-management@ai-skills   # installs product-management + product-ops
```

**Manual install (any Claude Code setup):** copy a skill folder into your skills directory.
```bash
cp -r skills/product-management skills/product-ops ~/.claude/skills/
```

**Claude.ai:** zip the skill folder. Then upload it under Settings → Capabilities → Skills.

## Conventions

- **Folder names:** use `kebab-case`. A skill's folder name must match the `name` field in its frontmatter.
- **Context budget:** keep each `SKILL.md` under about 500 lines. Put depth in `references/` and load it only when it's needed.
- **Tests:** add them under `evals/<case>/`, in the `claude plugin eval` layout.
- **New items:** add a row to [INDEX.md](INDEX.md), and to `.claude-plugin/marketplace.json` if the item is a skill or plugin.
- **Privacy:** keep no personal data, secrets or employer-confidential content in this repo.

## License

[MIT](LICENSE)
