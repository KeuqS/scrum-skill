---
name: scrum-dashboard
description: Generate an offline interactive Scrum project dashboard with sprint burndown, changing scope, velocity and dated timeline from explicit local project records or a labeled synthetic demo.
---

# Scrum dashboard

Create a local viewing artifact, not a new system of record or a promise of delivery.
Read the project's actual instructions and records first. Keep personal/project information
local; use `.scrum/dashboard/` when its ignore policy is confirmed. Do not publish, deploy,
import dependencies or connect services without project authorization.

Use [references/schema.md](references/schema.md) to map records. Missing estimates,
dates, scope history or DoD evidence remain missing. Never substitute AI votes for
Developers' planning-poker decisions or call provisional estimates measured velocity.
Story points and planning poker are optional team practices, not Scrum requirements.

The view is **project burndown by Sprint**, with remaining points and a changing total
scope line. No daily chart or separate burnup view is generated. Velocity includes only
closed Sprints and DoD-complete frozen items.
Preserve historical snapshots independently of current backlog edits, and make additions,
removals and re-estimation visible. Do not award partial points or compare teams by points.

For a practical standalone HTML dashboard, run the bundled Python 3.10+ helper:

```sh
python <skill-path>/scripts/generate_dashboard.py --demo --output .scrum/dashboard/demo.html
python <skill-path>/scripts/generate_dashboard.py --input .scrum/dashboard/data.json --output .scrum/dashboard/project.html
```

Outputs are created exclusively: choose a new filename to refresh; no silent overwrite.
The generator reads only the explicit input file. The dashboard has no server, fetch,
CDN, telemetry, third-party libraries or installation requirement. It embeds all supplied
data, so sharing the HTML shares that data. Do not commit real project exports.

Inspect desktop/mobile renders and keyboard use; check metric tables against input.
The bundled Operate-mode design is usable without external design skills. If redesign
is requested, use available Impeccable/minimalist guidance; taste-skill's landing-page
scope must not be misreported as a dashboard dependency. GSAP/Lenis are not needed for
static charts and must not be installed merely to satisfy a dependency checklist.

Return the actual file path, evidence, missing data and limitations. Record a handoff
in the project's existing format. Browser local-file rendering is not hosted deployment,
and unit tests alone do not establish visual accessibility or full host invocation.
