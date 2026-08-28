from src.data.test_record import OneTestRecord


class Logger:

    def __init__(self):
        self.records = []

    # pass in result and transfer it to TestRecord format
    def log(self, result):
        record = OneTestRecord(
            test_name=result.test_name,
            start_time=result.start_time,
            end_time=result.end_time,
            duration=result.duration,
            measurement=result.measurement,
            outcome=result.outcome,
            error=result.error,
            cleanup_error=result.cleanup_error
        )

        self.records.append(record)
