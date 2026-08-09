class TestRunner:
    def __init__(self, case_to_execute):
        self.testcase = case_to_execute

    def run(self):
        print("Starting test...")
        self.testcase.run()
