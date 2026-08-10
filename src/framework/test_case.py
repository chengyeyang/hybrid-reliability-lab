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

        try:
            self.communication.connect()
            self.hardware.move()
            result.measurement = self.sensor.read()
            print(f"{result.measurement}")

        except Exception as e:
            result.outcome = "ERROR"
            result.error = str(e)
            print(f"{self.__class__.__name__} test encountered an error: {e}")

        else:
            if result.measurement < 5:
                result.outcome = "FAIL"
            else:
                result.outcome = "PASS"

        finally:
            try:
                self.hardware.stop()
                self.communication.disconnect()

            except Exception:
                pass

            result.end_time = datetime.datetime.now()
            result.duration = result.end_time - result.start_time

        return result
