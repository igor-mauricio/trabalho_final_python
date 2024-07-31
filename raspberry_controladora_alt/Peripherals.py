from abc import ABC, abstractmethod


class Peripherals(ABC):
  @abstractmethod
  def getLamp(self) -> bool:...
  
  @abstractmethod
  def setLamp(self, value: bool) -> None:...
  
  @abstractmethod
  def getPresenceSensor(self) -> bool:...
  
  @abstractmethod
  def setAirConditioner(self, value: bool) -> None:...
  
  @abstractmethod
  def getAirConditioner(self) -> bool:...

  @abstractmethod
  def getTemperature(self) -> float:...


class FakePeripherals(Peripherals):
  lamp: bool
  presence: bool
  airConditioner: bool
  temperature: float

  def __init__(self):
    self.lamp = False
    self.presence = False
    self.airConditioner = False
    self.temperature = 0.0

  def getLamp(self) -> bool:
    return self.lamp

  def setLamp(self, value: bool) -> None:
    self.lamp = value

  def getPresenceSensor(self) -> bool:
    return self.presence
  
  def setAirConditioner(self, value: bool) -> None:
    self.airConditioner = value
  
  def getAirConditioner(self) -> bool:
    return self.airConditioner
  
  def getTemperature(self) -> float:
    return self.temperature
