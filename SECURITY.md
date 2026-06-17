# Security Policy

## Supported scope

This repository contains ReproProof skill instructions, examples, and documentation.

Security reports are in scope when they involve:

- Unsafe instructions that could cause unintended file deletion or secret disclosure
- Example content that leaks credentials, private paths, or private research data
- Documentation that encourages unsafe handling of unreleased research artifacts

## Reporting

Open a private security advisory if the hosting platform supports it. Otherwise, open an issue with minimal reproduction details and avoid including secrets or private artifacts.

## Safety defaults

- ReproProof must not claim that results reproduce unless the reviewed materials include sufficient code, data, commands, and outputs.
- ReproProof must distinguish unavailable material from actual defects.
- ReproProof must not expose private paper drafts, datasets, credentials, or reviewer-confidential material in examples.
