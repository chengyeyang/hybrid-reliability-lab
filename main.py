from src.controller.test_runner import TestRunner
from src.framework.test_sequence import TestSequence

from src.framework.test_case import TestCase1
from src.framework.test_case2 import TestCase2

from src.communication.communication import Communication
from src.hardware.hardware import Hardware
from src.sensors.sensor import Sensor
from src.device.device import Device


def main():
    communication = Communication()
    hardware = Hardware()
    sensor = Sensor()
    device = Device(communication, hardware, sensor)

    test_case = TestCase1(device)
    test_case2 = TestCase2(device)

    test_sequence = TestSequence()
    test_sequence.add(test_case)
    test_sequence.add(test_case2)

    runner = TestRunner(test_sequence, device)
    runner.run()


if __name__ == '__main__':
    main()
