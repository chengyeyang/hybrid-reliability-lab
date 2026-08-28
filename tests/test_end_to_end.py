from src.device.virtual_device import VirtualDevice
from src.framework.test_case import TestCase1
from src.framework.test_sequence import TestSequence
from src.controller.test_runner import TestRunner
from src.logger.logger import Logger
from src.export.csv_exporter import CSVExporter
from src.report.report_generator import ReportGenerator
from src.data.csv_reader import CSVReader


def test_end_to_end_pass_flow(tmp_path):
    device = VirtualDevice()
    device.set_measurement("hot")

    test_case = TestCase1(device)

    test_sequence = TestSequence()
    test_sequence.add(test_case)

    runner = TestRunner(test_sequence, device)
    results = runner.run()

    logger = Logger()

    for result in results:
        logger.log(result)

    records = logger.records

    exporter = CSVExporter()
    filepath = tmp_path / "test_results.csv"
    exporter.export(records, filepath)

    reader = CSVReader()
    loaded_records = reader.read(filepath)

    generator = ReportGenerator()
    report = generator.generate(loaded_records)

    assert results[0].outcome == "PASS"
    assert records[0].outcome == "PASS"
    assert report.pass_count == 1
    assert report.fail_count == 0


def test_end_to_end_fail_flow(tmp_path):
    device = VirtualDevice()
    device.set_measurement("cold")

    test_case = TestCase1(device)

    test_sequence = TestSequence()
    test_sequence.add(test_case)

    runner = TestRunner(test_sequence, device)
    results = runner.run()

    logger = Logger()

    for result in results:
        logger.log(result)

    records = logger.records

    exporter = CSVExporter()
    filepath = tmp_path / "test_results.csv"
    exporter.export(records, filepath)

    reader = CSVReader()
    loaded_records = reader.read(filepath)

    generator = ReportGenerator()
    report = generator.generate(loaded_records)

    assert results[0].outcome == "FAIL"
    assert records[0].outcome == "FAIL"
    assert report.pass_count == 0
    assert report.fail_count == 1


def test_end_to_end_error_flow(tmp_path):
    device = VirtualDevice()
    device.set_move_failure(True)

    test_case1 = TestCase1(device)
    test_case2 = TestCase1(device)

    test_sequence = TestSequence()
    test_sequence.add(test_case1)
    test_sequence.add(test_case2)

    runner = TestRunner(test_sequence, device)
    results = runner.run()

    logger = Logger()

    for result in results:
        logger.log(result)

    records = logger.records

    exporter = CSVExporter()
    filepath = tmp_path / "test_results.csv"
    exporter.export(records, filepath)

    reader = CSVReader()
    loaded_records = reader.read(filepath)

    generator = ReportGenerator()
    report = generator.generate(loaded_records)

    assert len(results) == 1
    assert results[0].outcome == "ERROR"
    assert results[0].error == "Failed to move"
    assert results[0].cleanup_error is None

    assert loaded_records[0].outcome == "ERROR"
    assert loaded_records[0].error == "Failed to move"

    assert report.error_count == 1
    assert report.pass_count == 0
    assert report.fail_count == 0
