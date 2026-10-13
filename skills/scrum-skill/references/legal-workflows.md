# Optional legal and privacy workflow routing

Read only for selected legal/privacy work. The Scrum Master, software engineer,
UI/UX, QA, security, operations and AI presets do not require LegalQuants skills.
These are routing recommendations, not copied skills or bundled dependencies.
Resolve the installed host's actual skill name/path; read the selected SKILL.md
and follow its inputs, scope and approval requirements. If absent, report the gap
and use an evidence-first manual workflow or install only within user authorization.

## Legal Counsel - platform/design decisions

Start with the proposed behavior, users, applicable jurisdictions, factual evidence
and the decision needing advice. Identify relevant platform risks, compare safeguards
and give the PO/accountable counsel a source-backed recommendation. Record the design
revision, source, risk, options, decision owner and residual issue in a risk register/ADR.
Follow [dependency routing](dependency-routing.md) to resolve/load actual installed skills.

| Actual task | Candidate LQ workflow | Boundary |
| --- | --- | --- |
| Whether a proposed platform activity/design falls under a rule | [regulatory](https://github.com/LegalQuants/lq-plugin-oss/blob/main/skills/core/regulatory/SKILL.md) | Actual facts/jurisdiction and official instrument/version; unresolved judgment stays with counsel |
| Whether authority supports a platform-risk/design proposition | [proposition-checking](https://github.com/LegalQuants/lq-skills/blob/main/skills/proposition-checking/SKILL.md) | Source unavailable means unverified, not a legal conclusion from memory |
| What leaves a legal AI workspace and related privacy/confidentiality risk | [local-first-legal-workspace](https://github.com/LegalQuants/lq-skills/blob/main/skills/local-first-legal-workspace/SKILL.md) | Observe actual architecture/runtime; missing evidence yields a plan and unknowns |
| Provider processing terms for a design/vendor decision | [dpa-checklist-review](https://github.com/LegalQuants/lq-skills/blob/main/skills/dpa-checklist-review/SKILL.md) | Supplied agreement, identified supported regime and party roles; privacy counsel collaborates |
| Challenge a substantive counsel risk analysis | [adversarial-qc](https://github.com/LegalQuants/lq-skills/blob/main/skills/adversarial-qc/SKILL.md) | Only authorized agents/providers; disclose actual independence; no professional sign-off |

For citations used in the decision memo, Singapore-specific sgcite and
bart-statutory-reference-checker are candidates only when relevant. For actual
vendor/customer terms, approved playbook review or defined-term checking may help
that document review. Apply the installed skill's prerequisites; transaction and
litigation workflows are selected by the actual question, not automatically by role.
These are source skill names; installations may expose lq- aliases or plugin namespaces.

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
