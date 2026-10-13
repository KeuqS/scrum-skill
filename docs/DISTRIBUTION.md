# Release and directory submission

## Artifact identity

`scrum-skill` is a skills-only plugin containing two separately invocable skills:
`scrum-skill` (coordination) and `scrum-dashboard` (local metrics UI). The root
`.codex-plugin/plugin.json` packages both. Individual skill folders can also be installed.
There is no MCP server, hook or automatic external dependency installer.

## Community Codex Marketplace

At https://www.codex-marketplace.com/submit choose **Plugin**, sign in with GitHub,
and enter `https://github.com/kevanwee/scrum-skill/tree/v0.5.1` as the GitHub target.
Review scanner findings and track the queued submission. Use the root rather than
`skills/scrum-skill`, which would submit only one skill. This directory explicitly
states it is not affiliated with OpenAI. Submission is not approval.

Suggested description: Scrum planning, evidence, AI teammate coordination and an
offline Sprint dashboard for Codex and Claude Code.

For separate standalone entries, use Skill and the respective tree URL ending
`/skills/scrum-skill` or `/skills/scrum-dashboard`. Start with the plugin listing to
avoid confusing users with duplicate installations.

Source: https://www.codex-marketplace.com/docs

## Official OpenAI directory

This is a separate application. OpenAI currently documents a complete ZIP upload,
verified publishing identity, automated checks, review and an explicit publish step
after approval. The release ZIP includes portable/root and host manifests, skills,
assets and docs, without local project records. Confirm the actual dashboard's
requirements before attesting to anything. No official listing or approval is claimed.

Sources: https://developers.openai.com/plugins/deploy/submission
and https://developers.openai.com/plugins/build/plugins

## Other visibility routes

1. Anthropic's official directory: follow the submission link in
   https://github.com/anthropics/claude-plugins-official or
   https://claude.com/docs/directory/publish. Approval is independent of other directories.
2. Vercel's skills.sh: make genuine skill installation easy with
   `npx skills add kevanwee/scrum-skill`. This installs skills, not the plugin.
   Rankings use aggregated CLI installs; do not simulate popularity.
   Documentation: https://skills.sh/docs
3. Show HN: share the runnable project and local demo, explain your work and lessons,
   and be available for questions. Review https://news.ycombinator.com/showhn.html.
4. Publish a practical walkthrough on your own professional channels: a real
   setup-to-review example, short screen recording and frank limitations are more
   useful than generic launch claims. No external posts were sent by this release task.

The prepared social image still needs uploading in GitHub Settings > Social preview.
