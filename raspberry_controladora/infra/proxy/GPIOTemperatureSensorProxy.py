from abc import ABC, abstractmethod
import RPi.GPIO as GPIO

class TemperatureSensorProxy(ABC):
  @abstractmethod
  def read(room: str): ...

class GPIOTemperatureSensorProxy(TemperatureSensorProxy):
  quartoPin: int
  salaPin: int
  
  def __init__(self, quartoPin, salaPin):
    self.quartoPin = quartoPin
    self.salaPin = salaPin
    GPIO.setup(self.quartoPin, GPIO.IN)
    GPIO.setup(self.salaPin, GPIO.IN)

  def read(self, room: str):
    if room == "quarto":
      return GPIO.input(self.quartoPin)
    if room == "sala":
      return GPIO.input(self.salaPin)
    raise ValueError("Local incorreto")