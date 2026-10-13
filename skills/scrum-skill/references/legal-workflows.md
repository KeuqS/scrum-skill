# Optional legal and privacy workflow routing

Read only for selected legal/privacy work. The Scrum Master, software engineer,
UI/UX, QA, security, operations and AI presets do not require LegalQuants skills.
These are routing recommendations, not copied skills or bundled dependencies.
Resolve the installed host's actual skill name/path; read the selected SKILL.md
and follow its inputs, scope and approval requirements. If absent, report the gap
and use an evidence-first manual workflow or install only within user authorization.

## Legal Counsel

Start with jurisdiction, decision/question, relevant facts and source access.
Turn the needed review into a small outcome with evidence and named decision owner.

| Actual task | Reusable LQ workflow | Important boundary |
| --- | --- | --- |
| Current regulatory requirements/version comparison | [regulatory](https://github.com/LegalQuants/lq-plugin-oss/blob/main/skills/core/regulatory/SKILL.md) | Official instrument/version evidence; unresolved application judgments stay with counsel |
| Whether a source supports a proposition | [proposition-checking](https://github.com/LegalQuants/lq-skills/blob/main/skills/proposition-checking/SKILL.md) | Missing source means unverified, not supported from memory |
| Singapore judgments/citations | [sgcite](https://github.com/LegalQuants/lq-skills/blob/main/skills/sgcite/SKILL.md) | Singapore-specific; verify sources, not merely citation shape |
| Singapore statutory citations | [bart-statutory-reference-checker](https://github.com/LegalQuants/lq-skills/blob/main/skills/bart-statutory-reference-checker/SKILL.md) | Optional tooling/infrastructure; do not claim a deployed checker from a skill file |
| Contract policy from lawyer-selected precedents | [playbook-builder](https://github.com/LegalQuants/lq-plugin-oss/blob/main/skills/transactional/playbook-builder/SKILL.md) | Candidate positions need actual lawyer confirmation |
| Contract against approved policy | [playbook-review](https://github.com/LegalQuants/lq-plugin-oss/blob/main/skills/transactional/playbook-review/SKILL.md) | Approved playbook, clause-linked coverage; issues list does not create a Word redline |
| Defined-term consistency | [definition-check](https://github.com/LegalQuants/lq-plugin-oss/blob/main/skills/transactional/definition-check/SKILL.md) | Record supplied text and evidence rather than inventing missing terms |
| Substantive legal-output challenge | [adversarial-qc](https://github.com/LegalQuants/lq-skills/blob/main/skills/adversarial-qc/SKILL.md) | Use only authorized/available agents/providers; disclose actual independence; no professional sign-off |

Litigation-specific plugins/workflows apply only to litigation tasks; do not silently
import US procedure into another jurisdiction. This map references source skill names;
installations may display `lq-` aliases or plugin namespaces.

## PDPA/GDPR Counsel

1. Determine applicable jurisdiction/regime, parties' actual roles, data categories,
   purposes, recipients, locations and decisions needing human counsel. PDPA and GDPR
   are distinct regimes; a profile selection alone establishes neither applicability.
2. Map collection, use, storage, logs/backups, disclosure, model calls, retention and
   deletion with engineering/security. Mark observed facts separately from unknowns.
3. Verify relevant obligations using current official instruments and guidance through
   `regulatory`; maintain a requirement-to-control/evidence map, with residual issues.
4. For provider DPAs use [dpa-checklist-review](https://github.com/LegalQuants/lq-skills/blob/main/skills/dpa-checklist-review/SKILL.md)
   only for a supported, identified regime and supplied agreement. Its enumerated
   regimes do not include a dedicated Singapore PDPA checklist; use official PDPA
   sources and a tailored counsel-reviewed checklist rather than mislabeling GDPR results.
5. For legal AI privacy/data boundaries use [local-first-legal-workspace](https://github.com/LegalQuants/lq-skills/blob/main/skills/local-first-legal-workspace/SKILL.md).
   No code/runtime evidence means an audit plan, not an asserted local-only guarantee.
6. Check legal propositions, challenge findings and present source-linked gaps/options
   to accountable counsel. Engineering implements controls; QA checks their behavior;
   neither substitutes for legal applicability and judgment.

Professional starting points: [PDPC assessment guidance](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/dpia/guide-to-data-protection-impact-assessments-14-sep-2021.pdf)
and [EDPB design/default guidance](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201904_dataprotection_by_design_and_by_default_v2.0_en.pdf).
Check current versions and applicable law during actual legal work; this routing
guide is not a conclusion that a particular product is compliant or a DPIA is required.
