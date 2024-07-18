import RPi.GPIO as GPIO

from infra.proxy.PresenceSensorProxy import PresenceSensorProxy

  
class GPIOPresenceSensorProxy(PresenceSensorProxy):

  def __init__(self, pin: int):
    self.pin = pin
    GPIO.setup(self.pin, GPIO.IN)
    
  def read(self) -> bool:
    return GPIO.input(self.pin) == GPIO.HIGH