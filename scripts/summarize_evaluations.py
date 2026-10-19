import json
from pathlib import Path

from validation import validate_record


def main():
    project_root = Path(__file__).resolve().parent.parent
    evaluations_dir = project_root / "evaluations"

    files = sorted(
        list(evaluations_dir.glob("CASE_*.json"))
        + list(evaluations_dir.glob("REAL_*.json"))
    )

    if not files:
        raise ValueError("No evaluation files found.")

    failed = 0

    print(f"Total evaluations: {len(files)}")

    for file in files:
        with file.open(encoding="utf-8") as f:
            record = json.load(f)

        validate_record(record)

        case_id = record["case_id"]
        outcome = record["outcome"]
        severity = record["severity"]

        if outcome == "FAIL":
            failed += 1

        print(f"{case_id}: {outcome} (severity: {severity})")

    print(f"Failed evaluations: {failed}")
    print("Validation: PASSED")


if __name__ == "__main__":
    main()
