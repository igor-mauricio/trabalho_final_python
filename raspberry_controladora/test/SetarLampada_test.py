import pytest
from application.SetarLampada import SetarLampada
from infra.proxy.LampProxy import FakeLampProxy


def test_deveLigarLampada() -> None:
  lampProxy = FakeLampProxy()
  setarLampada = SetarLampada(lampProxy)
  setarLampada.execute({
    "comando":"ligar"
  })
  assert lampProxy.getValue() is True

def test_deveLigarEDesligarLampDaSala() -> None:
  lampProxy = FakeLampProxy()
  setarLampada = SetarLampada(lampProxy)
  setarLampada.execute({
    "comando":"ligar"
  })
  assert lampProxy.getValue() is True
  setarLampada.execute({
    "comando":"desligar"
  })
  assert lampProxy.getValue() is False

def test_deveDarErroComComandoIncorreto() -> None:
  lampProxy = FakeLampProxy()
  setarLampada = SetarLampada(lampProxy)
  with pytest.raises(ValueError):
    setarLampada.execute({
      "comando":"religar"
    })