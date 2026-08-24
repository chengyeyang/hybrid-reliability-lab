from src.report.test_report import TestReport


class ReportGenerator:

    def generate(self, records):

        total_tests = len(records)
        pass_count = 0
        fail_count = 0
        error_count = 0
        measurements = []
        minimum_measurement = None
        maximum_measurement = None
        average_measurement = None
        failure_details = []

        for record in records:
            if record.outcome == "PASS":
                pass_count += 1

            elif record.outcome == "FAIL":
                fail_count += 1

            elif record.outcome == "ERROR":
                error_count += 1

            else:
                raise ValueError(f"Invalid test outcome: {record.outcome}")

            if record.outcome in ["FAIL", "ERROR"]:
                failure_details.append(
                    {
                        "test_name": record.test_name,
                        "outcome": record.outcome,
                        "measurement": record.measurement,
                        "error": record.error
                    }
                )

            if record.measurement is not None:
                measurements.append(record.measurement)

        if total_tests == 0:
            pass_rate = None
        else:
            pass_rate = pass_count / total_tests

        if measurements:
            minimum_measurement = min(measurements)
            maximum_measurement = max(measurements)
            average_measurement = sum(measurements) / len(measurements)

        return TestReport(
            total_tests=total_tests,
            pass_count=pass_count,
            fail_count=fail_count,
            error_count=error_count,
            pass_rate=pass_rate,
            measurement_count=len(measurements),
            minimum_measurement=minimum_measurement,
            maximum_measurement=maximum_measurement,
            average_measurement=average_measurement,
            failure_details=failure_details
        )
