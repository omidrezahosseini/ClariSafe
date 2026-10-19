import unittest

VALID_SEVERITIES = {"minor", "moderate", "major", "critical"}
VALID_OUTCOMES = {"PASS", "FAIL"}


def validate_record(record):
    if record["severity"] not in VALID_SEVERITIES:
        raise ValueError("Invalid severity")

    if record["outcome"] not in VALID_OUTCOMES:
        raise ValueError("Invalid outcome")


class TestEvaluationValidation(unittest.TestCase):

    def test_valid_record(self):
        record = {"severity": "critical", "outcome": "FAIL"}
        validate_record(record)

    def test_invalid_severity(self):
        record = {"severity": "very_bad", "outcome": "FAIL"}
        with self.assertRaises(ValueError):
            validate_record(record)

    def test_invalid_outcome(self):
        record = {"severity": "critical", "outcome": "UNKNOWN"}
        with self.assertRaises(ValueError):
            validate_record(record)


if __name__ == "__main__":
    unittest.main()
