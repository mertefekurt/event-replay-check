from __future__ import annotations

from event_replay_check.models import Rule

PROJECT_NAME = 'event-replay-check'
SUMMARY = 'Audit event stream plans for replay, ordering, and schema-version readiness.'
SAMPLE_RISK = 'event order.created replay unsupported schema_version missing ordering unknown'
SAMPLE_CLEAN = 'event order.created replay supported schema_version v2 ordering per aggregate'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='replay-unsupported',
        severity='high',
        pattern='\\breplay\\s*(unsupported|none|missing)\\b',
        message='event replay is unsupported',
        recommendation='Define replay source and retention window.',
    ),
    Rule(
        code='missing-schema-version',
        severity='medium',
        pattern='\\bschema_version\\s*(missing|none|null)\\b',
        message='schema version is missing',
        recommendation='Version event payloads.',
    ),
    Rule(
        code='unknown-ordering',
        severity='low',
        pattern='\\bordering\\s*(unknown|missing|none)\\b',
        message='ordering guarantee is unclear',
        recommendation='Document ordering key and consumer expectations.',
    ),
)
