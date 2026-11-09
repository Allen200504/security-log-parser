import csv
from collections import Counter
from pathlib import Path


def count_failed_logins(csv_path):
    failed_logins = Counter()

    with open(csv_path, encoding="utf-8-sig", newline="") as log_file:
        reader = csv.DictReader(log_file)
        if not {"username", "result"}.issubset(reader.fieldnames or []):
            raise ValueError("CSV must contain username and result columns.")

        for row in reader:
            username = (row["username"] or "").strip()
            result = (row["result"] or "").strip().lower()
            if not username or result not in {"success", "failed"}:
                raise ValueError(f"Invalid login record on line {reader.line_num}.")
            if result == "failed":
                failed_logins[username] += 1

    return failed_logins


if __name__ == "__main__":
    sample_path = Path(__file__).with_name("sample_logs.csv")
    failed_logins = count_failed_logins(sample_path)
    print(f"Total failed logins: {sum(failed_logins.values())}")
    for username, count in sorted(failed_logins.items()):
        print(f"{username}: {count}")
