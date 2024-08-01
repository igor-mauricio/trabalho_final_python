from unittest.mock import patch

from pytest import fixture
from Peripherals import FakePeripherals, Peripherals
from ControlService import ControlService

@fixture
def peripherals() -> Peripherals:
  return FakePeripherals()

@fixture
def controlService(peripherals) -> ControlService:
  return ControlService(peripherals)

def test_shouldTurnOnLamp(controlService, peripherals) -> None:
  controlService.switchLamp(value=True)
  assert peripherals.getLamp() is True
  
def test_shouldTurnOffLamp(controlService, peripherals) -> None:
  controlService.switchLamp(False)
  assert peripherals.getLamp() is False

def test_shouldSensePresence(controlService) -> None:
  with patch.object(controlService.peripherals, 'getPresenceSensor', return_value=False):
    assert controlService.sensePresence() is False
  with patch.object(controlService.peripherals, 'getPresenceSensor', return_value=True):
    assert controlService.sensePresence() is True

def test_shouldTurnOnAirConditioner(controlService, peripherals) -> None:
  controlService.switchAirConditioner(True)
  assert peripherals.getAirConditioner() is True

def test_shouldTurnOffAirConditioner(controlService, peripherals) -> None:
  controlService.switchAirConditioner(False)
  assert peripherals.getAirConditioner() is False

def test_shouldReadTemperature(controlService) -> None:
  with patch.object(controlService.peripherals, 'getTemperature', return_value=25):
    assert controlService.readTemperature() == 25