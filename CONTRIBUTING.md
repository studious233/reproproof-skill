# Contributing

Contributions are welcome when they keep the project focused on the ReproProof reproducibility-audit skill.

## Scope

Good contributions include:

- Clearer skill instructions
- Smaller, sharper reference material
- Reproducibility audit examples
- Validation checks
- Documentation that helps another user install or evaluate the skill

Avoid broad feature creep such as generic academic writing, unrelated agent personas, multi-agent runtime protocols, or experiment-running pipelines.

## Skill guidelines

- Keep `SKILL.md` concise and procedural.
- Put detailed checklists, schemas, examples, and templates under `references/`, `templates/`, `docs/`, or `examples/`.
- Use clear trigger language in frontmatter `description`.
- Do not invent claims about runtime behavior that is not implemented.
- Prefer bounded examples over promotional language.

## Before opening a pull request

Run:

```bash
python scripts/validate_skills.py
```

Then check:

- New files are UTF-8 text.
- No secrets or local absolute paths are committed, except documented examples.
- ReproProof changes preserve bounded-audit discipline.

## Pull request format

Include:

- What changed
- Why it changed
- Which part of the skill is affected
- How it was validated
