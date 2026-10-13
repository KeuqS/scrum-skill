# Inventory setup example

An invented scenario demonstrating the Python scaffold helper, not an installed
Codex/Claude conversation or a completed Sprint. All planning stays proposed.

```sh
python skills/scrum-skill/scripts/init_workspace.py --root /path/to/empty-project --name inventory-demo --goal "Staff can inspect stock changes" --specialists engineering,qa,design --product-owner "Example PO" --scrum-master "Example facilitator"
```

Actual helper output from a fresh isolated directory:

```text
Wrote 22 files; existing records preserved.
.scrum\workspace.json
.scrum\PRODUCT_GOAL.md
.scrum\TEAM.md
.scrum\PRODUCT_BACKLOG.md
.scrum\DEFINITION_OF_DONE.md
.scrum\DECISIONS.md
.scrum\IMPEDIMENTS.md
.scrum\EVIDENCE.md
.scrum\sprints\SPRINT-01.md
.scrum\sprints\SPRINT-01-PLANNING.md
.scrum\sprints\SPRINT-01-REVIEW.md
.scrum\sprints\SPRINT-01-RETROSPECTIVE.md
.scrum\handoffs\INITIAL.md
.scrum\handoffs\LATEST.md
.scrum\MASTER_PROMPT.md
.scrum\ACCOUNTABILITIES.md
.scrum\roles\engineering.md
.scrum\roles\qa.md
.scrum\roles\design.md
AGENTS.md
CLAUDE.md
.gitignore
```

Read the generated records, refine actual stories/DoD and begin delivery only when
requested. Repeating setup preserves existing decisions. See [setup guidance](../../skills/scrum-skill/references/workspace.md).
