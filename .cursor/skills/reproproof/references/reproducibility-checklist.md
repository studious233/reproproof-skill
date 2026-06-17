# Reproducibility Checklist

Use this checklist when auditing whether a research artifact is ready for independent reproduction. Mark each item as `Pass`, `Partial`, `Missing`, or `N/A`.

## Data

- Dataset name, version, license, and access path are specified.
- Data acquisition date or snapshot identifier is provided when relevant.
- Train, validation, test, and benchmark splits are defined.
- Preprocessing, filtering, deduplication, and leakage prevention steps are described.
- Synthetic, private, restricted, or proprietary data constraints are disclosed.

## Method and implementation

- Model architecture, algorithm, or intervention details are sufficient to reimplement.
- Important implementation choices are documented rather than hidden in prose.
- Code entry points are identified.
- Configuration files match the paper or report.
- Dependency versions and installation steps are provided.

## Experiment protocol

- Hyperparameters and search ranges are listed.
- Random seeds and number of runs are reported.
- Hardware, runtime, memory, and accelerator details are provided when they affect results.
- Training, inference, and evaluation commands are available.
- Checkpoints, expected outputs, or result artifacts are available or clearly scoped as unavailable.

## Evaluation

- Metric definitions and aggregation rules are explicit.
- Baseline sources, versions, and tuning budgets are stated.
- Comparison protocols are fair or differences are disclosed.
- Statistical uncertainty, confidence intervals, or significance tests are reported when needed.
- Negative results, failed runs, or excluded settings are disclosed when relevant.

## Release package

- README explains how to reproduce core results.
- Scripts are runnable in the documented order.
- Paths, environment variables, and credentials are documented without exposing secrets.
- Licenses and third-party asset restrictions are clear.
- Known limitations and expected deviations are documented.
