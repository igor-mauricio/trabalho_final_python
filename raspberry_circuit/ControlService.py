from dataclasses import dataclass
from Peripherals import Peripherals


@dataclass
class ControlService:
    peripherals: Peripherals

    def switchLamp(self, value: bool) -> None:
        self.peripherals.setLamp(value)

    def sensePresence(self) -> bool:
        return self.peripherals.getPresenceSensor()
    
    def switchAirConditioner(self, value: bool) -> None:
        self.peripherals.setAirConditioner(value)
    
    def readTemperature(self) -> float:
        return self.peripherals.getTemperature()