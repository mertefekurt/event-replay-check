<p align="center">
  <img src="assets/readme-cover.svg" alt="Event Replay Check cover" width="100%" />
</p>

# Event Replay Check

![stack](https://img.shields.io/badge/stack-Python-2563eb?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-16a34a?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-dc2626?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-7c3aed?style=flat-square)

Audit event stream plans for replay, ordering, and schema-version readiness.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `event-replay-check` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
event-replay-check examples/sample.txt
event-replay-check examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `replay-unsupported` | high | event replay is unsupported |
| `missing-schema-version` | medium | schema version is missing |
| `unknown-ordering` | low | ordering guarantee is unclear |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
event order.created replay unsupported schema_version missing ordering unknown
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m event_replay_check --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Event Replay Check policy easy to review.
