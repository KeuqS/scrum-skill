# Full project workflow review

The package provides guidance and local records from discovery through operational
handover. It is an orchestration aid; generating records does not establish actual
Scrum events, human appointments, agreed estimates, legal sign-off or release approval.

| Stage | Coverage | Evidence or boundary |
| --- | --- | --- |
| Discovery | Beneficiary, problem, assumptions, measurable Product Goal, first experiment | Project lifecycle guide; findings need project evidence |
| Setup/resume | Team accountabilities, selected specialisms, DoD, backlog, decisions and handoffs | Non-destructive helper; unresolved identities stay unresolved |
| Refinement/estimation | Outcomes, acceptance criteria, story points, uncertainty, Planning Poker | Actual participants and agreement required; agent estimates stay proposed |
| Planning | Why, what, how; capacity, risks and Developers' plan | Event preparation is distinct from an event held |
| Delivery | Bounded authorized work, tests, CI, quality, specialist checks | Exact revision evidence; unavailable gates remain unresolved |
| Inspection | Review preparation, actual feedback, backlog adaptation, retrospective improvements | No invented feedback or Done status |
| Metrics | Sprint burndown, closed-Sprint velocity, changing scope, progress, dated timeline | Explicit JSON snapshots; missing data visible; no daily view |
| Release/operations | Environment, evidence, actual release decision, recovery and support ownership | Source merge is separate from deployment/release |
| Continuity | Latest checkpoint, decisions, evidence, next bounded action | Existing records preserved; no automatic cross-project sync |

## Gaps addressed in this revision

Estimates now have a dedicated decision ledger and story-level fields. Guidance explains
private Planning Poker votes, discussion, re-voting and genuine agreement, without
fabricating a ceremony. Scope records distinguish additions, removals and re-estimation;
closed-Sprint velocity is frozen and unfinished work earns no partial points.

A separate dashboard skill consumes explicit snapshots and an initially empty metrics
file. Current backlog edits do not alter historical snapshots. Discovery and operational
handover guidance connect the previously event-focused workflow into a project lifecycle.

## Validation and remaining limits

Regression checks cover preservation, invocation parsing, two-skill package metadata,
metric reconciliation, duplicate completion, missing estimates, input failures and safe
HTML embedding. Synthetic desktop/mobile renders were inspected; filtering, keyboard
focus, reduced motion and browser errors were checked with a headless browser.

There is no persistent service, automatic Markdown-to-JSON synchronization, multi-user
Planning Poker application, issue tracker integration or automatic native tool executor.
The host agent must load relevant guidance, obtain actual project decisions and maintain
records. Native installed Codex/Claude end-to-end role activation remains a follow-up;
metadata checks and a deterministic resolver do not establish it. Screen reader and
real-device testing remain open. More real project cycles should become anonymized
regression scenarios, with no private project content copied into this public package.
