from __future__ import annotations
from typing import TypedDict

from infra.ArCondicionadoProxy import ArCondicionadoProxy


class SetarArCondicionado:
  def __init__(self, arCondicionadoProxy: ArCondicionadoProxy):
    self.arCondicionadoProxy = arCondicionadoProxy

  def execute(self, input: Input) -> None:
    comando = False
    if input['comando'] == "ligar":
        comando = True
    elif input['comando'] == "desligar":
        comando = False
    else:
       raise ValueError("Comando não suportado")
    self.arCondicionadoProxy.setValue(input['local'], comando)
  
class Input(TypedDict):
  local: str
  comando: str
