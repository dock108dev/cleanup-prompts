# Security policy

## Supported version

Security fixes target the current `main` branch. Older commits and local copies are not maintained separately. Review changes before updating an installed skill.

## Report a vulnerability privately

Use [GitHub private vulnerability reporting](https://github.com/dock108dev/cleanup-prompts/security/advisories/new) for unsafe instructions, permission-boundary failures, exploitable workflow behavior, or accidental exposure of sensitive information.

Include the affected commit, a minimal reproduction with synthetic data, the expected boundary, and the observed impact. Do not include credentials, private repository contents, or customer data. Avoid public issues or pull requests containing an unremediated exploit or secret.

The maintainer will assess reports as availability permits; this volunteer project has no guaranteed response time. Ordinary quality issues can use the public issue tracker.

## Execution boundary

This repository contains instructions and local validation helpers. The agent, its tools, and the target environment control actual permissions. Read prompts before use, preserve backups or version control for important work, and validate command targets before execution. Tests passing here do not establish that an agent's actions in another repository are secure.
