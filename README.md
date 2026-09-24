# Cleanup prompts

Reusable prompts for implementing focused repository maintenance. Choose a prompt, apply it to the target repository, and follow its scope and validation requirements.

- [Documentation cleanup](docs.md): accurate current-behavior docs and comments, with planning history kept in designated records.
- [Repository cleanup](cleanup.md): code structure, readability, maintainability, and documentation.
- [Product clarity cleanup](ui-ux-cleanup.md): concise interface text, useful layouts, and clear actions.
- [Error handling](abend.md): failure diagnosis, recovery, and operational clarity.
- [Security](security.md): repository security review and supported fixes.
- [Sources of truth](ssot.md): shared ownership and removal of duplicated policy.
- [CI readiness](ci.md): repository checks and continuous-integration readiness.

These are Markdown instructions, with no application build or runtime. Review changes for consistency and run `git diff --check`.

For UI work, use the target repository’s local design requirements and runtime styles. The original shared Desktop UI Templates gallery is unavailable in this workspace; do not make it a setup or runtime prerequisite. Preserve domain behavior and distinguish technical verification from owner acceptance.
