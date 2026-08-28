from src.device.device import Device, DeviceError


class VirtualDevice(Device):
    def __init__(self):
        self.is_connected = False
        self.is_moving = False
        self.measurement = 25
        self.connection_failure_enabled = False
        self.move_failure_enabled = False
        self.read_failure_enabled = False
        self.stop_failure_enabled = False

    def connect(self):
        if self.connection_failure_enabled:
            raise DeviceError("Fail to connect")
        self.is_connected = True

    def move(self):
        if not self.is_connected:
            raise DeviceError("Device must be connected before moving")

        if self.move_failure_enabled:
            raise DeviceError("Failed to move")

        self.is_moving = True  # this line will only be executed when connected, otherwise, it will have raise
        # DeviceError and leave this method

    def read(self):
        if not self.is_connected:
            raise DeviceError("Device must be connected before reading")

        if self.read_failure_enabled:
            raise DeviceError("Can not read from device")

        return self.measurement  # this line will only be executed when connected, otherwise, it will have raise
        # DeviceError and leave this method

    def stop(self):
        if not self.is_connected:
            raise DeviceError("Device must be connected before stopping")

        if not self.stop_failure_enabled:
            self.is_moving = False
        else:
            raise DeviceError("Fail to stop")

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

    def set_move_failure(self, enabled):
        self.move_failure_enabled = enabled

    def set_read_failure(self, enabled):
        self.read_failure_enabled = enabled

    def set_stop_failure(self, enabled):
        self.stop_failure_enabled = enabled

