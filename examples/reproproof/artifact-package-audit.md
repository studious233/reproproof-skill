# ReproProof Example: Artifact Package Audit

## Executive summary

- Overall readiness: Mostly ready
- Main risk: The README gives runnable commands but expected outputs are not documented.
- Most important fix: Add expected metrics and checksums for the primary reproduction path.

## Audit boundary

Reviewed:

- Paper PDF
- GitHub README
- `configs/main.yaml`
- `scripts/train.sh`
- `scripts/evaluate.sh`
- `results/table1.csv`

Not available in the reviewed material:

- Raw private dataset
- Model checkpoints

## Evidence Boundary Ledger

| ID | Claim | Location | Evidence found | Assessment | Risk |
|---|---|---|---|---|---|
| C1 | "Table 1 can be reproduced with the released scripts." | README | `train.sh` and `evaluate.sh` exist, but expected outputs are not listed. | Partially supported | Medium |
| C2 | "The released config matches the reported main experiment." | Paper Section 4 / config | Dataset, model size, and learning rate match; seed count differs. | Partially supported | High |
| C3 | "Private data restrictions are documented." | README | README explains access requirements and substitute public-data mode. | Supported | Low |

## Findings

### High Config and paper seed mismatch

**Issue:** The paper says results use five seeds, while `configs/main.yaml` lists one seed.

**Evidence:** Paper Section 4 states "five random seeds"; config contains `seeds: [1]`.

**Why it matters:** Reproducing the reported table requires the same repeated-run protocol.

**Recommended fix:** Add the full seed list or document that the public config is a reduced smoke-test config.

## Release readiness actions

1. Add expected output files and metric ranges to the README.
2. Clarify whether the config is full reproduction or smoke test.
3. Document checkpoint availability and expected deviations when checkpoints are not released.
