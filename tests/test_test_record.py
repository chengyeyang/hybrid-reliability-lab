import datetime
from src.data.test_record import OneTestRecord as OneTestRecord
import pytest
from dataclasses import FrozenInstanceError


def test_test_record_preserves_test_data():
    start_time = datetime.datetime(2026, 8, 21, 7, 30, 0)
    end_time = datetime.datetime(2026, 8, 21, 8, 30, 0)
    duration = datetime.timedelta(hours=1)

    record = OneTestRecord(
        test_name="Test name",
        start_time=start_time,
        end_time=end_time,
        duration=duration,
        measurement=15,
        outcome="PASS",
        error=None,
        cleanup_error=None
    )

    assert record.test_name == "Test name"
    assert record.start_time == start_time
    assert record.end_time == end_time
    assert record.duration == duration
    assert record.measurement == 15
    assert record.outcome == "PASS"
    assert record.error is None
    assert record.test_id is not None


def test_test_record_generates_unique_id():
    record1 = OneTestRecord(
        test_name="Test name",
        start_time=datetime.datetime(2026, 8, 21, 7, 30, 0),
        end_time=datetime.datetime(2026, 8, 21, 8, 30, 0),
        duration=datetime.timedelta(hours=1),
        measurement=15,
        outcome="PASS",
        error=None,
        cleanup_error=None
    )

    record2 = OneTestRecord(
        test_name="Test name",
        start_time=datetime.datetime(2026, 8, 21, 7, 30, 0),
        end_time=datetime.datetime(2026, 8, 21, 8, 30, 0),
        duration=datetime.timedelta(hours=1),
        measurement=15,
        outcome="PASS",
        error=None,
        cleanup_error=None
    )

    assert record1.test_id is not None
    assert record2.test_id is not None
    assert record1.test_id != record2.test_id


def test_test_record_is_immutable():
    record = OneTestRecord(
        test_name="Test name",
        start_time=datetime.datetime(2026, 8, 21, 7, 30, 0),
        end_time=datetime.datetime(2026, 8, 21, 8, 30, 0),
        duration=datetime.timedelta(hours=1),
        measurement=15,
        outcome="PASS",
        error=None,
        cleanup_error=None
    )

    # to specifically catch the error "FrozenInstanceError" which happens we try to modify an immutable object
    with pytest.raises(FrozenInstanceError):
        record.outcome = "FAIL"

    assert record.outcome == "PASS"
