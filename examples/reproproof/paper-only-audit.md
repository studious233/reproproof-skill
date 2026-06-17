# ReproProof Example: Paper-only Audit

## Executive summary

- Overall readiness: Release with limitations
- Main risk: The main performance claim is only partially supported because the paper reports aggregate scores but does not describe repeated runs or uncertainty.
- Most important fix: Add seeds, number of runs, and uncertainty reporting for the central benchmark table.

## Audit boundary

Reviewed:

- Draft paper text
- Main result table
- Figure captions

Not available in the reviewed material:

- Source code
- Training logs
- Dataset download scripts
- Full configuration files

## Evidence Boundary Ledger

| ID | Claim | Location | Evidence found | Assessment | Risk |
|---|---|---|---|---|---|
| C1 | "Our method improves accuracy across all benchmark tasks." | Abstract | Table 1 reports higher mean scores on four tasks. | Partially supported | High |
| C2 | "The method is computationally efficient." | Introduction | No runtime, memory, or hardware comparison is provided. | Unsupported | High |
| C3 | "The ablation confirms the routing module is necessary." | Section 4.3 | Ablation table removes the routing module but reports one run only. | Partially supported | Medium |

## Findings

### High Unsupported efficiency claim

**Issue:** The paper claims computational efficiency but does not provide runtime, memory, hardware, or throughput evidence.

**Evidence:** The reviewed paper includes accuracy tables but no compute table or runtime appendix.

**Why it matters:** Efficiency claims require compute evidence; otherwise readers cannot inspect the tradeoff.

**Recommended fix:** Either add compute measurements under a disclosed hardware setup or narrow the claim to accuracy only.

## Release readiness actions

1. Add run count, seeds, and uncertainty for Table 1.
2. Add compute measurements or remove efficiency language.
3. Add an artifact availability statement explaining that code and configs were not reviewed.
