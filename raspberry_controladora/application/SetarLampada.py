from __future__ import annotations
from typing import TypedDict

from infra.proxy.LampProxy import LampProxy


class SetarLampada:
  def __init__(self, lampProxy: LampProxy):
    self.lampProxy = lampProxy

  def execute(self, input: Input) -> None:
    comando = False
    if input['comando'] == "ligar":
        comando = True
    elif input['comando'] == "desligar":
        comando = False
    else:
       raise ValueError("Comando não suportado")
    self.lampProxy.setValue(comando)
  
class Input(TypedDict):
  comando: str
