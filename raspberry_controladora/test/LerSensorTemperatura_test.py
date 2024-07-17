import pytest

from application.LerSensorTemperatura import LerSensorTemperatura
from infra.TemperatureSensorProxy import FakeTemperatureSensorProxy


def test_deveVerificarQuartoComTemperatura42Graus():
  temperatureSensorProxy = FakeTemperatureSensorProxy(quartoValue=42)
  lerSensorTemperatura = LerSensorTemperatura(temperatureSensorProxy)
  output = lerSensorTemperatura.execute("quarto")
  assert output == 42

def test_deveVerificarSalaComTemperatura24Graus():
  temperatureSensorProxy = FakeTemperatureSensorProxy(salaValue=24)
  lerSensorTemperatura = LerSensorTemperatura(temperatureSensorProxy)
  output = lerSensorTemperatura.execute("sala")
  assert output == 24

def test_deveDarErroQuandoSolicitaLocalQueNaoExiste():
  temperatureSensorProxy = FakeTemperatureSensorProxy(salaValue=24)
  lerSensorTemperatura = LerSensorTemperatura(temperatureSensorProxy)
  with pytest.raises(ValueError, match="Local incorreto"):
    lerSensorTemperatura.execute("banheiro")