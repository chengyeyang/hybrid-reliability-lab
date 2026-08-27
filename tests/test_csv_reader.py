from src.data.test_record import OneTestRecord
import datetime
from src.export.csv_exporter import CSVExporter
from src.data.csv_reader import CSVReader


def test_csv_reader_restores_exported_record(tmp_path):
    test_record = OneTestRecord(
        test_name="test_name",
        start_time=datetime.datetime(2026, 8, 27, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 27, 15, 0, 0),
        duration=datetime.timedelta(hours=2),
        measurement=1,
        outcome="FAIL",
        error="Timeout...",
    )

    file_path = tmp_path / "test_result.csv"

    exporter = CSVExporter()
    exporter.export([test_record], file_path)

    reader = CSVReader()
    records = reader.read(file_path)

    assert records == [test_record]


def test_csv_reader_restores_none_measurement(tmp_path):
    test_record = OneTestRecord(
        test_name="test_name",
        start_time=datetime.datetime(2026, 8, 27, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 27, 15, 0, 0),
        duration=datetime.timedelta(hours=2),
        measurement=None,
        outcome="FAIL",
        error="Timeout...",
    )

    file_path = tmp_path / "test_result.csv"

    exporter = CSVExporter()
    exporter.export([test_record], file_path)

    reader = CSVReader()
    records = reader.read(file_path)

    assert records[0].measurement is None


def test_csv_reader_preserves_zero_measurement(tmp_path):
    test_record = OneTestRecord(
        test_name="test_name",
        start_time=datetime.datetime(2026, 8, 27, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 27, 15, 0, 0),
        duration=datetime.timedelta(hours=2),
        measurement=0,
        outcome="FAIL",
        error="Timeout...",
    )

    file_path = tmp_path / "test_result.csv"

    exporter = CSVExporter()
    exporter.export([test_record], file_path)

    reader = CSVReader()
    records = reader.read(file_path)

    assert records[0].measurement == 0


def test_csv_reader_restores_multiple_records(tmp_path):
    test_record1 = OneTestRecord(
        test_name="test_name",
        start_time=datetime.datetime(2026, 8, 27, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 27, 15, 0, 0),
        duration=datetime.timedelta(hours=2),
        measurement=0,
        outcome="PASS",
        error=None,
    )

    test_record2 = OneTestRecord(
        test_name="test_name",
        start_time=datetime.datetime(2026, 8, 27, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 27, 15, 0, 0),
        duration=datetime.timedelta(hours=2),
        measurement=0,
        outcome="FAIL",
        error="Timeout...",
    )

    test_record3 = OneTestRecord(
        test_name="test_name",
        start_time=datetime.datetime(2026, 8, 27, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 27, 15, 0, 0),
        duration=datetime.timedelta(hours=2),
        measurement=0,
        outcome="ERROR",
        error="Unexpected error...",
    )

    file_path = tmp_path / "test_result.csv"

    exporter = CSVExporter()
    exporter.export([test_record1, test_record2, test_record3], file_path)

    reader = CSVReader()
    records = reader.read(file_path)

    assert records == [test_record1, test_record2, test_record3]
