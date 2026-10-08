# Cleanup prompts

Reusable prompts for implementing focused repository maintenance. Choose a prompt, apply it to the target repository, and follow its scope and validation requirements.

- [Documentation cleanup](docs.md): accurate current-behavior docs and comments, with planning history kept in designated records.
- [Repository cleanup](cleanup.md): code structure, readability, documentation, current Git ignore rules, and removal of unnecessary tracked artifacts while preserving local copies.
- [Product UI and UX review](ui-ux-cleanup.md): professional visual design, approachable interactions, task-first layouts, concise text, and deliberate spacing.
- [Error handling](abend.md): failure diagnosis, recovery, and operational clarity.
- [Security](security.md): repository security review and supported fixes.
- [Sources of truth](ssot.md): shared ownership and removal of duplicated policy.
- [CI readiness](ci.md): event-driven workflows, comprehensive project checks, security and reliability, run summaries, quality metrics, and suitable free integrations.

These are Markdown instructions, with no application build or runtime. Review changes for consistency and run `git diff --check`.

For UI work, follow the target repository’s current design requirements. When available, consult the shared [UI Templates requirements](../ui-templates/DESIGN_REQUIREMENTS.md) and relevant examples; the gallery is a reference, not a setup or runtime prerequisite. Preserve domain behavior and distinguish technical verification from owner acceptance.
