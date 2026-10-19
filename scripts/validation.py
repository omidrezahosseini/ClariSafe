VALID_SEVERITIES = {"minor", "moderate", "major", "critical"}
VALID_OUTCOMES = {"PASS", "FAIL"}


def validate_record(record):
    """Validate severity and outcome fields in an evaluation record."""

    if record["severity"] not in VALID_SEVERITIES:
        raise ValueError(
            f"Invalid severity: {record['severity']}"
        )

    if record["outcome"] not in VALID_OUTCOMES:
        raise ValueError(
            f"Invalid outcome: {record['outcome']}"
        )

    return True
