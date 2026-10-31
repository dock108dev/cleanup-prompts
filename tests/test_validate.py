"""Exercise packaging failures without changing the working repository."""

from pathlib import Path
import tempfile
import unittest

from scripts.validate import REQUIRED, validate


class BundleValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for name in REQUIRED:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("Example document.\n")
        (self.root / "SKILL.md").write_text(
            "---\nname: cleanup-harness\ndescription: A fixture skill.\n---\n"
            "Read [the coordinator](harness.md).\n"
        )

    def write_readme(self, text):
        (self.root / "README.md").write_text(text)
        return validate(self.root)

    def test_valid_portable_bundle(self):
        self.assertEqual(validate(self.root), [])

    def test_missing_required_file(self):
        (self.root / "harness.md").unlink()
        errors = validate(self.root)
        self.assertTrue(any("Missing required file: harness.md" in e for e in errors))
        self.assertTrue(any("broken local link" in e for e in errors))

    def test_broken_reference_link(self):
        errors = self.write_readme("See [guide][guide].\n\n[guide]: missing.md\n")
        self.assertTrue(any("broken local link" in e for e in errors))

    def test_link_cannot_depend_on_sibling_checkout(self):
        errors = self.write_readme("[Other project](../other/README.md)\n")
        self.assertTrue(any("link leaves the bundle" in e for e in errors))

    def test_nested_policy_links_resolve_from_document(self):
        (self.root / ".github/SECURITY.md").write_text("[Home](../README.md)\n")
        self.assertEqual(validate(self.root), [])

    def test_home_paths_rejected_even_in_code_examples(self):
        errors = self.write_readme("```sh\ncat /Users/example/private/file\n```\n")
        self.assertTrue(any("machine-specific home path" in e for e in errors))

    def test_external_links_and_fenced_examples_are_not_fetched(self):
        errors = self.write_readme(
            "[Web](https://example.invalid/guide)\n"
            "```markdown\n[Example](missing.md)\n```\n"
        )
        self.assertEqual(errors, [])

    def test_conflicts_and_whitespace_fail(self):
        errors = self.write_readme("<<<<<<< HEAD\nUnfinished  \n=======\n")
        self.assertTrue(any("merge-conflict marker" in e for e in errors))
        self.assertTrue(any("trailing whitespace" in e for e in errors))

    def test_invalid_skill_metadata_fails(self):
        (self.root / "SKILL.md").write_text("---\nname: wrong\n---\n")
        errors = validate(self.root)
        self.assertTrue(any("expected name" in e for e in errors))
        self.assertTrue(any("missing description" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
