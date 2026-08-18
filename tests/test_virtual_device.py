from src.device.virtual_device import VirtualDevice
from src.device.device import DeviceError

import pytest


def test_virtual_device_initial_state():
    virtual_device = VirtualDevice()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False
    assert virtual_device.measurement == 25
    assert virtual_device.connection_failure_enabled is False


def test_virtual_device_connect():
    virtual_device = VirtualDevice()

    virtual_device.connect()

    assert virtual_device.is_connected is True
    assert virtual_device.is_moving is False


def test_virtual_device_move_when_connected():
    virtual_device = VirtualDevice()

    virtual_device.connect()
    virtual_device.move()

    assert virtual_device.is_connected is True
    assert virtual_device.is_moving is True


def test_virtual_device_move_when_disconnected():
    virtual_device = VirtualDevice()

    with pytest.raises(DeviceError):
        virtual_device.move()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False


def test_virtual_device_move_when_already_moving():
    virtual_device = VirtualDevice()

    virtual_device.connect()
    virtual_device.move()

    assert virtual_device.is_moving is True

    virtual_device.move()

    assert virtual_device.is_connected is True
    assert virtual_device.is_moving is True


def test_virtual_device_read_when_connected():
    virtual_device = VirtualDevice()

    virtual_device.connect()
    measurement = virtual_device.read()

    assert measurement == 25


def test_virtual_device_read_when_moving():
    virtual_device = VirtualDevice()

    virtual_device.connect()
    virtual_device.move()
    measurement = virtual_device.read()

    assert measurement == 25
    assert virtual_device.is_moving is True


def test_virtual_device_read_when_disconnected():
    virtual_device = VirtualDevice()

    with pytest.raises(DeviceError):
        virtual_device.read()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False


def test_virtual_device_stop_when_moving():
    virtual_device = VirtualDevice()

    virtual_device.connect()
    virtual_device.move()

    assert virtual_device.is_moving is True

    virtual_device.stop()

    assert virtual_device.is_moving is False


def test_virtual_device_stop_when_already_stopped():
    virtual_device = VirtualDevice()

    virtual_device.connect()

    assert virtual_device.is_connected is True
    assert virtual_device.is_moving is False

    virtual_device.stop()

    assert virtual_device.is_connected is True
    assert virtual_device.is_moving is False


def test_virtual_device_stop_when_disconnected():
    virtual_device = VirtualDevice()

    with pytest.raises(DeviceError):
        virtual_device.stop()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False


def test_virtual_device_disconnect_when_connected():
    virtual_device = VirtualDevice()

    virtual_device.connect()

    assert virtual_device.is_connected is True
    assert virtual_device.is_moving is False

    virtual_device.disconnect()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False


def test_virtual_device_disconnect_when_moving():
    virtual_device = VirtualDevice()

    virtual_device.connect()
    virtual_device.move()

    assert virtual_device.is_connected is True
    assert virtual_device.is_moving is True

    virtual_device.disconnect()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is True


def test_virtual_device_disconnect_when_already_disconnected():
    virtual_device = VirtualDevice()

    virtual_device.disconnect()

    assert virtual_device.is_connected is False
    assert virtual_device.is_moving is False


def test_virtual_device_set_measurement():
    virtual_device = VirtualDevice()

    assert virtual_device.measurement == 25

    virtual_device.set_measurement("hot")

    assert virtual_device.measurement == 35


@pytest.mark.parametrize(
    "temp_level, expectation",
    [("Hot", 35), ("MEDIUM", 25), ("cold", 0)]
)
def test_virtual_device_set_measurement_case_insensitive(temp_level, expectation):
    virtual_device = VirtualDevice()

    virtual_device.set_measurement(temp_level)

    assert virtual_device.measurement == expectation


def test_virtual_device_set_invalid_measurement_preserves_state():
    virtual_device = VirtualDevice()

    assert virtual_device.measurement == 25

    with pytest.raises(DeviceError):
        virtual_device.set_measurement("warm")

    assert virtual_device.measurement == 25


def test_virtual_device_connection_failure():
    virtual_device = VirtualDevice()

    virtual_device.set_connection_failure(True)

    with pytest.raises(DeviceError):
        virtual_device.connect()

    assert virtual_device.is_connected is False


def test_virtual_device_connection_failure_persists():
    virtual_device = VirtualDevice()

    virtual_device.set_connection_failure(True)

    with pytest.raises(DeviceError):
        virtual_device.connect()

    with pytest.raises(DeviceError):
        virtual_device.connect()

    assert virtual_device.is_connected is False


def test_virtual_device_connection_failure_recovery():
    virtual_device = VirtualDevice()

    virtual_device.set_connection_failure(True)

    with pytest.raises(DeviceError):
        virtual_device.connect()

    virtual_device.set_connection_failure(False)

    virtual_device.connect()

    assert virtual_device.is_connected is True
