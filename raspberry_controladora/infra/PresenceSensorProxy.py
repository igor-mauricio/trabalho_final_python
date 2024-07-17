from abc import ABC, abstractmethod


class PresenceSensorProxy(ABC):
  @abstractmethod
  def read() -> bool: ...

class FakePresenceSensorProxy(PresenceSensorProxy):
  def __init__(self, value=True):
    self.value = value

  def read(self) -> bool:
    return self.value