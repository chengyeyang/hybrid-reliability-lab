class Logger:

    def __init__(self):
        self.records = []

    def log(self, result):
        self.records.append({
            "test_name": result.test_name,
            "start_time": result.start_time,
            "end_time": result.end_time,
            "duration": result.duration,
            "measurement": result.measurement,
            "outcome": result.outcome,
            "error": result.error
        })

