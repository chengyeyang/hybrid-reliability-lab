from src.framework.test_case import TestCase1 as HardwareTestCase1

import pytest
from src.framework.execution_error import ExecutionError

class FakeDevice:
    def __init__(self, measurement, move_should_fail=False, stop_should_fail=False):
        self.measurement = measurement
        self.move_should_fail = move_should_fail
        self.stop_should_fail = stop_should_fail

    def move(self):
        if self.move_should_fail:
            raise Exception("Failed to move hardware")

    def read(self):
        return self.measurement

    def stop(self):
        if self.stop_should_fail:
            raise Exception("Failed to stop hardware")


def test_testcase_returns_pass_result():
    device = FakeDevice(6.0)
    test_case = HardwareTestCase1(device)

    result = test_case.run()

    assert result.outcome == "PASS"

def test_testcase_returns_fail_result():
    device = FakeDevice(3.0)
    test_case = HardwareTestCase1(device)

    result = test_case.run()

    assert result.outcome == "FAIL"

def test_testcase_raises_execution_error_when_move_fails():
    device = FakeDevice(6.0, move_should_fail=True)
    test_case = HardwareTestCase1(device)

    with pytest.raises(ExecutionError) as exc_info:
        test_case.run()

    assert exc_info.value.stage == "move"
    assert exc_info.value.result.outcome == "ERROR"
    assert str(exc_info.value.original_error) == "Failed to move hardware"


def test_testcase_raises_execution_error_when_cleanup_fails():
    device = FakeDevice(3.0, stop_should_fail=True)
    test_case = HardwareTestCase1(device)

    with pytest.raises(ExecutionError) as exc_info:
        test_case.run()

    assert exc_info.value.stage == "cleanup"
    assert exc_info.value.result.outcome == "FAIL"
    assert str(exc_info.value.original_error) == "Failed to stop hardware"

def test_testcase_preserves_cleanup_error_when_move_and_cleanup_fail():
    device = FakeDevice(
        6.0,
        move_should_fail=True,
        stop_should_fail=True
    )
    test_case = HardwareTestCase1(device)

    with pytest.raises(ExecutionError) as exc_info:
        test_case.run()

    assert exc_info.value.stage == "move"
    assert exc_info.value.result.outcome == "ERROR"
    assert str(exc_info.value.original_error) == "Failed to move hardware"
    assert str(exc_info.value.cleanup_error) == "Failed to stop hardware"
