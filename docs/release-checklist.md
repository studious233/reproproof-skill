# ReproProof Release Checklist

Use this before publishing a GitHub release.

## Repository hygiene

- [ ] `README.md` explains what the project is and is not.
- [ ] `LICENSE` is present.
- [ ] `CONTRIBUTING.md` is present.
- [ ] `SECURITY.md` is present.
- [ ] No local absolute paths are required for public installation.
- [ ] No secrets, private data, or proprietary research artifacts are included.

## Skill hygiene

- [ ] Every skill has `SKILL.md`.
- [ ] Every `SKILL.md` has YAML frontmatter with only `name` and `description`.
- [ ] Skill names match lowercase hyphen-case.
- [ ] `SKILL.md` files are concise enough to load into an agent context.
- [ ] Detailed checklists, templates, and examples live outside `SKILL.md`.

## ReproProof

- [ ] Evidence Boundary Ledger is documented.
- [ ] Bounded-audit discipline is preserved.
- [ ] Example audits distinguish missing material from unavailable material.
- [ ] The skill does not claim to run experiments or guarantee reproduction.

## Validation

```bash
python scripts/validate_skills.py
```

On Windows, `py scripts\validate_skills.py` is equivalent.

Fix all errors before tagging a release.
