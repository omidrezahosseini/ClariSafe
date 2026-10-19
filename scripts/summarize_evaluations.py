import json
from pathlib import Path

# Locate the evaluation files relative to this script.
project_root = Path(__file__).resolve().parent.parent
evaluation_dir = project_root / "evaluations"

# Load all JSON evaluation records.
records = []

for file_path in sorted(evaluation_dir.glob("CASE_*.json")):
    with file_path.open(encoding="utf-8") as file:
        records.append(json.load(file))

# Summarize the evaluation results.
print(f"Total evaluations: {len(records)}")

for record in records:
    print(
        f"{record['case_id']}: "
        f"{record['outcome']} "
        f"(severity: {record['severity']})"
    )

failed = sum(
    record["outcome"] == "FAIL"
    for record in records
)

print(f"Failed evaluations: {failed}")
