from dataclasses import dataclass
from Peripherals import Peripherals


@dataclass
class ControlService:
    peripherals: Peripherals

    def switchLamp(self, value: bool) -> None:
        self.peripherals.setLamp(value)

    def getLampState(self) -> bool:
        return self.peripherals.getLamp()

    def sensePresence(self) -> bool:
        return self.peripherals.getPresenceSensor()
    
    def switchAirConditioner(self, value: bool) -> None:
        self.peripherals.setAirConditioner(value)
        
    def getAirConditionerState(self) -> bool:
        return self.peripherals.getAirConditioner()
    
    def readTemperature(self) -> float:
        return self.peripherals.getTemperature()