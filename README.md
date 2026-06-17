# ReproProof Skill

ReproProof is a lightweight agent skill for auditing research claims, evidence boundaries, and reproducibility readiness before paper submission, thesis defense, benchmark release, or artifact publication.

It helps answer one practical question:

```text
Are the claims in this research artifact actually supported by the reviewed evidence, and is the reproduction path clear enough for another researcher to inspect?
```

ReproProof is intentionally narrow. It does not write papers, simulate peer review, run experiments, or guarantee reproducibility. It produces a bounded audit based only on the materials provided.

## What it checks

- Claim-evidence alignment
- Unsupported or overstated scientific claims
- Missing reproduction details
- Experimental protocol clarity
- Figure, table, caption, text, README, code, and config consistency
- Artifact evaluation and code release readiness

The core output is an **Evidence Boundary Ledger**: a claim-by-claim record of what the reviewed materials support, partially support, overstate, fail to support, contradict, or leave not assessable.

## Repository layout

```text
.
|-- .cursor/
|   `-- skills/
|       `-- reproproof/
|           |-- SKILL.md
|           |-- README.md
|           |-- references/
|           |   |-- audit-scope-routing.md
|           |   `-- reproducibility-checklist.md
|           `-- templates/
|               `-- audit-report.md
|-- docs/
|   |-- comparison.md
|   `-- release-checklist.md
|-- examples/
|   `-- reproproof/
|       |-- artifact-package-audit.md
|       `-- paper-only-audit.md
|-- scripts/
|   `-- validate_skills.py
|-- CONTRIBUTING.md
|-- LICENSE
|-- SECURITY.md
`-- README.md
```

## Install

### Project-level Cursor install

Copy or keep the `.cursor` directory at the root of a project:

```text
your-project/
`-- .cursor/
    `-- skills/
        `-- reproproof/
```

### Personal install

Copy the skill folder into your personal Cursor skills directory:

```text
~/.cursor/skills/reproproof/
```

## Example prompts

```text
Use ReproProof to audit this paper draft for reproducibility readiness.
```

```text
Check whether the benchmark claims in this report are supported by the tables, logs, and README.
```

```text
Review this repository and paper as an artifact evaluation package.
```

## Output modes

Quick audits include:

1. Overall readiness
2. Top risks
3. Claim-evidence gaps
4. Missing reproduction details
5. Immediate fixes

Full audits follow `.cursor/skills/reproproof/templates/audit-report.md` and include:

- Executive summary
- Audit boundary
- Evidence Boundary Ledger
- Severity-ranked findings
- Reproducibility checklist
- Consistency checks
- Safer wording suggestions for overclaims
- Release readiness actions

See [examples/reproproof](examples/reproproof) for sample outputs.

## Comparable projects

ReproProof is adjacent to larger academic-agent and reproducibility projects such as:

- [sistm/AI4Reproducibility](https://github.com/sistm/AI4Reproducibility)
- [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills)
- Academic research skill collections and artifact-evaluation templates

ReproProof's contribution is narrower: it is a final readiness pass that keeps claims tied to reviewed evidence and separates unavailable material from actual defects.

## Validate

Run the lightweight validation script:

```bash
python scripts/validate_skills.py
```

On Windows, if `python` resolves to the Microsoft Store launcher, use:

```powershell
py scripts\validate_skills.py
```

## License

MIT License. See [LICENSE](LICENSE).
