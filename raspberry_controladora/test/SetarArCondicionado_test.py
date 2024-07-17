import pytest
from application.SetarArCondicionado import SetarArCondicionado
from infra.proxy.ArCondicionadoProxy import FakeArCondicionadoProxy


def test_deveLigarArCondicionadoDoQuarto() -> None:
  arCondicionadoProxy = FakeArCondicionadoProxy()
  setarArCondicionado = SetarArCondicionado(arCondicionadoProxy)
  setarArCondicionado.execute({
    "local": "quarto",
    "comando":"ligar"
  })
  assert arCondicionadoProxy.getValue("quarto") is True

def test_deveLigarArCondicionadoDaSala() -> None:
  arCondicionadoProxy = FakeArCondicionadoProxy()
  setarArCondicionado = SetarArCondicionado(arCondicionadoProxy)
  setarArCondicionado.execute({
    "local": "sala",
    "comando":"ligar"
  })
  assert arCondicionadoProxy.getValue("sala") is True

def test_deveLigarEDesligarArCondicionadoDaSala() -> None:
  arCondicionadoProxy = FakeArCondicionadoProxy()
  setarArCondicionado = SetarArCondicionado(arCondicionadoProxy)
  setarArCondicionado.execute({
    "local": "sala",
    "comando":"ligar"
  })
  assert arCondicionadoProxy.getValue("sala") is True
  setarArCondicionado.execute({
    "local": "sala",
    "comando":"desligar"
  })
  assert arCondicionadoProxy.getValue("sala") is False

def test_deveDarErroComComandoIncorreto() -> None:
  arCondicionadoProxy = FakeArCondicionadoProxy()
  setarArCondicionado = SetarArCondicionado(arCondicionadoProxy)
  with pytest.raises(ValueError):
    setarArCondicionado.execute({
      "local": "sala",
      "comando":"religar"
    })