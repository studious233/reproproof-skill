# ReproProof Launch Kit

Use this when sharing ReproProof with researchers, PhD students, artifact authors, and agent-tool users.

## One-line pitch

ReproProof is a portable agent skill that audits whether research claims are supported by reviewed evidence and whether another researcher has enough detail to inspect or reproduce the result.

## Short post

```text
I released ReproProof, a portable agent skill for checking research artifacts before submission or release.

It audits:
- unsupported or overstated claims
- missing reproduction details
- figure/table/text inconsistencies
- artifact evaluation readiness

Core idea: an Evidence Boundary Ledger that maps each claim to reviewed evidence.

GitHub: https://github.com/studious233/reproproof-skill
```

## Longer post

```text
I built ReproProof because paper and benchmark drafts often fail in a very specific way: the claims are stronger than the evidence, or the reproduction path is scattered across prose, configs, logs, and README files.

ReproProof is a lightweight agent skill that performs a bounded reproducibility audit. It does not write the paper or claim that results reproduce. Instead, it checks the reviewed materials and produces an Evidence Boundary Ledger:

- Supported
- Partially supported
- Overstated
- Unsupported
- Contradicted
- Not assessable

It is meant as a final pass before submission, thesis defense, code release, artifact evaluation, or rebuttal.

GitHub: https://github.com/studious233/reproproof-skill
```

## Chinese post

```text
我发布了 ReproProof，一个用于论文、benchmark 报告和开源 artifact 的可复现性审计 agent skill。

它不帮你“润色论文”，而是检查更关键的问题：

- claim 有没有被表格、图、日志、配置或 README 支撑
- 实验协议是否足够清楚
- 是否缺少 seed、数据版本、baseline、硬件、命令等复现信息
- abstract / method / table / caption / README 是否互相矛盾
- 有没有过度声称或证据边界不清

核心输出是 Evidence Boundary Ledger，把每个 claim 和证据逐条对齐。

GitHub: https://github.com/studious233/reproproof-skill
```

## Suggested communities

- LinkedIn: academic, research engineering, open science audience
- X/Twitter: AI agents, reproducible research, PhD/research communities
- Reddit: `r/MachineLearning`, `r/academia`, `r/PhD`, `r/OpenScience`
- Hacker News: `Show HN: ReproProof, an agent skill for auditing research claims before submission`
- Awesome lists: reproducible research, open science, AI agents, agent skills

## Suggested outreach message

```text
Hi, I built a small open-source agent skill that audits research artifacts for unsupported claims and reproducibility gaps. It may be useful for paper submission or artifact evaluation prep:

https://github.com/studious233/reproproof-skill

Feedback from researchers or artifact authors would be very useful.
```

## What to ask for

Ask for concrete feedback instead of only asking for stars:

- Was the Evidence Boundary Ledger useful?
- Which artifact type should ReproProof support better?
- What reproduction details are most often missing in your field?
- Would this fit into your paper submission checklist?

If people find it useful, then ask them to star the repository so others can discover it.
