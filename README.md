# Cleanup prompts

[![Validate](https://github.com/dock108dev/cleanup-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/dock108dev/cleanup-prompts/actions/workflows/validate.yml)

A reusable cleanup harness for coding agents. One entry point inspects a project's current state, selects relevant maintenance prompts, makes scoped repairs, verifies them, and stops when the agreed work is complete.

The shared process lives here. Your target repository supplies its own instructions, product constraints, and verification commands. These are Markdown instructions, not an autonomous service or a guarantee that an agent will find every defect.

## Quick start with any coding agent

Clone this repository somewhere outside the project you want to clean up:

```sh
git clone https://github.com/dock108dev/cleanup-prompts.git
```

In your target project's chat, give the agent the actual path to this clone:

> Read harness.md in my cleanup-prompts clone at PATH_TO_CLONE, then run the cleanup harness for this target repository.

Start with [the coordinator](harness.md); it follows [the playbook](playbook.md) and loads only the applicable prompts. An agent needs access to both repositories. For agents without local file access, provide the coordinator, playbook, and relevant prompt contents along with the target's files and instructions.

## Install as a Codex skill

On macOS or Linux, clone once and link the whole repository into your personal skills directory:

```sh
mkdir -p "$HOME/.local/share" "$HOME/.agents/skills"
git clone https://github.com/dock108dev/cleanup-prompts.git "$HOME/.local/share/cleanup-prompts"
ln -s "$HOME/.local/share/cleanup-prompts" "$HOME/.agents/skills/cleanup-harness"
```

If you already have a clone, link its absolute path instead. Do not overwrite an existing skill directory. On Windows, or where symlinks are unavailable, copy the entire clone into your personal `.agents/skills/cleanup-harness` directory; keep the supporting Markdown files beside `SKILL.md`.

Start a new chat in the target project and say **“Run the cleanup harness for this repo”**, or explicitly invoke **`$cleanup-harness`**. If the skill is not listed, reopen the agent session or use the explicit coordinator path above. See [Codex skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

To update a linked installation, review upstream changes and run `git pull --ff-only` in its clone. Copied installations need to be refreshed manually. The installed clone determines which version runs; check out a reviewed commit to keep a fixed version. No background updates or external service accounts are required.

## Choose the scope

| Say | Result |
| --- | --- |
| “Run the relevant cleanup prompts” | Clean up staged, unstaged, and relevant untracked changes, plus affected code |
| “Run cleanup for this branch against BASE” | Review the branch diff and affected behavior, then make supported repairs |
| “Run cleanup for the backend” | Limit implementation and checks to that subsystem and its affected contracts |
| “Run broader cleanup across this repo” | Consider all applicable maintenance areas across the repository |
| “Run a full audit, no edits” | Review the repository and report findings without changing source or configuration |
| “Run a full audit and fix the findings” | Review broadly and implement supported in-scope repairs |

A clean working tree triggers bounded triage by default, not an unsolicited whole-project rewrite. Audit breadth and permission to edit are separate. Every pass reports selected/skipped prompts, actual verification, and unresolved gaps. See the [playbook's completion rules](playbook.md).

## Prompt catalog

- [Repository cleanup](cleanup.md): structure, readability, file-size review, ignores, and tracked artifacts.
- [Documentation](docs.md): current documentation, comments, links, and documented workflows.
- [UI and UX](ui-ux-cleanup.md): visual design, interactions, accessibility, layouts, and concise copy.
- [Backend and database](backend-db-cleanup.md): integrity, transactions, jobs, migrations, contracts, and recovery.
- [Error handling](abend.md): failure diagnosis, retries, cancellation, and operational clarity.
- [Security](security.md): trust boundaries, dependencies, secrets, and supported repairs.
- [Sources of truth](ssot.md): shared ownership and duplicated policy.
- [CI readiness](ci.md): workflows, checks, security, reproducibility, and reporting.
- [Next Steps reconciliation](next_steps.md): reconcile an identified planning document with completed and remaining work.

You can use these prompts individually. UI work follows the target project's design requirements and any design references that project supplies; no companion template repository is required.

## Boundaries

The harness preserves existing work and product intent. It does not grant permission to commit, push, deploy, modify production data, spend money, or replace installed builds. Authorization already given in the session still applies. Inspect commands and diffs before approving consequential actions; prompts cannot enforce permissions independently of the agent that runs them.

The agent should stop after completing and verifying the defined scope, or report a specific blocker. A passing local check is not hosted CI, owner acceptance, or release approval.

## Contribute and validate

Read [CONTRIBUTING.md](CONTRIBUTING.md). With Python 3.10+ and Git:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

CI checks local Markdown links, portable paths, skill metadata, text hygiene, and the validator's behavior. It does not evaluate an agent's actual cleanup quality or the availability of external websites.

Report ordinary bugs through [GitHub issues](https://github.com/dock108dev/cleanup-prompts/issues). Report security issues privately as described in [security policy](.github/SECURITY.md). Repository protection policy is documented in [the maintainer guide](.github/MAINTAINERS.md).

Licensed under the [MIT License](LICENSE).
