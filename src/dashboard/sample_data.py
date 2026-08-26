from src.report.test_report import OneTestReport
from src.data.test_record import OneTestRecord
import datetime


report = OneTestReport(
    total_tests=10,
    pass_count=7,
    fail_count=2,
    error_count=1,
    pass_rate=0.7,
    measurement_count=8,
    minimum_measurement=2.0,
    maximum_measurement=6.0,
    average_measurement=3.0,
    failure_details=[{
                        "test_name": "NAME",
                        "outcome": "FAIL",
                        "measurement": 1.0,
                        "error": "Timeout"
                    }],
)

records = [
    OneTestRecord(
        test_name="name1",
        start_time=datetime.datetime(2026, 8, 26, 7, 30, 0),
        end_time=datetime.datetime(2026, 8, 26, 8, 30, 0),
        duration=datetime.timedelta(hours=1),
        measurement=1.0,
        outcome="PASS",
        error=None
    ),
    OneTestRecord(
        test_name="name2",
        start_time=datetime.datetime(2026, 8, 26, 7, 30, 0),
        end_time=datetime.datetime(2026, 8, 26, 8, 30, 0),
        duration=datetime.timedelta(hours=1),
        measurement=1.0,
        outcome="FAIL",
        error="Timeout"
    ),
    OneTestRecord(
        test_name="name3",
        start_time=datetime.datetime(2026, 8, 26, 7, 30, 0),
        end_time=datetime.datetime(2026, 8, 26, 8, 30, 0),
        duration=datetime.timedelta(hours=1),
        measurement=3.0,
        outcome="ERROR",
        error="Unexpected error"
    ),
]
