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

        execution_error = None
        cleanup_error = None
        current_stage = None
        execution_error_time = None
        cleanup_error_time = None

        try:
            current_stage = "move"
            self.device.move()

            current_stage = "read"
            result.measurement = self.device.read()

            print(f"{result.measurement}")

        except Exception as e:  # if ANY step in the 'try' section above fails will then execute this part
            result.outcome = "ERROR"
            result.error = str(e)

            execution_error = e
            execution_error_time = datetime.datetime.now()

        else:
            # this is only a concept, to extract this evaluation section in the future
            if result.measurement < 5:
                result.outcome = "FAIL"
            else:
                result.outcome = "PASS"

        finally:
            try:
                self.device.stop()

            except Exception as e:

                cleanup_error = e
                cleanup_error_time = datetime.datetime.now()

        result.end_time = datetime.datetime.now()
        result.duration = result.end_time - result.start_time

        # These 3 cases below happens only when error happens, whether it's in execution step, cleanup step, or both.
        # All the error information collected above will then be included in executionError and return while raising
        # error.
        if execution_error is not None and cleanup_error is None:  # execution error only
            raise ExecutionError(
                result.test_name,
                result,
                execution_error,
                execution_error_time,
                current_stage
            )

        elif execution_error is None and cleanup_error is not None:  # cleanup stage error only
            raise ExecutionError(
                result.test_name,
                result,
                cleanup_error,
                cleanup_error_time,
                "cleanup"
            )

        elif execution_error is not None and cleanup_error is not None:  # both execution and cleanup errors
            raise ExecutionError(
                result.test_name,
                result,
                execution_error,
                execution_error_time,
                current_stage,
                cleanup_error
                )

        return result  # normal case, no errors at all. The result will be returned here.
