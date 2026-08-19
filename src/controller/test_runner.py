class TestRunner:
    def __init__(self, test_sequence, device):
        self.device = device
        self.test_sequence = test_sequence

    def run(self):
        self.device.connect()
        try:
            results = self.test_sequence.execute()
        finally:
            self.device.disconnect()

        return results
