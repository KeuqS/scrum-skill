# Invocation modes, roles and guided setup

One canonical skill handles these arguments. These examples are requests to the host
agent; they are not shell commands or automatically registered individual agents.
Codex uses `$scrum-skill`; Claude plugin uses `/scrum-skill:scrum-skill` with the same
arguments. A direct Claude skill install uses `/scrum-skill`.

## Explicit workflow modes

| Mode | Outcome and boundary |
| --- | --- |
| wizard / no arguments | Inspect state and guide missing choices; no automatic implementation/install |
| setup | Create/reconcile local team, artifacts and dependency import plan |
| resume | Reconcile latest handoff with actual files/evidence; preserve decisions |
| plan | Refine outcomes, Goal, capacity and Developers' plan; proposals stay proposals |
| deliver | Execute the requested bounded slice under actual project authorization |
| review | SM: Sprint Review preparation; specialist: scoped discipline review |
| retro | Inspect collaboration/quality and owned measurable improvements |
| doctor | Diagnose artifacts/dependency readiness; report findings, no silent repair |
| dashboard | Use available scrum-dashboard with explicit local data; no automatic publication or inferred history |

```text
$scrum-skill setup --goal "Staff can inspect stock changes" --roles engineering,qa,design
$scrum-skill resume
$scrum-skill plan --cadence "2 weeks"
$scrum-skill deliver --target US-7
$scrum-skill review
$scrum-skill retro
$scrum-skill doctor
```

## Role-specific requests

```text
$scrum-skill role engineering plan --target apps/api
$scrum-skill role design plan --target apps/web
$scrum-skill role qa review --target .github/workflows/ci.yml
$scrum-skill role security review --target docs/architecture
$scrum-skill role legal-counsel review --target docs/architecture
$scrum-skill role privacy-counsel review --target docs/security/DATA_FLOW.md
```

Additional roles: ai, operations, domain-reviewer. Aliases: sm, engineer,
software-engineer, ui-ux, ux, legal, privacy, ops. Custom specialisms use
`role domain-reviewer plan --profile .scrum/roles/horticulture.md`.
Read the actual target/profile after resolving it under project permissions; a string
argument does not establish existence, trust or authorization. Role selection is AI
assistance and does not appoint a human PO, SM, lawyer or DPO.

For role review, load the selected profile and dependency guidance; do not turn a
legal platform-risk request into a generic contract review, or a QA pipeline review
into a fictional Sprint Review. A role deliver request is still bounded by the actual
user task, repository permissions and applicable human decisions.

## Guided wizard

1. Read applicable instructions and existing records first. Detect a resume situation;
   do not initialize a second board or overwrite existing choices.
2. Offer a short context-aware choice: setup, resume, plan, delivery, review/retro or
   dependency diagnosis. Recommend based on evidence; do not start delivery on a bare call.
3. Gather only missing essentials in a small batch: desired outcome, actual accountable
   people (or unresolved), specialist roles, useful cadence and record visibility.
   Preserve supplied preferences and project decisions rather than asking again.
4. Present the concrete setup/dependency import plan and any human decisions. Install
   only under actual authorization; reuse standing grants. Missing required tools keep
   the affected work unready, not fictitiously completed.
5. Create/reconcile artifacts and selected profiles. Report actual evidence, unresolved
   inputs and the next usable invocation. Continue delivery only when requested.

Host-supported input UI is optional; ordinary concise questions also work. Do not
require a particular question tool, account integration or external provider.

## Optional deterministic resolver

```sh
python <skill-dir>/scripts/route_invocation.py 'role legal-counsel review --target docs/architecture'
```

It returns intent JSON only. It performs no filesystem/network/model operation,
installation, delegation or deployment. Typos in explicit role/mode/flags fail with
helpful errors; multiword natural-language requests remain supported for agent intent
resolution. The agent may resolve equivalent intent directly when Python is absent.
Never evaluate argument values as code or interpolate them into a shell command.

If a shell rewrites embedded quotation marks, pass the request via stdin instead:
`python <skill-dir>/scripts/route_invocation.py --stdin`. In PowerShell, pipe a
single-quoted here-string containing the request; in Bash use a quoted heredoc.
Use the host's appropriate text encoding. This avoids native argument reconstruction.
