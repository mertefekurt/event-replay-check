# event-replay-check

**Integration Note.** Audit event stream plans for replay, ordering, and schema-version readiness.

## Where It Fits

Event-driven systems need replay and compatibility plans. This CLI catches weak event-stream contracts early.

## Install

`event-replay-check` accepts event stream contract or architecture notes in text, JSON, JSONL, or CSV form.

## CI Example

```bash
python -m pip install -e ".[dev]"
event-replay-check examples/sample.txt
event-replay-check examples/sample.txt --json --fail-on medium
```

## Schema

| Rule | Severity | Meaning |
|---|---:|---|
| `replay-unsupported` | high | event replay is unsupported |
| `missing-schema-version` | medium | schema version is missing |
| `unknown-ordering` | low | ordering guarantee is unclear |

## License

```bash
ruff check .
pytest
python -m event_replay_check --help
```

License: MIT

### Example Input

```text
event order.created replay unsupported schema_version missing ordering unknown
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the event-replay-check policy surface explicit.
