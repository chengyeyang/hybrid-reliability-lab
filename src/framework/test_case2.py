from src.framework.result import Result
import datetime


class TestCase2:

    def run(self):
        # instantiate result object here so there will be result for each run instead of all runs share the same result
        result = Result()
        result.test_name = self.__class__.__name__
        result.start_time = datetime.datetime.now()

        print("running case 2")

        # ----------------------
        # do some evaluating here
        # ----------------------

        result.end_time = datetime.datetime.now()
        result.duration = result.end_time - result.start_time
        result.passed = True

        return result
