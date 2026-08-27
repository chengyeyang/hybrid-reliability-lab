from src.controller.test_runner import TestRunner
from src.framework.test_sequence import TestSequence

from src.framework.test_case import TestCase1
from src.framework.test_case2 import TestCase2

from src.device.virtual_device import VirtualDevice
from src.logger.logger import Logger

from src.export.csv_exporter import CSVExporter
from pathlib import Path
from src.report.report_generator import ReportGenerator


def main():
    device = VirtualDevice()

    test_case = TestCase1(device)
    test_case2 = TestCase2(device)

    test_sequence = TestSequence()
    test_sequence.add(test_case)
    test_sequence.add(test_case2)

    runner = TestRunner(test_sequence, device)
    results = runner.run()

    logger = Logger()

    for result in results:
        logger.log(result)

    records = logger.records

    exporter = CSVExporter()
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)  # Do not raise FileExistsError if the directory already exists
    filepath = output_dir / "test_results.csv"
    exporter.export(records, filepath)

    generator = ReportGenerator()
    report = generator.generate(records)


if __name__ == '__main__':
    main()
