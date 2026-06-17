# Audit Scope Routing

Use this guide to adapt a ReproProof audit to the materials actually provided. Do not treat unavailable materials as defects; report them as outside the audit boundary.

| Materials provided | Primary audit focus | Avoid overclaiming |
|---|---|---|
| Paper or report only | Claim-evidence alignment, missing protocol details, figure/table/text consistency, overclaiming | Do not assert code, data, or release package defects unless they are described in the paper |
| Paper + README | Reproduction path, installation steps, expected outputs, paper-to-release consistency | Do not infer command correctness without scripts or logs |
| Paper + code/configs | Paper-code consistency, command completeness, hyperparameter traceability, dependency clarity | Do not claim results reproduce unless outputs or logs are available |
| Paper + logs/results | Result traceability, metric definitions, aggregation, repeated-run evidence, table/log consistency | Do not assume hidden code matches logs without configs or scripts |
| Artifact evaluation package | End-to-end readiness: setup, data access, run commands, expected outputs, compute requirements, license limits | Do not promise acceptance; report readiness against reviewed criteria only |
| Replication target from another work | Ambiguous protocol, hidden assumptions, unavailable data, metric uncertainty, reproduction blockers | Distinguish flaws in the target paper from materials unavailable to the reviewer |
| Rebuttal or defense material | Whether response claims are supported by existing evidence and whether new claims exceed reviewed results | Do not generate new evidence or strengthen claims beyond the provided record |

When multiple material types are available, combine the relevant rows and state the final audit boundary explicitly.
