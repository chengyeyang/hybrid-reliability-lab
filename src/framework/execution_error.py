class ExecutionError(Exception):
    def __init__(self, test_name, result, original_error, timestamp, stage):
        self.test_name = test_name
        self.result = result
        self.original_error = original_error
        self.timestamp = timestamp
        self.stage = stage

        message = (
            f"{self.original_error} occurred during {self.stage} "
            f"of {self.test_name} at {self.timestamp}"
        )

        super().__init__(message)
