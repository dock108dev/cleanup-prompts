# Repository maintenance

The intended GitHub configuration is:

- Public repository, MIT license, issues enabled, and private vulnerability reporting enabled.
- `main` requires pull requests and the `validate` check, with up-to-date branches and resolved review conversations. The active ruleset grants a named bypass only to the owner account `dock108dev`, allowing that account to push directly without waiting for validation. No general collaborator, administrator-role, or application bypass is configured.
- Validation still runs after pushes and on pull requests. Separate branch protection keeps force pushes and deletion disabled and requires linear history, including for the owner. Preserve the owner-only exception; do not broaden it to all maintainers or remove the requirements for other contributors.
- Squash merge is enabled; merge commits and rebase merge are disabled. Merged topic branches are deleted automatically.
- Actions use a read-only default token and cannot approve pull requests. External actions are restricted to `actions/checkout` and pinned to full commit SHAs. Checkout does not persist credentials. Fork pull requests use the ordinary unprivileged `pull_request` event; no secrets or publication steps are needed.
- Dependabot checks GitHub Actions weekly. Dependency alerts, security updates, secret scanning, and push protection remain enabled.

These settings live in GitHub, not in the clone. Review the live settings when maintainership or workflows change. Do not claim this document alone enforces protection.

Before pushing or merging, inspect the diff and run relevant local checks. Inspect validation for the actual pushed commit and address failures. After a workflow change, confirm the check on `main` too.

The validation suite checks prompt packaging and helper behavior. Agent performance needs realistic examples and, when warranted, disposable-project trials; do not present text validation as an end-to-end audit.
