from src.data.test_record import TestRecord as TheTestRecord
import datetime
from src.export.csv_exporter import CSVExporter
import csv


# To reduce the repetition of creating records in the following tests
def make_test_record(
    test_name="test_name",
    measurement=11.5,
    outcome="PASS",
    error=None,
):
    return TheTestRecord(
        test_name=test_name,
        start_time=datetime.datetime(2026, 8, 23, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 23, 13, 0, 30),
        duration=datetime.timedelta(seconds=30),
        measurement=measurement,
        outcome=outcome,
        error=error,
    )


def test_csv_exporter_exports_single_record(tmp_path):  # tmp_path is a pytest fixture
    test_record = TheTestRecord(
            test_name="test_name",
            start_time=datetime.datetime(2026, 8, 23, 13, 0, 0),
            end_time=datetime.datetime(2026, 8, 23, 13, 0, 30),
            duration=datetime.timedelta(seconds=30),
            measurement=11.5,
            outcome="PASS",
            error=None
        )

    file_path = tmp_path / "single_record.csv"

    exporter = CSVExporter()
    exporter.export([test_record], file_path)

    assert file_path.is_file()

    with file_path.open(newline="") as csv_file:
        rows = list(csv.reader(csv_file))

    assert len(rows) == 2

    header = rows[0]
    assert header == [
        "test_id",
        "test_name",
        "start_time",
        "end_time",
        "duration",
        "measurement",
        "outcome",
        "error",
    ]

    data_row = rows[1]
    assert data_row[0] == str(test_record.test_id)
    assert data_row[1] == test_record.test_name
    assert data_row[2] == test_record.start_time.isoformat()
    assert data_row[3] == test_record.end_time.isoformat()
    assert data_row[4] == str(test_record.duration.total_seconds())
    assert data_row[5] == str(test_record.measurement)
    assert data_row[6] == test_record.outcome
    assert data_row[7] == ""


def test_csv_exporter_exports_multiple_records(tmp_path):  # tmp_path is a pytest fixture
    test_record1 = make_test_record(
        test_name="test_name_1",
        measurement=11.5,
        outcome="PASS",
        error=None,
    )

    test_record2 = make_test_record(
        test_name="test_name_2",
        measurement=12.5,
        outcome="PASS",
        error=None,
    )

    test_record3 = make_test_record(
        test_name="test_name_3",
        measurement=13.5,
        outcome="PASS",
        error=None,
    )

    file_path = tmp_path / "multiple_records.csv"

    exporter = CSVExporter()
    exporter.export([test_record1, test_record2, test_record3], file_path)

    with file_path.open(newline="") as csv_file:
        rows = list(csv.reader(csv_file))

    assert len(rows) == 4
    assert rows[1][1] == "test_name_1"
    assert rows[2][1] == "test_name_2"
    assert rows[3][1] == "test_name_3"


def test_csv_exporter_appends_records(tmp_path):  # tmp_path is a pytest fixture
    test_record1 = make_test_record(
        test_name="test_name_1",
        measurement=11.5,
        outcome="PASS",
        error=None,
    )

    test_record2 = make_test_record(
        test_name="test_name_2",
        measurement=12.5,
        outcome="PASS",
        error=None,
    )

    test_record3 = make_test_record(
        test_name="test_name_3",
        measurement=13.5,
        outcome="PASS",
        error=None,
    )

    file_path = tmp_path / "append_records.csv"

    exporter = CSVExporter()
    exporter.export([test_record1, test_record2], file_path)
    exporter.export([test_record3], file_path)

    with file_path.open(newline="") as csv_file:
        rows = list(csv.reader(csv_file))

    assert len(rows) == 4
    assert rows[1][1] == "test_name_1"
    assert rows[2][1] == "test_name_2"
    assert rows[3][1] == "test_name_3"


def test_csv_exporter_writes_header(tmp_path):  # tmp_path is a pytest fixture

    file_path = tmp_path / "write_header_records.csv"
    file_path.touch()

    test_record = TheTestRecord(
        test_name="test_name",
        start_time=datetime.datetime(2026, 8, 23, 13, 0, 0),
        end_time=datetime.datetime(2026, 8, 23, 13, 0, 30),
        duration=datetime.timedelta(seconds=30),
        measurement=13.5,
        outcome="PASS",
        error=None
    )

    exporter = CSVExporter()
    exporter.export([test_record], file_path)

    with file_path.open(newline="") as csv_file:
        rows = list(csv.reader(csv_file))

    expected_header = [
        "test_id",
        "test_name",
        "start_time",
        "end_time",
        "duration",
        "measurement",
        "outcome",
        "error",
    ]

    assert len(rows) == 2
    assert rows[0] == expected_header
    assert rows.count(expected_header) == 1  # check if there's only one header
    assert rows[1][1] == test_record.test_name


def test_csv_exporter_serializes_record_fields(tmp_path):  # tmp_path is a pytest fixture
    test_record = TheTestRecord(
        test_name="serialization_test",
        start_time=datetime.datetime(2026, 8, 23, 13, 15, 30),
        end_time=datetime.datetime(2026, 8, 23, 13, 15, 31, 500000),
        duration=datetime.timedelta(seconds=1.5),
        measurement=3.25,
        outcome="ERROR",
        error="Device connection failed",
    )

    file_path = tmp_path / "serializes_record_fields.csv"

    exporter = CSVExporter()
    exporter.export([test_record], file_path)

    with file_path.open(newline="") as csv_file:
        rows = list(csv.reader(csv_file))

    assert rows[1][0] == str(test_record.test_id)
    assert rows[1][1] == test_record.test_name
    assert rows[1][2] == test_record.start_time.isoformat()
    assert rows[1][3] == test_record.end_time.isoformat()
    assert rows[1][4] == str(test_record.duration.total_seconds())
    assert rows[1][5] == str(test_record.measurement)
    assert rows[1][6] == test_record.outcome
    assert rows[1][7] == test_record.error


def test_csv_exporter_does_nothing_for_empty_records(tmp_path):  # tmp_path is a pytest fixture
    file_path = tmp_path / "empty_records.csv"

    exporter = CSVExporter()
    exporter.export([], file_path)

    assert not file_path.exists()


def test_csv_exporter_preserves_record_order(tmp_path):  # tmp_path is a pytest fixture
    test_record1 = make_test_record(
        test_name="test_name_1",
        measurement=11.5,
        outcome="PASS",
        error=None,
    )

    test_record2 = make_test_record(
        test_name="test_name_2",
        measurement=12.5,
        outcome="PASS",
        error=None,
    )

    test_record3 = make_test_record(
        test_name="test_name_3",
        measurement=13.5,
        outcome="PASS",
        error=None,
    )

    file_path = tmp_path / "record_order.csv"

    exporter = CSVExporter()
    exporter.export([test_record3, test_record1, test_record2], file_path)

    with file_path.open(newline="") as csv_file:
        rows = list(csv.reader(csv_file))

    assert rows[1][1] == "test_name_3"
    assert rows[2][1] == "test_name_1"
    assert rows[3][1] == "test_name_2"
