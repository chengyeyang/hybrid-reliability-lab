from src.dashboard.sample_data import records
from src.dashboard.dashboard_helpers import filter_records, format_pass_rate


def test_filter_records_returns_all_records_for_all_filter():
    filtered_records = filter_records(records, "All")
    assert filtered_records == records


def test_filter_records_returns_only_matching_outcomes():
    filtered_records = filter_records(records, "FAIL")
    assert len(filtered_records) == 1
    assert filtered_records[0].outcome == "FAIL"


def test_filter_records_handles_empty_records():
    filtered_records = filter_records([], "PASS")
    assert filtered_records == []


def test_filter_records_returns_empty_when_no_records_match():
    records_without_error = [
        record
        for record in records
        if record.outcome != "ERROR"
    ]
    filtered_records = filter_records(records_without_error, "ERROR")
    assert filtered_records == []


def test_format_pass_rate_returns_na_when_pass_rate_is_none():
    result = format_pass_rate(None)
    assert result == "N/A"


def test_format_pass_rate_returns_zero_percentage_when_pass_rate_is_zero():
    result = format_pass_rate(0)
    assert result == "0.0%"


def test_format_pass_rate_formats_normal_percentage():
    result = format_pass_rate(0.8)
    assert result == "80.0%"


def test_format_pass_rate_returns_full_percentage_when_pass_rate_is_one():
    result = format_pass_rate(1)
    assert result == "100.0%"
