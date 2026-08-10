class TestSequence:

    def __init__(self):
        self.test_cases = []
        self.test_results = []

    def add(self, test_case):
        self.test_cases.append(test_case)

    def execute(self):
        for case in self.test_cases:
            # run case and then append its test result to test_result list
            self.test_results.append(case.run())

        print(self.test_results)
