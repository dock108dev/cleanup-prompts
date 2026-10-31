# Cleanup prompts

Reusable prompts for implementing focused repository maintenance. Start with the [cleanup harness](harness.md), which follows the [playbook](playbook.md) to inspect the target repository and select the applicable prompts. Individual prompts can still be used directly.

Use “Run the cleanup harness for this repo” or “Run the relevant cleanup prompts.” The default covers local changes and affected code. You can also request branch cleanup, broader repository cleanup, a full audit without edits, or a full audit with fixes. The playbook defines scope, routing, verification, and when to stop.

The shared repo owns the reusable process; each target repo supplies its instructions, product constraints, and verification commands.

- [Documentation cleanup](docs.md): concise current documentation and comments, small repository fixes, and cleanup of unnecessary tracked working material.
- [Repository cleanup](cleanup.md): code structure, stack-specific file-size review and extraction, documentation, current Git ignore rules, and removal of unnecessary tracked artifacts while preserving local copies.
- [Product UI and UX review](ui-ux-cleanup.md): professional visual design, approachable interactions, task-first layouts, concise text, and deliberate spacing.
- [Backend and database review](backend-db-cleanup.md): end-of-sprint maintenance for data integrity, transactions, jobs, migrations, query performance, backend contracts, and operational recovery.
- [Error handling](abend.md): failure diagnosis, recovery, and operational clarity.
- [Security](security.md): repository security review and supported fixes.
- [Sources of truth](ssot.md): shared ownership and removal of duplicated policy.
- [CI readiness](ci.md): event-driven workflows, comprehensive project checks, security and reliability, run summaries, quality metrics, and suitable free integrations.
- [Next Steps reconciliation](next_steps.md): reconcile an identified planning document with completed work and the remaining project goal.

These are Markdown instructions, with no application build or runtime. Review changes for consistency and run `git diff --check`.

For UI work, follow the target repository’s current design requirements. When available, consult the shared [UI Templates requirements](../ui-templates/DESIGN_REQUIREMENTS.md) and relevant examples; the gallery is a reference, not a setup or runtime prerequisite. Preserve domain behavior and distinguish technical verification from owner acceptance.
