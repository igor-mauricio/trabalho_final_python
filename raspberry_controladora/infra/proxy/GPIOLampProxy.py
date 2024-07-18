import RPi.GPIO as GPIO

from infra.proxy.LampProxy import LampProxy

class GPIOLampProxy(LampProxy):
  pin: int

  def __init__(self, pin: int):
    self.pin = pin
    GPIO.setup(self.pin, GPIO.OUT)
    GPIO.output(self.pin, False)

  def setValue(self, command: bool) -> None:
    GPIO.output(self.pin, command)

  def getValue(self) -> bool:
    return GPIO.input(self.pin)

