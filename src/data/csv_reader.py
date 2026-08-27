import csv
import datetime
import uuid

from src.data.test_record import OneTestRecord


class CSVReader:

    def read(self, file_path):
        records = []

        with file_path.open("r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)  # Utilize csv.DictReader method to do the transformation

            for row in reader:
                # convert row → OneTestRecord

                if row["measurement"] == "":
                    measurement = None
                else:
                    measurement = float(row["measurement"])

                error = row["error"] if row["error"] else None

                record = OneTestRecord(
                    test_id=uuid.UUID(row["test_id"]),
                    test_name=row["test_name"],
                    start_time=datetime.datetime.fromisoformat(row["start_time"]),
                    end_time=datetime.datetime.fromisoformat(row["end_time"]),
                    duration=datetime.timedelta(seconds=float(row["duration"])),
                    outcome=row["outcome"],
                    measurement=measurement,
                    error=error
                )

                records.append(record)

        return records
