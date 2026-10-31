# Cleanup harness

Use this coordinator when asked to “run the cleanup harness for this repo” or “run the relevant cleanup prompts.” The target is the user's current or named project, not the shared cleanup-prompts repository merely because this file lives here.

1. Read [the playbook](playbook.md) and the shared [prompt catalog](README.md).
2. Read the target's applicable repository instructions, requirements, and verification commands. Inspect its current Git state and relevant implementation before choosing work.
3. Establish the requested scope and whether this is cleanup or audit-only. Give a brief scope and routing update, including why prompts apply or are skipped. Proceed with routine decisions.
4. Read each selected prompt in full and apply its relevant sections within the established scope. Combine overlapping work and checks; selecting a prompt does not automatically authorize every task it describes.
5. Verify the resulting changes with the target's required and relevant checks. Review the final diff against the starting state and preserve unrelated work.
6. Report scope, routing, changes or findings, actual verification, unresolved items, and the completion status defined in the playbook.

The shared repository owns the process. The target owns its product rules, architecture, commands, and acceptance criteria. Do not copy the shared prompts into every target or invent a parallel set of project rules.
