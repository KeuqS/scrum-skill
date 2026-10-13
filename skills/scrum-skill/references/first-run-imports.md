# First-run dependency setup

Run when initializing a consumer or adding a role with external dependencies. Inspect
existing installations first. Produce a concrete import plan: selected roles, host,
scope (project/user/workspace), upstream identities and reviewed revisions, target app,
missing dependencies and commands. Reuse prior installation authorization; otherwise
present this plan for approval before installing. Do not require repeated approval.

Required means required for the selected preset, not every possible project. A clean
scrum-skill import alone does not include these dependencies. If an essential tool is
missing, complete independent planning but keep the affected specialist workflow
unready until import/verification or an explicit user-chosen fallback.

## Select the import set

| Selected work | Import set |
| --- | --- |
| Core engineering/QA/security/SM | No LQ or design dependencies |
| Platform Legal Counsel / privacy counsel | LQ transactional bundle, including shared regulatory; extra bundles only for their actual tasks |
| Full LQ catalog explicitly requested | Transactional, litigation and companion bundles; install all, load only relevant workflows |
| Web UI/UX preset | taste, minimalist and redesign skills; Impeccable; GSAP and Lenis in target web app |
| React web UI | Also @gsap/react |
| Native UI / non-web project | Relevant design instructions; omit web libraries unless applicable |

The LQ OSS catalog does not contain the legacy local-first, proposition-checking,
DPA-checklist or adversarial-QC skills linked by optional routes. Installing all
three bundles does not create them. Use the available regulatory workflow for
source-backed platform research; mark legacy routes unavailable. If those specific
workflows are required, separately review/import them from their source repository
under explicit scope, or agree a manual alternative. Never silently substitute names.

## Host-native LQ import

For Codex:

```sh
codex plugin marketplace add LegalQuants/lq-plugin-oss
codex plugin add legalquants-transactional@legalquants-skills
```

For Claude Code:

```sh
claude plugin marketplace add LegalQuants/lq-plugin-oss
claude plugin install legalquants-transactional@legalquants-skills
```

Full-catalog mode adds legalquants-litigation and legalquants-companion with the
same host command. Inspect existing catalog entries before adding duplicates.
Use a reviewed ref/pin when the host supports it; record actual installed revision.
GUI/org-managed hosts use their approved import/catalog UI and administrator access;
do not assume terminal commands install into that workspace.
See [upstream LQ installation](https://github.com/LegalQuants/lq-plugin-oss#install-an-audience-plugin-from-a-native-catalog).

## Design skill imports

With the reviewed skills installer, these examples select Codex project skills:

```sh
npx skills add Leonxlnx/taste-skill --skill design-taste-frontend --agent codex
npx skills add Leonxlnx/taste-skill --skill minimalist-ui --agent codex
npx skills add Leonxlnx/taste-skill --skill redesign-existing-projects --agent codex
npx skills add pbakaus/impeccable --skill impeccable --agent codex
```

For Claude use --agent claude-code, or the upstream native plugin marketplace route.
Select one route, appropriate scope and reviewed source/installer version; inspect
the import plan before execution. Commands above are upstream discovery examples,
not a claim their floating defaults are pinned. Preserve existing installations;
review upgrades/collisions instead of overwriting them. Native plugin namespace can
differ from folder/frontmatter name. Keep each skill's references/scripts/assets.
See [taste installation](https://github.com/Leonxlnx/taste-skill#installing) and
[Impeccable installation](https://impeccable.style/docs/).

Impeccable's recommended installer can add host integrations; its engine can download
on first execution. Include engine/tool readiness in the concrete plan. Installing
instructions does not authorize hooks, telemetry settings, image-provider setup or
paid image/model calls. Follow actual user choices and installed instructions.

## Application libraries

Identify the actual app/package manager and existing lockfile first. For npm web apps:

```sh
npm install gsap lenis
# React apps only:
npm install @gsap/react
```

Run in the target app/workspace, not this skill repository. Use the project's version
policy and record resolved versions/lock changes. Preserve already satisfactory
dependencies. No app/package manifest yet means defer library installation until the
app exists; do not invent an npm project solely to mark this step complete.

## Verify before specialist execution

Record a dependency register under the consumer's local Scrum workspace: selected
dependency, source/ref, scope, actual host name/path/version, import outcome and gaps.
Reload/start the host session if required. Confirm the worker's actual skill catalog
and readable full instruction resources, load the needed guide and run an appropriate
authorized smoke check. For libraries verify resolution/import and later browser
motion, cleanup and reduced-motion behavior. For Impeccable verify usable launcher/
engine before claiming command readiness; for LQ check helper runtimes and inputs.

Keep imported, discoverable, loaded and executed distinct. A successful CLI exit or
clone alone does not establish host activation. Resume incomplete setup without
reinstalling known dependencies. Imported upstream code belongs in consumer-managed
skill/plugin locations or app dependencies, not in scrum-skill's published source.
