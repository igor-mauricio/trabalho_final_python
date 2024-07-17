from abc import ABC, abstractmethod


class LampProxy(ABC):
  @abstractmethod
  def setValue(self, command: bool): ...
  
  @abstractmethod
  def getValue(self) -> bool: ...

class FakeLampProxy(LampProxy):
  def __init__(self):
    self.value = False

  def setValue(self, enabled: bool) -> None:
    self.value = enabled
  
  def getValue(self) -> bool:
    return self.value