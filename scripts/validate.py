"""Validate this prompt bundle with Python's standard library only."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "SKILL.md", "LICENSE", "CONTRIBUTING.md",
    ".github/SECURITY.md", "harness.md", "playbook.md",
    "cleanup.md", "docs.md", "ui-ux-cleanup.md", "backend-db-cleanup.md",
    "abend.md", "security.md", "ssot.md", "ci.md", "next_steps.md",
)
LINK = re.compile(r"\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
REFERENCE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
PERSONAL_PATH = re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/|[A-Z]:\\Users\\", re.I)


def markdown_prose(text):
    """Exclude fenced examples from link validation."""
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def validate(root):
    root = Path(root).resolve()
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")

    # Only repository-owned text, not a user's virtualenv or checkout metadata.
    paths = list(root.glob("*.md")) + list((root / ".github").rglob("*.md"))
    paths += list((root / ".github").rglob("*.yml"))
    paths += list((root / "scripts").glob("*.py"))
    paths += list((root / "tests").glob("*.py"))
    paths += [root / "LICENSE", root / ".github/CODEOWNERS", root / ".gitignore"]
    for path in sorted(set(paths)):
        if not path.is_file():
            continue
        name = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            errors.append(f"{name}: missing final newline")
        for number, line in enumerate(text.splitlines(), 1):
            if line != line.rstrip():
                errors.append(f"{name}:{number}: trailing whitespace")
            if re.match(r"^(?:<{7}|={7}|>{7})(?:\s|$)", line):
                errors.append(f"{name}:{number}: merge-conflict marker")
        if path.suffix != ".md":
            continue
        if PERSONAL_PATH.search(text):
            errors.append(f"{name}: machine-specific home path")
        prose = markdown_prose(text)
        for raw in LINK.findall(prose) + REFERENCE.findall(prose):
            link = urlsplit(raw.strip("<>"))
            if link.scheme or link.netloc or not link.path:
                continue
            target = (path.parent / unquote(link.path)).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{name}: link leaves the bundle: {raw}")
            elif not target.exists():
                errors.append(f"{name}: broken local link: {raw}")

    skill = root / "SKILL.md"
    if skill.is_file():
        match = re.match(r"\A---\n(.*?)\n---\n", skill.read_text(), re.S)
        if not match:
            errors.append("SKILL.md: missing frontmatter")
        else:
            fields = dict(re.findall(r"^([a-z-]+): (.+)$", match.group(1), re.M))
            if fields.get("name") != "cleanup-harness":
                errors.append("SKILL.md: expected name cleanup-harness")
            if not fields.get("description", "").strip():
                errors.append("SKILL.md: missing description")
    return errors


if __name__ == "__main__":
    problems = validate(ROOT)
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        sys.exit(1)
    print("Prompt bundle validation passed.")
