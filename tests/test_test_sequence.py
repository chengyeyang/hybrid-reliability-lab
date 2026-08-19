from src.framework.test_sequence import TestSequence as HardwareTestSequence  # to avoid a name start with `Test` to be
# mistaken for test by pytest


import datetime
import pytest

from src.framework.execution_error import ExecutionError


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


def test_sequence_collects_results_from_multiple_cases():
    sequence = HardwareTestSequence()

    case1 = FakeTestCase("result1")
    case2 = FakeTestCase("result2")

    sequence.add(case1)
    sequence.add(case2)

    results = sequence.execute()

    assert results == ["result1", "result2"]


def test_sequence_stops_when_execution_error_occurs():
    sequence = HardwareTestSequence()

    case1 = FailingFakeTestCase("error_result")
    case2 = FakeTestCase("result2")

    sequence.add(case1)
    sequence.add(case2)

    # in this scenario, there will be ExecutionError, so we utilize pytest.raise() method to catch it
    with pytest.raises(ExecutionError) as exc_info:
        sequence.execute()

    assert exc_info.value.result == "error_result"
    assert case2.was_run is False
