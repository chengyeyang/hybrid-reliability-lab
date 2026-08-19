from src.framework.execution_error import ExecutionError


class TestSequence:

    def __init__(self):
        self.test_cases = []

    def add(self, test_case):
        self.test_cases.append(test_case)

    def execute(self):
        test_results = []
        for case in self.test_cases:
            result = case.run()
            test_results.append(result)

        return test_results
