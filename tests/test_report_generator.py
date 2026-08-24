from src.report.report_generator import ReportGenerator
from src.data.test_record import OneTestRecord
import datetime
import pytest


def make_test_record(
    test_name="test",
    measurement=1.5,
    outcome="PASS",
    error=None,
):
    return OneTestRecord(
        test_name=test_name,
        start_time=datetime.datetime(2026, 8, 24, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 24, 13, 2, 0),
        duration=datetime.timedelta(seconds=120),
        measurement=measurement,
        outcome=outcome,
        error=error,
    )


def test_generate_report_with_mixed_outcomes():
    record1 = make_test_record(
        test_name="test1",
        measurement=1.5,
        outcome="PASS",
        error=None,
    )

    record2 = make_test_record(
        test_name="test2",
        measurement=1.5,
        outcome="FAIL",
        error=None,
    )

    record3 = make_test_record(
        test_name="test3",
        measurement=1.5,
        outcome="PASS",
        error=None,
    )

    record4 = make_test_record(
        test_name="test4",
        measurement=1.5,
        outcome="ERROR",
        error=None,
    )

    records = [record1, record2, record3, record4]
    generator = ReportGenerator()
    test_report = generator.generate(records)

    assert test_report.total_tests == 4
    assert test_report.pass_count == 2
    assert test_report.fail_count == 1
    assert test_report.error_count == 1
    assert test_report.pass_rate == 0.5


def test_generate_report_with_empty_records():
    records = []
    generator = ReportGenerator()
    test_report = generator.generate(records)

    assert test_report.total_tests == 0
    assert test_report.pass_count == 0
    assert test_report.fail_count == 0
    assert test_report.error_count == 0
    assert test_report.pass_rate is None


def test_generate_report_with_invalid_outcome_raises_value_error():
    record = make_test_record(
        test_name="test",
        measurement=1.5,
        outcome="UNKNOWN",
        error=None,
    )

    records = [record]
    generator = ReportGenerator()

    with pytest.raises(ValueError):
        generator.generate(records)


def test_generate_report_with_valid_measurements_including_zero():
    record1 = make_test_record(
        test_name="test1",
        measurement=0,
        outcome="PASS",
        error=None,
    )

    record2 = make_test_record(
        test_name="test2",
        measurement=1.5,
        outcome="FAIL",
        error=None,
    )

    record3 = make_test_record(
        test_name="test3",
        measurement=4.5,
        outcome="PASS",
        error=None,
    )

    records = [record1, record2, record3]
    generator = ReportGenerator()
    test_report = generator.generate(records)

    assert test_report.measurement_count == 3
    assert test_report.minimum_measurement == 0
    assert test_report.maximum_measurement == 4.5
    assert test_report.average_measurement == 2.0


def test_generate_report_with_no_valid_measurements():
    record = make_test_record(
        test_name="test1",
        measurement=None,
        outcome="PASS",
        error=None,
    )

    records = [record]
    generator = ReportGenerator()
    test_report = generator.generate(records)

    assert test_report.measurement_count == 0
    assert test_report.minimum_measurement is None
    assert test_report.maximum_measurement is None
    assert test_report.average_measurement is None


def test_generate_report_includes_fail_and_error_details():
    record1 = make_test_record(
        test_name="test1",
        measurement=0,
        outcome="PASS",
        error=None,
    )

    record2 = make_test_record(
        test_name="test2",
        measurement=1.5,
        outcome="FAIL",
        error="record2 error",
    )

    record3 = make_test_record(
        test_name="test3",
        measurement=4.5,
        outcome="ERROR",
        error="record3 error",
    )

    records = [record1, record2, record3]
    generator = ReportGenerator()
    test_report = generator.generate(records)

    assert test_report.failure_details == [
        {
            "test_name": "test2",
            "outcome": "FAIL",
            "measurement": 1.5,
            "error": "record2 error"
        },
        {
            "test_name": "test3",
            "outcome": "ERROR",
            "measurement": 4.5,
            "error": "record3 error"
        }
    ]


def test_generate_report_with_all_pass_has_no_failure_details():
    record1 = make_test_record(
        test_name="test1",
        measurement=1.5,
        outcome="PASS",
        error=None,
        )

    records = [record1]
    generator = ReportGenerator()
    test_report = generator.generate(records)

    assert test_report.failure_details == []
