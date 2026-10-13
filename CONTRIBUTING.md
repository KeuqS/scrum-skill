# Contributing

Start with a [good first issue](https://github.com/kevanwee/scrum-skill/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22good%20first%20issue%22)
or propose an invented, reproducible workflow improvement. Useful contributions include
host-specific setup evidence, non-software examples, accessible docs and routing edge cases.
Discuss larger changes in an issue first; keep PRs focused and state what was actually tested.

Propose small behavior-backed changes. Keep one canonical skill and compatible host
manifests. Test with invented inputs in an isolated workspace; never upload project
plans, original reference PDFs or actual stakeholder data as a reproduction.

Run:

```text
python scripts/validate_package.py
python -m unittest discover -s tests -v
```

For Mermaid changes, extract README fences and render with the pinned development
CLI; retain evidence, not screenshots or node_modules in commits. A metadata validator
cannot prove runtime invocation or Scrum facilitation behavior. State evaluation scope.

Scrum Master or QA reviews/merges after required checks. Human/project acceptance and
production release remain separate. Update version for published behavior/packaging
changes, and add a sanitized regression for a demonstrated failure. Never auto-sync a
consumer project's private instructions or overwrite its configured quality criteria.
