---
name: cleanup-harness
description: Run a shared cleanup harness for a target repository. Use for requests to run relevant cleanup prompts, scoped or broader repository cleanup, or a full cleanup audit using the shared process.
---

# Cleanup harness

Read [harness.md](harness.md) beside this file and follow its linked playbook and prompt catalog. Resolve these files relative to this skill's installed directory, following a directory symlink to the shared clone when present. Load selected prompts at execution time rather than copying their instructions into the target repository.

Use the user's current or named repository as the target. The skill's own repository is not the target unless explicitly requested. Preserve the requested breadth and audit-only versus implementation mode. If supporting files are missing, report the incomplete installation and ask for the shared clone's location; do not silently substitute a generic cleanup workflow.
