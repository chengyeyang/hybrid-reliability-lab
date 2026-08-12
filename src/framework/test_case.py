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

        except Exception as e:
            result.outcome = "ERROR"
            result.error = str(e)

            execution_error = e
            execution_error_time = datetime.datetime.now()

        else:
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

        if execution_error is not None and cleanup_error is None:
            raise ExecutionError(
                result.test_name,
                result,
                execution_error,
                execution_error_time,
                current_stage
            )

        elif execution_error is None and cleanup_error is not None:
            raise ExecutionError(
                result.test_name,
                result,
                cleanup_error,
                cleanup_error_time,
                "cleanup"
            )

        elif execution_error is not None and cleanup_error is not None:
            raise ExecutionError(
                result.test_name,
                result,
                execution_error,
                execution_error_time,
                current_stage,
                cleanup_error
                )

        result.end_time = datetime.datetime.now()
        result.duration = result.end_time - result.start_time

        return result
