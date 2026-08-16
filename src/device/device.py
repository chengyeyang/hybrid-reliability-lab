from abc import ABC, abstractmethod


class DeviceError(Exception):
    pass


class Device(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
