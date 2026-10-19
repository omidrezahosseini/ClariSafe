import sys
import unittest
from pathlib import Path

# Make the scripts directory available for imports.
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "scripts"))

from validation import validate_record


class TestEvaluationValidation(unittest.TestCase):

    def test_valid_record(self):
        record = {"severity": "critical", "outcome": "FAIL"}
        self.assertTrue(validate_record(record))

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
