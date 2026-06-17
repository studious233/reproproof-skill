# ReproProof

A lightweight Agent Skill for auditing research claims, evidence boundaries, and reproducibility readiness before paper submission or code release.

> Find unsupported claims, missing experiment details, and reproducibility gaps before your paper or code goes public.

## What it does

ReproProof reviews research artifacts through a reproducibility-first lens. It helps identify whether a paper, thesis, benchmark report, experiment section, README, or release package gives another researcher enough evidence and procedural detail to inspect or reproduce the work.

Its core output is an **Evidence Boundary Ledger**: a claim-by-claim record of what the reviewed materials support, partially support, overstate, fail to support, contradict, or leave not assessable.

It focuses on:

- Claim-evidence alignment
- Unsupported or overstated scientific claims
- Missing reproduction details
- Experimental protocol clarity
- Figure, table, caption, text, README, code, and config consistency
- Artifact evaluation and code release readiness

## What it is not

ReproProof is not a paper writer, peer-review simulator, experiment runner, or publication pipeline. It does not guarantee reproducibility. It produces a bounded audit based on the materials provided.

## When to use it

Use ReproProof before:

- Submitting a paper
- Releasing research code or checkpoints
- Preparing an artifact evaluation package
- Responding to reviewer concerns about evidence or reproducibility
- Defending a thesis or technical report
- Attempting to replicate another work
- Publishing a benchmark or experiment report

## Files

```text
reproproof/
|-- SKILL.md
|-- README.md
|-- references/
|   |-- audit-scope-routing.md
|   `-- reproducibility-checklist.md
`-- templates/
    `-- audit-report.md
```

## Example requests

```text
Audit this paper draft for reproducibility readiness.
```

```text
Check whether the claims in this experiment section are supported by the tables and figures.
```

```text
Review this repository and README as an artifact evaluation package.
```

```text
Give me a quick ReproProof audit before I submit this benchmark report.
```

## Output

ReproProof can produce either a quick audit or a full audit.

A quick audit includes:

1. Overall readiness
2. Top risks
3. Claim-evidence gaps
4. Missing reproduction details
5. Immediate fixes

A full audit follows `templates/audit-report.md` and includes:

- Executive summary
- Audit boundary
- Evidence Boundary Ledger
- Findings with severity levels
- Reproducibility checklist
- Consistency checks
- Safer wording suggestions for overclaims
- Release readiness actions

## Severity levels

- **Critical**: A central claim is unsupported, contradicted, or impossible to reproduce from available materials.
- **High**: A major result has missing protocol details, unclear baselines, inconsistent numbers, or likely overclaiming.
- **Medium**: Reproducibility is possible but important details are incomplete or scattered.
- **Low**: Minor clarity, traceability, or packaging issue.
- **Positive**: Strong reproducibility practice worth preserving.

## Why ReproProof is intentionally small

Large academic-agent suites can manage literature review, drafting, citation checks, peer review, revision, and publication workflows. ReproProof does not compete with those systems.

It is designed as a final, standalone readiness pass that can be used with any workflow: LaTeX papers, notebooks, GitHub repositories, thesis drafts, benchmark reports, or artifact evaluation packages.

Its value is narrow by design: check whether claims are bounded by evidence and whether another researcher has enough information to inspect or reproduce the result.

## Installation

For a generic agent runtime, place this directory wherever that runtime loads skill folders from:

```text
skills/reproproof/
```

For Cursor-style project-level use, place this directory at:

```text
.cursor/skills/reproproof/
```

For Cursor-style personal use across projects, place it at:

```text
~/.cursor/skills/reproproof/
```

## License

This skill is distributed under the repository-level MIT License.
