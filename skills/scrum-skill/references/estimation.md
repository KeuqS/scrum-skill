# Story points, Planning Poker and scope history

Use story points for this point-based workflow when the team selects them. They are
relative effort/uncertainty estimates, not hours or productivity targets. Scrum does
not require points or Planning Poker. Developers own sizing; the PO clarifies value
and criteria, and the Scrum Master facilitates.

## Attach estimates to stories

Keep stable ID, outcome, criteria, scope membership, dependencies and DoD. Record
points as number or null, estimate state (unestimated/proposed/agreed), method,
actual participants, decision/source/date, reference item and uncertainty. Select
an agreed scale such as 1,2,3,5,8,13. Null is unknown, not zero; explicit agreed zero
is valid if the team uses it. Show proposed forecasts separately from adopted estimates.

## Planning Poker

1. Explain the story, boundaries and acceptance/DoD effort; clarify questions.
2. Compare reference items; estimators choose privately before seeing others.
3. Reveal together and inspect the highest/lowest assumptions and overlooked risks.
4. Clarify/split and repeat a bounded round when useful.
5. Record the actual adopted estimate or unresolved range/questions; don't average
   away disagreement merely to fill a field.
6. Retain actual votes, participants, assumptions and follow-up evidence privately.

AI estimates are proposals. Do not invent human votes, agreement or independent
provider opinions. Single-agent reasoning is not Planning Poker. Record the actual
method and any human decision adopting forecasts. Sources:
[Planning Poker](https://www.mountaingoatsoftware.com/agile/story-points/planning-poker),
[points are optional](https://www.scrum.org/resources/blog/myth-9-story-points-are-required-scrum).

## Capacity and observed delivery

Select a usable slice using actual availability, reviews/testing, support work,
dependencies and uncertainty. Without measured history, capacity is a provisional
forecast. Do not divide backlog by invented velocity or convert points to a two-week
schedule. Dates/timeboxes require actual choices; agent cycles do not establish formal events.

Velocity sums frozen adopted points of items meeting DoD in that completed Sprint.
No partial credit or active-Sprint velocity. Carryover retains its ID and is counted
once when Done. Never recalculate old velocity from latest backlog estimates.

## Scope ledger and dashboard mapping

Record every add/remove/reestimate/split/reopen: event ID/date, affected IDs, previous
and new values, reason, decision/source and affected checkpoint. Keep original scope,
current backlog and frozen Sprint snapshots separate. Total estimated points can rise
or fall; unestimated items remain separately visible.

- Removal of unfinished work is not completion.
- Split stories retain parent linkage; exclude the retired parent from current totals.
- Reestimate current work with an event without rewriting closed snapshots.
- Reopened Done work becomes a linked rework item by default; retain historical credit
  and estimate new work. Old-record corrections need explicit provenance/versioning.

Capture scope/completed/unknown-size counts at actual checkpoints, change deltas and
frozen completed-Sprint items. Map an explicit dataset using the dashboard skill's
references/schema.md; missing history stays missing, never invented from current Markdown.
Current/proposed totals aren't proof of all-project completion or acceptance.
