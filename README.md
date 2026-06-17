# ReproProof Skill

[![Validate](https://github.com/studious233/reproproof-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/studious233/reproproof-skill/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/studious233/reproproof-skill)](https://github.com/studious233/reproproof-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

ReproProof is a lightweight, portable agent skill for auditing research claims, evidence boundaries, and reproducibility readiness before paper submission, thesis defense, benchmark release, or artifact publication.

It helps researchers catch unsupported claims, missing experiment details, and reproducibility gaps before their paper or code goes public.

It helps answer one practical question:

```text
Are the claims in this research artifact actually supported by the reviewed evidence, and is the reproduction path clear enough for another researcher to inspect?
```

ReproProof is intentionally narrow. It does not write papers, simulate peer review, run experiments, or guarantee reproducibility. It produces a bounded audit based only on the materials provided.

## Quick start

Copy `reproproof/` into your agent skill directory, then ask your agent:

```text
Use ReproProof to audit this paper draft. Identify unsupported claims, missing reproduction details, and figure/table inconsistencies.
```

For a repository plus paper:

```text
Use ReproProof to review this paper, README, configs, and result files as an artifact evaluation package.
```

## Sample output

ReproProof's main artifact is an Evidence Boundary Ledger:

| ID | Claim | Evidence found | Assessment | Risk |
|---|---|---|---|---|
| C1 | "Our method improves accuracy across all benchmark tasks." | Table 1 reports higher mean scores on four tasks. | Partially supported | High |
| C2 | "The method is computationally efficient." | No runtime, memory, or hardware comparison is provided. | Unsupported | High |
| C3 | "The ablation confirms the routing module is necessary." | Ablation table removes the routing module but reports one run only. | Partially supported | Medium |

See complete examples:

- [Paper-only audit](examples/reproproof/paper-only-audit.md)
- [Artifact-package audit](examples/reproproof/artifact-package-audit.md)

## What it checks

- Claim-evidence alignment
- Unsupported or overstated scientific claims
- Missing reproduction details
- Experimental protocol clarity
- Figure, table, caption, text, README, code, and config consistency
- Artifact evaluation and code release readiness

The core output is an **Evidence Boundary Ledger**: a claim-by-claim record of what the reviewed materials support, partially support, overstate, fail to support, contradict, or leave not assessable.

## Who should use it

- Researchers preparing a paper submission
- PhD students checking a thesis or defense report
- Authors releasing benchmark results or research code
- Teams preparing artifact evaluation packages
- Reviewers or collaborators checking whether claims are evidence-bound

## Repository layout

```text
.
|-- reproproof/
|   |-- SKILL.md
|   |-- README.md
|   |-- references/
|   |   |-- audit-scope-routing.md
|   |   `-- reproducibility-checklist.md
|   `-- templates/
|       `-- audit-report.md
|-- docs/
|   |-- comparison.md
|   |-- launch-kit.md
|   `-- release-checklist.md
|-- examples/
|   `-- reproproof/
|       |-- artifact-package-audit.md
|       `-- paper-only-audit.md
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   `-- workflows/
|-- scripts/
|   `-- validate_skills.py
|-- CITATION.cff
|-- CONTRIBUTING.md
|-- LICENSE
|-- SECURITY.md
`-- README.md
```

## Install

### Generic install

Copy the `reproproof/` directory into any agent runtime or project that supports skill-style folders with a `SKILL.md` entry point.

```text
skills/
`-- reproproof/
    |-- SKILL.md
    |-- references/
    `-- templates/
```

### Cursor-compatible install

For Cursor-style project installation, copy `reproproof/` to:

```text
your-project/.cursor/skills/reproproof/
```

For personal installation, copy it to:

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

Full audits follow `reproproof/templates/audit-report.md` and include:

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

## Share or cite

If ReproProof helps your paper, benchmark, or artifact release, consider starring the repository or citing it with the metadata in [CITATION.cff](CITATION.cff).

Launch copy and community-post templates are available in [docs/launch-kit.md](docs/launch-kit.md).

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
