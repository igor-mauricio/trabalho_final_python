from unittest.mock import patch
from Peripherals import FakePeripherals
from controlService import ControlService


def test_shouldTurnOnLamp() -> None:
  peripherals = FakePeripherals()
  controlService = ControlService(peripherals)
  controlService.switchLamp(value=True)
  assert controlService.getLampState() is True

def test_shouldTurnOffLamp() -> None:
  peripherals = FakePeripherals()
  controlService = ControlService(peripherals)
  controlService.switchLamp(False)
  assert controlService.getLampState() is False

def test_shouldSensePresence() -> None:
  peripherals = FakePeripherals()
  controlService = ControlService(peripherals)
  with patch.object(peripherals, 'getPresenceSensor', return_value=False):
    assert controlService.sensePresence() is False
  with patch.object(peripherals, 'getPresenceSensor', return_value=True):
    assert controlService.sensePresence() is True

def test_shouldTurnOnAirConditioner() -> None:
  peripherals = FakePeripherals()
  controlService = ControlService(peripherals)
  controlService.switchAirConditioner(True)
  assert controlService.getAirConditionerState() is True

def test_shouldTurnOffAirConditioner() -> None:
  peripherals = FakePeripherals()
  controlService = ControlService(peripherals)
  controlService.switchAirConditioner(False)
  assert controlService.getAirConditionerState() is False

def test_shouldReadTemperature() -> None:
  peripherals = FakePeripherals()
  controlService = ControlService(peripherals)
  with patch.object(peripherals, 'getTemperature', return_value=25):
    assert controlService.readTemperature() == 25


