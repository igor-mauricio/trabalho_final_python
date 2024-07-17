from abc import ABC, abstractmethod


class ArCondicionadoProxy(ABC):
  @abstractmethod
  def setValue(self, room: str, command: bool): ...

  @abstractmethod
  def getValue(self, room: str) -> bool: ...

class FakeArCondicionadoProxy(ArCondicionadoProxy):
  def __init__(self):
    self.quartoValue = False
    self.salaValue = False

  def setValue(self, room: str, command: bool) -> None:
    if room == "quarto":
      self.quartoValue = command
      return
    if room == "sala":
      self.salaValue = command
      return
    raise ValueError(f"Local incorreto:{room}")
  
  def getValue(self, room: str) -> bool:
    if room == "quarto":
      return self.quartoValue
    if room == "sala":
      return self.salaValue
    raise ValueError(f"Local incorreto:{room}")