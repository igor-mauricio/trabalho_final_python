from infra import TemperatureSensorProxy


class LerSensorTemperatura:
  def __init__(self, temperatureSensorProxy: TemperatureSensorProxy):
    self.temperatureSensorProxy = temperatureSensorProxy

  def execute(self, room: str) -> bool:
    return self.temperatureSensorProxy.read(room)
