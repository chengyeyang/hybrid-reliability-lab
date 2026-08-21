from src.framework.result import Result
from src.logger.logger import Logger
import datetime
from src.data.test_record import TestRecord as OneTestRecord


def test_logger_records_result_data():
    result = Result()
    result.test_name = "test name"
    result.start_time = datetime.datetime(2026, 6, 7, 14, 30, 0)
    result.end_time = datetime.datetime(2026, 6, 7, 14, 35, 30)
    result.duration = datetime.timedelta(minutes=5, seconds=30)
    result.measurement = 25
    result.outcome = "PASS"
    result.error = None

    logger = Logger()
    logger.log(result)

    assert len(logger.records) == 1  # if this case fails, there's no need to run the rest

    record = logger.records[0]

    assert record.test_name == "test name"
    assert record.start_time == datetime.datetime(2026, 6, 7, 14, 30, 0)
    assert record.end_time == datetime.datetime(2026, 6, 7, 14, 35, 30)
    assert record.duration == datetime.timedelta(minutes=5, seconds=30)
    assert record.measurement == 25
    assert record.outcome == "PASS"
    assert record.error is None
    assert isinstance(record, OneTestRecord)


def test_logger_stores_result_snapshot():
    result = Result()
    result.error = None

    logger = Logger()
    logger.log(result)

    result.error = "add an error now"

    assert logger.records[0].error is None


def test_logger_records_multiple_results():
    result1 = Result()
    result1.test_name = "test name 1"
    result1.start_time = datetime.datetime(2026, 6, 7, 14, 30, 0)
    result1.end_time = datetime.datetime(2026, 6, 7, 14, 35, 30)
    result1.duration = datetime.timedelta(minutes=5, seconds=30)
    result1.measurement = 25
    result1.outcome = "PASS"
    result1.error = None

    result2 = Result()
    result2.test_name = "test name 2"
    result2.start_time = datetime.datetime(2026, 8, 20, 14, 30, 0)
    result2.end_time = datetime.datetime(2026, 8, 20, 14, 35, 15)
    result2.duration = datetime.timedelta(minutes=5, seconds=15)
    result2.measurement = 0
    result2.outcome = "FAIL"
    result2.error = None

    logger = Logger()
    logger.log(result1)
    logger.log(result2)

    assert len(logger.records) == 2

    assert logger.records[0].test_name == "test name 1"
    assert logger.records[0].measurement == 25
    assert logger.records[0].outcome == "PASS"

    assert logger.records[1].test_name == "test name 2"
    assert logger.records[1].measurement == 0
    assert logger.records[1].outcome == "FAIL"


def test_logger_result_with_error():
    result = Result()
    result.outcome = "ERROR"
    result.error = "This is an error for unit test"

    logger = Logger()
    logger.log(result)

    assert logger.records[0].outcome == "ERROR"
    assert logger.records[0].error == "This is an error for unit test"


