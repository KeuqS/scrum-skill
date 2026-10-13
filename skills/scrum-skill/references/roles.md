# Accountabilities and adaptable profiles

Scrum has Product Owner, Scrum Master and Developers accountabilities. Specialisms
are not additional Scrum accountabilities or sub-team hierarchies. AI execution aids
the accountable human; this package does not create autonomous human responsibility.

Read [accountability behavior](accountabilities.md) for the three accountabilities.
The whole Scrum Team is self-managing; the Scrum Master serves it, and the PO orders
value/outcomes while Developers decide how work gets done.

| Accountability | Decisions and work | AI assistance |
| --- | --- | --- |
| Product Owner | Product Goal, value, backlog order and stakeholder tradeoffs | Draft/refine options; never invent the person's agreement |
| Scrum Master | Team effectiveness, facilitation, coaching and impediment removal | Maintain inspection evidence and coordinate bounded workers |
| Developers | Plan, size, build, verify and adapt the Sprint Backlog | Collaborate through shared quality criteria and small integrated slices |

Start with the smallest useful team. Software projects often use engineering and QA;
add design, security, operations, data/AI or a domain reviewer when relevant. A legal
project may need counsel; a game or research project may need different expertise.
The Product Owner does not have to be a lawyer. Do not install third-party skills,
select a paid model or create accounts merely because a profile mentions a tool.

## Profile contract

For each specialist record: contribution, owned scope, dependencies, acceptance
criteria, evidence/review expectations, handoff path and collaboration boundaries.
Responsibilities may overlap; avoid conflicting writes and unclear integration owners.
The coordinator facilitates scope negotiation rather than assigning an inflexible plan.

- Engineering: just-enough architecture, implementation, contracts, integration and
  meaningful tests; composition/interface polymorphism where it improves replaceability.
- QA: independently derive critical negative/boundary cases, inspect test oracles,
  maintain evidence/traceability and verify CI/release claims.
- Design: user flows, hierarchy, accessibility, responsive behavior and honest product
  claims; follow the project's chosen design system and tools.
- Security: threat/data-flow review proportional to actual boundaries, controls and
  findings with owners; distinguish source-sharing risk from production-release risk.
- Domain reviewer: project-specific substantive judgments and evidence; do not claim
  regulated human sign-off from an agent review.

Use the optional template in assets/role-profile.md for custom specialisms.

## Selectable presets

| Helper slug | Behavior guide copied into the project |
| --- | --- |
| engineering | [Architecture, implementation and integration](../assets/profiles/engineering.md) |
| qa | [Risk-based verification and CI evidence](../assets/profiles/qa.md) |
| design | [User flows, accessibility and interaction](../assets/profiles/design.md) |
| security | [Threats, data boundaries and controls](../assets/profiles/security.md) |
| ai | [Model/data pipeline and evaluation](../assets/profiles/ai.md) |
| operations | [Delivery, reliability and recovery](../assets/profiles/operations.md) |
| domain-reviewer | [Domain evidence and decision limits](../assets/profiles/domain-reviewer.md) |
| legal-counsel | [Optional legal review and LQ workflow routing](../assets/profiles/legal-counsel.md) |
| privacy-counsel | [Optional PDPA/GDPR assessment](../assets/profiles/privacy-counsel.md) |

The helper uses an exact slug match; custom slugs get the generic profile template.
Tailor the copied profile with owned scope, criteria, dependencies and the current
handoff path before work. Presets do not activate agents or install named tools.
Existing project profiles are preserved; upgrading the skill does not rewrite them.

Core software preset: Scrum Master assistance plus engineering, design, QA and security
contributions; the user remains the Product Owner. These do not require legal or LQ
skills. Add legal-counsel and/or privacy-counsel only when the project needs them;
read [legal workflow routing](legal-workflows.md) only for those tasks. AI and operations
are optional extensions, not a requirement to increase team size.
