class TestReport:
    def __init__(
        self,
        total_tests: int,
        pass_count: int,
        fail_count: int,
        error_count: int,
        pass_rate: float | None,
        measurement_count: int,
        minimum_measurement: int | float | None,
        maximum_measurement: int | float | None,
        average_measurement: float | None,
        failure_details: list[dict]
    ):
        self.total_tests = total_tests
        self.pass_count = pass_count
        self.fail_count = fail_count
        self.error_count = error_count
        self.pass_rate = pass_rate
        self.measurement_count = measurement_count
        self.minimum_measurement = minimum_measurement
        self.maximum_measurement = maximum_measurement
        self.average_measurement = average_measurement
        self.failure_details = failure_details
