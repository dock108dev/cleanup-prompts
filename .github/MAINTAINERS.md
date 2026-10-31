# Repository maintenance

The intended GitHub configuration is:

- Public repository, MIT license, issues enabled, and private vulnerability reporting enabled.
- `main` requires a pull request, the `validate` GitHub Actions check, an up-to-date branch, and resolved review conversations. Administrators are subject to the same rules. Force pushes and deletion are disabled; history is linear.
- No independent approval is required while there is one maintainer. Add an approval requirement when a second reviewer can maintain it; do not disable required checks as a workaround.
- Squash merge is enabled; merge commits and rebase merge are disabled. Merged topic branches are deleted automatically.
- Actions use a read-only default token and cannot approve pull requests. External actions are restricted to `actions/checkout` and pinned to full commit SHAs. Checkout does not persist credentials. Fork pull requests use the ordinary unprivileged `pull_request` event; no secrets or publication steps are needed.
- Dependabot checks GitHub Actions weekly. Dependency alerts, security updates, secret scanning, and push protection remain enabled.

These settings live in GitHub, not in the clone. Review the live settings when maintainership or workflows change. Keep the required check name stable, or update branch protection together with the workflow. Do not claim this document alone enforces protection.

Before merging, inspect the diff and required checks for the actual PR head. Do not use an administrator bypass to skip a failing check. After merging a workflow change, confirm the check on `main` too.

The validation suite checks prompt packaging and helper behavior. Agent performance needs realistic examples and, when warranted, disposable-project trials; do not present text validation as an end-to-end audit.
