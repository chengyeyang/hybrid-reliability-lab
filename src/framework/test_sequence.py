from src.framework.execution_error import ExecutionError


class TestSequence:

    def __init__(self):
        self.test_cases = []
        self.test_results = []

    def add(self, test_case):
        self.test_cases.append(test_case)

    def execute(self):
        for case in self.test_cases:
            # run case and then append its test result to test_result list
            try:
                result = case.run()
                self.test_results.append(result)

            except ExecutionError as e:
                self.test_results.append(e.result)
                raise  # we want to keep the original traceback so use 'raise' instead of 'raise e'

        print(self.test_results)
