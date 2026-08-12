from src.framework.result import Result
import datetime


class TestCase2:

    def __init__(self, device):
        self.device = device

    def run(self):
        # instantiate result object here so there will be result for each run instead of all runs share the same result
        result = Result()
        result.test_name = self.__class__.__name__
        result.start_time = datetime.datetime.now()

        try:
            print("running case 2")

            # do some evaluating here. To be updated
            if False:
                result.outcome = "FAIL"

        except Exception as e:
            result.outcome = "ERROR"
            result.error = str(e)
            print(f"{self.__class__.__name__} test encountered an error: {e}")

        else:
            result.outcome = "PASS"

        finally:
            result.end_time = datetime.datetime.now()
            result.duration = result.end_time - result.start_time

        return result
