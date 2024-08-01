from dataclasses import dataclass
from Peripherals import Peripherals
import RPi.GPIO as GPIO

@dataclass
class GPIOPeripherals(Peripherals):
  lampPin: int
  airConditionerPin: int
  presenceSensorPin: int
  temperatureSensorPin: int

  def __post_init__(self) -> None:
    GPIO.setup(self.lampPin, GPIO.OUT)
    GPIO.setup(self.airConditionerPin, GPIO.OUT)
    GPIO.setup(self.presenceSensorPin, GPIO.IN)
    GPIO.setup(self.temperatureSensorPin, GPIO.IN)
    GPIO.output(self.lampPin, False)
    GPIO.output(self.airConditionerPin, False)

  def getLamp(self) -> bool:
    return GPIO.input(self.lampPin)

  def setLamp(self, value: bool) -> None:
    GPIO.output(self.lampPin, value)

  def getPresenceSensor(self) -> bool:
    return GPIO.input(self.presenceSensorPin)

  def setAirConditioner(self, value: bool) -> None:
    GPIO.output(self.airConditionerPin, value)

  def getAirConditioner(self) -> bool:
    return GPIO.input(self.airConditionerPin)

  def getTemperature(self) -> float:
    try:
      with open("/sys/bus/w1/devices/10-000802824e58/w1_slave") as temperatureSensorFile:
        text = temperatureSensorFile.read()
        if "YES" not in text.split("\n")[0]:
            raise ValueError("Invalid temperature sensor data")
        
        temperature_data = text.split("\n")[1].split(" ")[9]
        temperature = float(temperature_data[2:]) / 1000
        return temperature
    except (FileNotFoundError, IndexError, ValueError) as e:
      print(f"Error reading temperature sensor: {e}")
      return float('nan')

    