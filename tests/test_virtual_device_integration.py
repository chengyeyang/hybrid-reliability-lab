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
    runner.run()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False
    assert len(sequence.test_results) == 1

    # virtual_device.read() only return 0 currently no matter what, so asserting virtual_device.measurement == 0 can
    # not be sure test_case really calls virtual_device.read() in the flow. Hence, utilizing test_result[0] to confirm
    # indirectly
    result = sequence.test_results[0]
    assert result.measurement == 25
    assert result.outcome == "PASS"


def test_virtual_device_execution_is_repeatable():
    virtual_device = VirtualDevice()
    test_case = VirtualTestCase1(virtual_device)

    sequence = VirtualTestSequence()
    sequence.add(test_case)

    runner = VirtualTestRunner(sequence, virtual_device)
    runner.run()  # first run
    runner.run()  # second run

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False
    assert len(sequence.test_results) == 2

    assert sequence.test_results[0].measurement == sequence.test_results[1].measurement
    assert sequence.test_results[0].outcome == sequence.test_results[1].outcome
    assert sequence.test_results[0] is not sequence.test_results[1]


