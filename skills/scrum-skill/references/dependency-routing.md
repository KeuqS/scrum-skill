# Use an external skill or library

This package supplies workflow instructions, not an external-skill runtime or dependency
installer. A source link identifies a candidate; it does not establish host availability.
Use this guide when a selected role needs an external skill or application library.

## Resolve, load and use

1. Select a workflow from the actual task. For platform counsel read legal-workflows.md;
   for UI use the selected design profile. Keep LQ routing confined to legal/privacy work.
2. Inspect the host's available skill catalog or approved installed directories. Resolve
   the exact registered name/namespace or local SKILL.md path. Read metadata and relevant
   prerequisites; record the selected source/version when available. Resolve duplicate
   versions explicitly. A sibling project's vendored skill is not automatically available.
3. Where the host exposes native skill invocation, use that actual capability/name.
   Otherwise, if approved local instructions are readable, load the full SKILL.md and
   needed references and follow them. Record this as instruction loading, not proven
   native registration. Never run slash commands as shell commands or invent a tool.
4. Check required inputs, supported jurisdiction/surface, executable helpers and project
   authorization. Follow the loaded skill's scope and approval boundaries; task assignment
   does not authorize paid calls, new providers, hooks, installs or confidential transfer.
5. Execute the authorized workflow and inspect its actual output. Record unavailable
   dependencies or prerequisites and an appropriate fallback; never claim a missing skill
   was used. Missing inputs can yield a bounded question/plan, not a fictitious review.

Give a delegated worker the selected role, exact skill identity/path, task, inputs,
scope and evidence requirement. Check what the worker can access in its own context;
do not assume skills are preloaded. Where supported, preloading uses the host's real
agent configuration, not this package's generic Markdown profiles. See
[Claude subagent skill loading](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents).

## Skills versus libraries

| Dependency | What constitutes use |
| --- | --- |
| LQ workflow | Load the selected installed instructions, satisfy its inputs and perform its review/research workflow |
| taste-skill | Resolve its installed identity (which may be design-taste-frontend), read and apply it to the appropriate UI surface |
| Impeccable | Load its installed instructions and relevant command guide; use its actual launcher/workflow when requested and available |
| GSAP / Lenis | Resolve the target app's installed package, import it in application code and verify the relevant motion/scroll behavior |

GSAP and Lenis are not skills or slash commands. A package declaration is not an
installed module; an import alone does not prove browser behavior. Use the target
app's dependency/lockfile policy when installation is authorized. No global install
or copying upstream source into this skill is required.

## Evidence in the ordinary handoff

Record the requested workflow, resolved identity/path/version, whether instructions
were loaded or native invocation observed, what actually ran, output/checks and gaps.
Keep selected, available, loaded and executed distinct. Report a manual fallback as
a fallback. A successful package test for scrum-skill does not establish external
skill activation, model judgment or professional approval.
