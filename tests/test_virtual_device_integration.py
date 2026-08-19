from src.device.virtual_device import VirtualDevice
from src.framework.test_case import TestCase1 as VirtualTestCase1
from src.framework.test_sequence import TestSequence as VirtualTestSequence
from src.controller.test_runner import TestRunner as VirtualTestRunner


def test_runner_executes_with_virtual_device():
    virtual_device = VirtualDevice()
    test_case = VirtualTestCase1(virtual_device)

    sequence = VirtualTestSequence()
    sequence.add(test_case)

    runner = VirtualTestRunner(sequence, virtual_device)
    test_results = runner.run()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False
    assert len(test_results) == 1

    # Checking the Result verifies that the measurement returned by the device actually flowed through TestCase
    # execution, rather than only inspecting the VirtualDevice's internal measurement state.
    result = test_results[0]
    assert result.measurement == 25
    assert result.outcome == "PASS"


def test_virtual_device_execution_is_repeatable():
    virtual_device = VirtualDevice()
    test_case = VirtualTestCase1(virtual_device)

    sequence = VirtualTestSequence()
    sequence.add(test_case)

    runner = VirtualTestRunner(sequence, virtual_device)
    test_result1 = runner.run()  # first run
    test_result2 = runner.run()  # second run

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False
    assert len(test_result1) == 1
    assert len(test_result2) == 1

    assert test_result1[0].measurement == test_result2[0].measurement
    assert test_result1[0].outcome == test_result2[0].outcome
    assert test_result1[0] is not test_result2[0]


def test_runner_returns_fail_result_with_cold_virtual_device():
    virtual_device = VirtualDevice()
    virtual_device.set_measurement("cold")

    test_case = VirtualTestCase1(virtual_device)

    sequence = VirtualTestSequence()
    sequence.add(test_case)

    runner = VirtualTestRunner(sequence, virtual_device)
    test_results = runner.run()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False
    assert test_results[0].measurement == 0
    assert test_results[0].outcome == "FAIL"


def test_runner_executes_multiple_cases_with_virtual_device():
    virtual_device = VirtualDevice()

    test_case1 = VirtualTestCase1(virtual_device)
    test_case2 = VirtualTestCase1(virtual_device)

    sequence = VirtualTestSequence()
    sequence.add(test_case1)
    sequence.add(test_case2)

    runner = VirtualTestRunner(sequence, virtual_device)
    test_results = runner.run()

    assert len(test_results) == 2
    assert test_results[0].measurement == 25
    assert test_results[1].measurement == 25
    assert test_results[0].outcome == "PASS"
    assert test_results[1].outcome == "PASS"
    assert test_results[0] is not test_results[1]
    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False
