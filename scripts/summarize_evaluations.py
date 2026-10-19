import json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
evaluation_dir = project_root / "evaluations"

valid_severities = {"minor", "moderate", "major", "critical"}
valid_outcomes = {"PASS", "FAIL"}

records = []

for file_path in sorted(evaluation_dir.glob("CASE_*.json")):
    with file_path.open(encoding="utf-8") as file:
        record = json.load(file)

    if record["severity"] not in valid_severities:
        raise ValueError(
            f"{file_path.name}: invalid severity "
            f"'{record['severity']}'"
        )

    if record["outcome"] not in valid_outcomes:
        raise ValueError(
            f"{file_path.name}: invalid outcome "
            f"'{record['outcome']}'"
        )

    records.append(record)

print(f"Total evaluations: {len(records)}")

for record in records:
    print(
        f"{record['case_id']}: "
        f"{record['outcome']} "
        f"(severity: {record['severity']})"
    )

failed = sum(record["outcome"] == "FAIL" for record in records)
print(f"Failed evaluations: {failed}")
print("Validation: PASSED")
