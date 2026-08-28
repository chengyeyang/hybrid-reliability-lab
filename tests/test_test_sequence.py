from src.framework.test_sequence import TestSequence as HardwareTestSequence  # to avoid a name start with `Test` to be
# mistaken for test by pytest


import datetime
import pytest

from src.framework.execution_error import ExecutionError
from src.framework.result import Result


class FakeTestCase:
    def __init__(self, result):
        self.result = result
        self.was_run = False

    def run(self):
        self.was_run = True
        return self.result


class FailingFakeTestCase:
    def __init__(self, result):
        self.result = result

    def run(self):
        raise ExecutionError(
            "FakeTestCase",
            self.result,
            Exception("Fake execution failure"),
            datetime.datetime.now(),
            "fake_stage"
        )


class FakeErrorTestCase:
    def __init__(self, execution_error):
        self.execution_error = execution_error
        self.was_run = False

    def run(self):
        self.was_run = True
        raise self.execution_error


def test_sequence_collects_results_from_multiple_cases():
    sequence = HardwareTestSequence()

    case1 = FakeTestCase("result1")
    case2 = FakeTestCase("result2")

    sequence.add(case1)
    sequence.add(case2)

    results = sequence.execute()

    assert results == ["result1", "result2"]


def test_sequence_preserves_error_result_and_stops_when_execution_error_occurs():
    sequence = HardwareTestSequence()

    case1 = FailingFakeTestCase("error_result")
    case2 = FakeTestCase("result2")

    sequence.add(case1)
    sequence.add(case2)

    results = sequence.execute()

    assert results == ["error_result"]
    assert case2.was_run is False


def test_sequence_preserves_error_result_and_stops_remaining_tests():
    pass_result = Result()
    pass_result.outcome = "PASS"

    error_result = Result()
    error_result.outcome = "ERROR"
    error_result.error = "Failed to move hardware"

    third_result = Result()
    third_result.outcome = "PASS"

    execution_error = ExecutionError(
        "TestCase2",
        error_result,
        Exception("Failed to move hardware"),
        datetime.datetime.now(),
        "move",
    )

    case1 = FakeTestCase(pass_result)
    case2 = FakeErrorTestCase(execution_error)
    case3 = FakeTestCase(third_result)

    sequence = HardwareTestSequence()
    sequence.add(case1)
    sequence.add(case2)
    sequence.add(case3)

    results = sequence.execute()

    assert len(results) == 2
    assert results[0].outcome == "PASS"
    assert results[1].outcome == "ERROR"
    assert results[1].error == "Failed to move hardware"
    assert case1.was_run is True
    assert case2.was_run is True
    assert case3.was_run is False
