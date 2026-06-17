# Comparison and Positioning

ReproProof is a compact reproducibility-audit skill, not a full research automation system.

## Adjacent open-source projects

| Area | Examples | What they provide | ReproProof position |
|---|---|---|---|
| Reproducibility pipelines | [AI4Reproducibility](https://github.com/sistm/AI4Reproducibility) | End-to-end workflows for reproducing or assessing results | ReproProof is lighter: it audits readiness and claim support before release |
| Academic research skill packs | [Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) and similar catalogs | Broad skills for empirical research, literature work, coding, and writing | ReproProof focuses only on evidence boundaries and reproducibility gaps |
| Artifact-evaluation templates | Conference and community artifact checklists | Structured expectations for artifact review | ReproProof turns those expectations into an agent-facing audit workflow |
| Claim-audit agents | Research-agent plugins and paper-checking prompts | Claim extraction and consistency checks | ReproProof adds bounded-audit discipline and a reusable Evidence Boundary Ledger |

## Differentiators

- Uses an Evidence Boundary Ledger as the primary audit artifact.
- Separates "missing from reviewed material" from "not available to review".
- Treats overclaiming, protocol ambiguity, and figure/table inconsistency as reproducibility risks.
- Works with partial material while stating the audit boundary.
- Provides reusable references and a full audit report template.

## Current limitations

- ReproProof does not run experiments.
- ReproProof does not guarantee that results reproduce.
- ReproProof does not replace domain review or artifact evaluation.
- ReproProof cannot verify code, data, or logs that were not provided.

## Contribution thesis

The contribution is procedural:

1. Make research claims auditable against reviewed evidence.
2. Make unavailable material explicit instead of silently converting it into a defect.
3. Give authors a lightweight final pass before submission, release, rebuttal, or defense.
