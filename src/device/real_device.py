from src.device.device import Device


class RealDevice(Device):
    def __init__(self, communication, hardware, sensor):
        self.communication = communication
        self.hardware = hardware
        self.sensor = sensor

    def connect(self):
        self.communication.connect()

    def move(self):
        self.hardware.move()

    def read(self):
        return self.sensor.read()

    def stop(self):
        self.hardware.stop()

    def disconnect(self):
        self.communication.disconnect()
