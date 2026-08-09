from src.communication.communication import Communication
from src.hardware.hardware import Hardware
from src.sensors.sensor import Sensor


class TestCase:

    def __init__(self):
        self.communication = Communication()
        self.hardware = Hardware()
        self.sensor = Sensor()

    def run(self):
        self.communication.connect()
        self.hardware.move()
        value = self.sensor.read()
        print(value)
        self.hardware.stop()
        self.communication.disconnect()
