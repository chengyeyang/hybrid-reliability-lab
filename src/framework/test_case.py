from src.framework.result import Result
from src.framework.execution_error import ExecutionError

import datetime


class TestCase1:

    def __init__(self, device):
        self.device = device

    def run(self):
        # instantiate result object here so there will be result for each run instead of all runs share the same result
        result = Result()
        result.test_name = self.__class__.__name__
        result.start_time = datetime.datetime.now()

        try:
            self.device.move()
            result.measurement = self.device.read()

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
                self.device.stop()

            except Exception as e:
                raise ExecutionError(result.test_name, result, e, datetime.datetime.now(), "cleanup")

            result.end_time = datetime.datetime.now()
            result.duration = result.end_time - result.start_time

        return result
