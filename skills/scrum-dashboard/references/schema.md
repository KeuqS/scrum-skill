# Dashboard records (schema version 1)

JSON contains `schema_version: 1`, `project`, `backlog`, and ordered `sprints`.
The generator validates types, IDs, finite nonnegative estimates and ISO dates.

- `project`: `name`, `goal`, `data_kind` (`project` or `synthetic`).
- `backlog`: current items with unique `id`, `title`, `points` (number or null),
  `status` (`backlog`, `in_progress`, `done`) and boolean `dod_met`. Done requires DoD.
- `sprints`: unique `id`, `label`, `state` (`planned`, `active`, `completed`);
  optional `start_date` and `end_date`; optional `snapshot` object containing
  `scope_points`, `completed_points` (cumulative across this project at that checkpoint),
  `unestimated_count`. Scope and completion use a consistent estimating convention.
- A completed Sprint may contain `velocity_items`: unique `{id, points, dod_met}`
  frozen completion records. Only `dod_met: true` contributes velocity. A missing
  list means velocity unknown; an explicit empty list means zero completed points.
  The same Done item cannot be counted in two Sprints. Active/planned Sprints never
  report measured velocity.
- Optional `scope_changes`: `added_points`, `removed_points`, `reestimated_delta`
  (the last can be signed). This records changes since the preceding checkpoint;
  absent changes mean unknown, not zero. The chart does not manufacture an ideal line.
  Consecutive known snapshots must reconcile scope delta to additions minus removals
  plus re-estimation. Cumulative completion must not decrease; reopened Done work is
  a linked new rework item, preserving earlier completion evidence.
- Optional `timeline`: `{title, start_date?, end_date?, kind: 'actual'|'forecast'}`.
  Missing date ranges stay in the table, without invented bars. Forecast bars are dashed.

Snapshots are deliberately explicit: changing a current item's points must not rewrite
earlier scope/completion/velocity. A scope checkpoint can have unknown-size items:
charts display known estimated scope only and the table identifies unestimated counts.
Remaining known points equals snapshot scope minus completed; it can rise when scope
is added. Removing an item does not imply completing it. Keep completed work in cumulative
scope if using a cumulative completion metric. Split/new estimates need recorded decisions.

Use Developers' actual agreed estimates. If using planning poker, prepare criteria and
reference stories, obtain independently chosen votes, discuss disagreement, re-vote and
record the agreed estimate/participants and unresolved questions. Do not invent votes.
Preserve estimate changes in the project's decision/history records. Gantt is supporting
forecast practice, not a formal Scrum artifact or binding individual commitment.

The generator checks structural consistency, not whether agreement or DoD evidence
actually exists. Map those fields only after inspecting estimate decisions and evidence.
For proposed estimates, label the report provisional and retain provenance in the
project's estimate ledger; do not present it as measured team agreement.

The synthetic [demo dataset](../assets/demo.json) shows growing and shrinking scope,
an unestimated item, closed-Sprint velocity, a current Sprint and forecast dates.
