# `analysis/reviewed/` — promotion staging

Where consolidated analysis lands once a reviewer has examined it, immediately **before** a
promotion decision. It is the waiting room between `analysis/{human,ai}/` and the canonical KB.

```text
analysis/human/transport/2026-10-09-transport-upe-coverage.md     status: working
analysis/ai/transport/2026-10-09-transport-requirement-extraction.md
        ↓  reviewer consolidates the findings that survived scrutiny
analysis/reviewed/transport/2026-10-14-transport-upe-consolidated.md   status: reviewed
        ↓  Architecture Committee decides per finding
knowledge-base/requirements/…  ·  problems/…  ·  capabilities/…  ·  architecture/decisions/…
```

## Rules

- **Still non-canonical.** `status: reviewed` means "examined", not "true". The KB records do not
  exist until the gate has been passed and they have been created.
- **One consolidated artefact per topic and round**, named `<iso-date>-<topic>-consolidated.md`,
  using the contract in [`../README.md`](../README.md).
- **Say what was rejected.** A promotion round that accepted three findings out of twenty must state
  what the other seventeen were, and why — otherwise the next round re-litigates them.
- **List the promotions.** Each accepted finding names the KB record it became, and the analysis
  records it in its `promoted:` field.
- **Do not edit payloads or canonical records from here.** Promotion means *creating a KB record
  that cites this analysis*, not copying text across.

This directory is empty until the first review round runs. It is created on first use; git does not
track empty directories.
