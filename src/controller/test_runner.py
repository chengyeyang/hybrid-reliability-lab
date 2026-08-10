class TestRunner:
    def __init__(self, test_sequence):
        self.test_sequence = test_sequence

    def run(self):
        print("Starting test...")
        self.test_sequence.execute()
