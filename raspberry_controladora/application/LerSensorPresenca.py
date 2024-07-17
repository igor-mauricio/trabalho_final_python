

from infra.proxy.PresenceSensorProxy import PresenceSensorProxy


class LerSensorPresenca:
  def __init__(self, presenceSensorProxy: PresenceSensorProxy) -> None:
    self.presenceSensorProxy = presenceSensorProxy

  def execute(self) -> bool:
    return self.presenceSensorProxy.read()
