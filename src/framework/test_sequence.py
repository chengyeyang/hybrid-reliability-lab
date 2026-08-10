class TestSequence:

    def __init__(self):
        self.test_cases = []

    def add(self, test_case):
        self.test_cases.append(test_case)

    def execute(self):
        for case in self.test_cases:
            case.run()
