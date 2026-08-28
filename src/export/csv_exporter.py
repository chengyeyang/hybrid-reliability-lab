import csv


class CSVExporter:
    HEADER = [
        "test_id",
        "test_name",
        "start_time",
        "end_time",
        "duration",
        "measurement",
        "outcome",
        "error",
        "cleanup_error"
    ]

    def export(self, records, file_path):
        if not records:  # to filter out empty records' case
            return

        # Determine header behavior before append mode creates a missing file.
        # check if file already exists or exits but is empty
        # this needs to be placed before opening the file
        should_write_header = (
            not file_path.exists()
            or file_path.stat().st_size == 0
        )

        with file_path.open("a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            if should_write_header:
                writer.writerow(self.HEADER)

            for record in records:
                writer.writerow([
                    record.test_id,
                    record.test_name,
                    record.start_time.isoformat(),
                    record.end_time.isoformat(),
                    record.duration.total_seconds(),
                    record.measurement,
                    record.outcome,
                    record.error,
                    record.cleanup_error
                ])
