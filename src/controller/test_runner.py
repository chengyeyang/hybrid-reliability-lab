from src.communication.communication import Communication
from src.hardware.hardware import Hardware
from src.sensors.sensor import Sensor


class TestRunner:

    def __init__(self):
        self.communication = Communication()
        self.hardware = Hardware()
        self.sensor = Sensor()

    def run(self):
        print("Starting test...")

        self.communication.connect()
        self.hardware.move()
        value = self.sensor.read()
        print(value)
        self.hardware.stop()
        self.communication.disconnect()
