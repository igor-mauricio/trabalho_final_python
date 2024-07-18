import RPi.GPIO as GPIO

from infra.proxy.ArCondicionadoProxy import ArCondicionadoProxy
  
class GPIOArCondicionadoProxy(ArCondicionadoProxy):
  quartoPin: int
  salaPin: int

  def __init__(self, quartoPin, salaPin):
    self.quartoPin = quartoPin
    self.salaPin = salaPin
    GPIO.setup(self.quartoPin, GPIO.OUT)
    GPIO.setup(self.salaPin, GPIO.OUT)
    GPIO.output(self.quartoPin, False)
    GPIO.output(self.salaPin, False)

  def setValue(self, room: str, command: bool) -> None:
    if room == "quarto":
      GPIO.output(self.quartoPin, command)
      return
    if room == "sala":
      GPIO.output(self.salaPin, command)
      return
    raise ValueError(f"Local incorreto:{room}")
  
  def getValue(self, room: str) -> bool:
    if room == "quarto":
      return GPIO.input(self.quartoPin)
    if room == "sala":
      return GPIO.input(self.salaPin)
    raise ValueError(f"Local incorreto:{room}")