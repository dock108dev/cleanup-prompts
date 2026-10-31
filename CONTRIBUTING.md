# Contributing

Bug reports, practical examples, and focused prompt improvements are welcome. Open an issue for a substantial change in scope or behavior before building it. Small fixes can go straight to a pull request.

## Make a change

1. Fork and clone the repository, then create a topic branch.
2. Keep the coordinator small. Put shared scope and stopping rules in `playbook.md`, domain guidance in the relevant prompt, and user-facing usage in `README.md`.
3. Preserve the distinction between audit and implementation, respect target-repository instructions, and avoid adding unbounded cleanup or implied external authorization.
4. Use repository-relative links and portable examples. Do not include personal paths, credentials, private customer data, or real sensitive reproduction material.
5. Run the checks below and describe the problem, resulting behavior, and verification in your pull request.

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

Python 3.10+ and Git are sufficient; no third-party packages are required. For a behavioral prompt change, describe a realistic request and what the agent should do, skip, and report. When practical, exercise it in a disposable fixture project and state the observed limits. Passing text validation alone does not prove prompt effectiveness.

## Review

The maintainer reviews scope, correctness, portability, and verification. Pull requests must pass the required validation check and resolve review conversations. Changes are squash-merged. Independent approval is not required while the project has one maintainer; revisit that policy when another maintainer joins.

Be respectful, explain disagreements with evidence, and keep discussion about the work. Harassment, personal attacks, and disclosure of private information are not welcome; maintainers may moderate such contributions.

By submitting a contribution, you agree that it is provided under this repository's [MIT License](LICENSE). Submit only material you have the right to share. For security-sensitive reports, use [security policy](.github/SECURITY.md) rather than a public issue.
