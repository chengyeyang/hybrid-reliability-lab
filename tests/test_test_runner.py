from src.controller.test_runner import TestRunner as HardwareTestRunner


class FakeDevice:
    def __init__(self):
        self.connected = False
        self.disconnected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.disconnected = True


class FakeSequence:
    def __init__(self):
        self.executed = False

    def execute(self):
        self.executed = True


def test_runner_executes_sequence_with_device_session():
    device = FakeDevice()
    sequence = FakeSequence()

    runner = HardwareTestRunner(sequence, device)
    runner.run()

    assert device.connected is True
    assert sequence.executed is True
    assert device.disconnected is True
