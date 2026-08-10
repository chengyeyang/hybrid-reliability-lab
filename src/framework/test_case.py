from src.communication.communication import Communication
from src.hardware.hardware import Hardware
from src.sensors.sensor import Sensor
from src.framework.result import Result

import datetime


class TestCase1:

    def __init__(self):
        self.communication = Communication()
        self.hardware = Hardware()
        self.sensor = Sensor()

    def run(self):
        # instantiate result object here so there will be result for each run instead of all runs share the same result
        result = Result()
        result.test_name = self.__class__.__name__
        result.start_time = datetime.datetime.now()

        self.communication.connect()
        self.hardware.move()
        value = self.sensor.read()
        print(value)
        self.hardware.stop()
        self.communication.disconnect()

        # ----------------------
        # do some evaluating here
        # ----------------------

        result.end_time = datetime.datetime.now()
        result.duration = result.end_time - result.start_time
        result.passed = True

        return result
