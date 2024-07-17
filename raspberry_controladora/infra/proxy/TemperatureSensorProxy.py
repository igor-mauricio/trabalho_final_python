from abc import ABC, abstractmethod


class TemperatureSensorProxy(ABC):
  @abstractmethod
  def read(room: str): ...

class FakeTemperatureSensorProxy(TemperatureSensorProxy):
  def __init__(self, quartoValue=20, salaValue=30):
    self.quartoValue = quartoValue
    self.salaValue = salaValue

  def read(self, room: str):
    if room == "quarto":
      return self.quartoValue
    if room == "sala":
      return self.salaValue
    raise ValueError("Local incorreto")