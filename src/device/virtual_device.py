from src.device.device import Device, DeviceError


class VirtualDevice(Device):
    def __init__(self):
        self.is_connected = False
        self.is_moving = False
        self.measurement = 25
        self.connection_failure_enabled = False

    def connect(self):
        if self.connection_failure_enabled:
            raise DeviceError("Fail to connect")
        self.is_connected = True

    def move(self):
        if not self.is_connected:
            raise DeviceError("Device must be connected before moving")

        self.is_moving = True  # this line will only be executed when connected, otherwise, it will have raise
        # DeviceError and leave this method

    def read(self):
        if not self.is_connected:
            raise DeviceError("Device must be connected before reading")

        return self.measurement  # this line will only be executed when connected, otherwise, it will have raise
        # DeviceError and leave this method

    def stop(self):
        if not self.is_connected:
            raise DeviceError("Device must be connected before stopping")

        self.is_moving = False

    def disconnect(self):
        self.is_connected = False

    def set_measurement(self, temp_level):
        condition = temp_level.lower()
        if condition == "hot":
            self.measurement = 35
        elif condition == "medium":
            self.measurement = 25
        elif condition == "cold":
            self.measurement = 0
        else:
            raise DeviceError("Wrong temperature level")

    def set_connection_failure(self, enabled):
        self.connection_failure_enabled = enabled
