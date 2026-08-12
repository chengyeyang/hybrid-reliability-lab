class ExecutionError(Exception):
    def __init__(self, test_name, result, original_error, timestamp, stage, cleanup_error=None):
        self.test_name = test_name
        self.result = result
        self.original_error = original_error
        self.timestamp = timestamp
        self.stage = stage
        self.cleanup_error = cleanup_error

        message = (
            f"{self.original_error} occurred during {self.stage} "
            f"of {self.test_name} at {self.timestamp}"
        )

        super().__init__(message)
