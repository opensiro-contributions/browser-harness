"""Native proof for domain-skill auto-discovery without an LLM or browser daemon."""
import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest

from browser_harness import domain_skills
from browser_harness import run


def _site_skill(root: Path, site: str = "github", filename: str = "repo-actions.md", text: str = "# Repo actions\nUse a known workflow.\n") -> Path:
    file = root / site / filename
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(text, encoding="utf-8")
    return file


def _indexed(root: Path) -> dict[str, str]:
    """Hermes-style entrypoint requirement: SKILL.md with name/description frontmatter."""
    result = {}
    for file in root.rglob("SKILL.md"):
        text = file.read_text(encoding="utf-8")
        assert text.startswith("---\nname: ")
        assert "\ndescription: \"" in text.split("---", 2)[1]
        name = text.splitlines()[1].split(": ", 1)[1]
        result[name] = text
    return result


def test_export_makes_invisible_domain_repertoire_indexable(tmp_path):
    source, output = tmp_path / "domain-skills", tmp_path / "external-skills"
    original = _site_skill(source)
    _site_skill(source, "linkedin", "invitation-manager.md", "# LinkedIn invitations\nManage pending invites.\n")
    assert _indexed(source) == {}  # pinned original: *.md, not SKILL.md
    stats = domain_skills.export_domain_skills(source, output)
    assert stats == {"exported": 2, "unchanged": 0, "total": 2}
    exported = _indexed(output)
    assert sorted(exported) == [
        "browser-harness-github-repo-actions",
        "browser-harness-linkedin-invitation-manager",
    ]
    assert original.read_text() in exported["browser-harness-github-repo-actions"]
    assert original.read_text() == "# Repo actions\nUse a known workflow.\n"
    assert not list(source.rglob("SKILL.md"))
    assert domain_skills.export_domain_skills(source, output) == {
        "exported": 0, "unchanged": 2, "total": 2,
    }


def test_modified_source_requires_explicit_update_of_managed_export(tmp_path):
    source, output = tmp_path / "source", tmp_path / "out"
    file = _site_skill(source)
    domain_skills.export_domain_skills(source, output)
    target = output / "browser-harness-github-repo-actions" / "SKILL.md"
    old = target.read_text()
    file.write_text("# Corrected workflow\n")
    with pytest.raises(domain_skills.ExportError, match="Refusing to overwrite"):
        domain_skills.export_domain_skills(source, output)
    assert target.read_text() == old
    assert domain_skills.export_domain_skills(source, output, update_managed=True)["exported"] == 1
    assert "# Corrected workflow" in target.read_text()


def test_do_not_overwrite_user_edited_managed_export_even_with_update(tmp_path):
    source, output = tmp_path / "source", tmp_path / "out"
    file = _site_skill(source)
    domain_skills.export_domain_skills(source, output)
    target = output / "browser-harness-github-repo-actions" / "SKILL.md"
    target.write_text(target.read_text() + "\nuser edit\n")
    file.write_text("# New generation\n")
    with pytest.raises(domain_skills.ExportError, match="Refusing to overwrite"):
        domain_skills.export_domain_skills(source, output, update_managed=True)
    assert target.read_text().endswith("user edit\n")


def test_preflight_conflict_prevents_partial_writes(tmp_path):
    source, output = tmp_path / "source", tmp_path / "out"
    _site_skill(source, "aaa", "first.md")
    _site_skill(source, "zzz", "last.md")
    conflict = output / "browser-harness-zzz-last" / "SKILL.md"
    conflict.parent.mkdir(parents=True)
    conflict.write_text("# hand-written by user\n")
    with pytest.raises(domain_skills.ExportError, match="unmanaged"):
        domain_skills.export_domain_skills(source, output)
    assert conflict.read_text() == "# hand-written by user\n"
    assert not (output / "browser-harness-aaa-first").exists()


def test_collision_rejected_before_any_write(tmp_path):
    source, output = tmp_path / "source", tmp_path / "out"
    _site_skill(source, "GitHub", "foo.md")
    _site_skill(source, "github", "foo.md")
    with pytest.raises(domain_skills.ExportError, match="Colliding"):
        domain_skills.export_domain_skills(source, output)
    assert not output.exists()


def test_refuses_symlinked_source_or_destination(tmp_path):
    source, output = tmp_path / "source", tmp_path / "out"
    _site_skill(source)
    source_file = source / "github" / "repo-actions.md"
    linked = source / "github" / "link.md"
    try:
        linked.symlink_to(source_file)
    except OSError:
        pytest.skip("symlink unavailable")
    with pytest.raises(domain_skills.ExportError, match="symbolic source"):
        domain_skills.export_domain_skills(source, output)
    linked.unlink()
    target_dir = output / "browser-harness-github-repo-actions"
    target_dir.parent.mkdir(parents=True)
    target_dir.symlink_to(tmp_path / "elsewhere", target_is_directory=True)
    with pytest.raises(domain_skills.ExportError, match="symbolic destination"):
        domain_skills.export_domain_skills(source, output)
    assert not (tmp_path / "elsewhere").exists()


def test_empty_source_and_output_inside_source_fail_closed(tmp_path):
    source, output = tmp_path / "source", tmp_path / "out"
    source.mkdir()
    with pytest.raises(domain_skills.ExportError, match="No domain-skill"):
        domain_skills.export_domain_skills(source, output)
    _site_skill(source)
    with pytest.raises(domain_skills.ExportError, match="outside"):
        domain_skills.export_domain_skills(source, source / "exported")


def test_cli_export_never_starts_browser_daemon(tmp_path, monkeypatch):
    source, output = tmp_path / "agent-workspace", tmp_path / "external"
    _site_skill(source / "domain-skills")
    monkeypatch.setenv("BH_AGENT_WORKSPACE", str(source))
    with patch.object(sys, "argv", ["browser-harness", "domain-skills", "export", "--output", str(output)]), \
         patch("browser_harness.run.ensure_daemon") as daemon, \
         patch("browser_harness.run.print_update_banner"), \
         patch("sys.stdout", new_callable=StringIO) as stream:
        with pytest.raises(SystemExit) as exit_info:
            run.main()
    assert exit_info.value.code == 0
    daemon.assert_not_called()
    assert "exported=1" in stream.getvalue()
    assert "browser-harness-github-repo-actions" in _indexed(output)
