from infra.proxy.PresenceSensorProxy import FakePresenceSensorProxy
from application.LerSensorPresenca import LerSensorPresenca

def test_deveDetectarQuartoComPessoas():
  presenceSensorProxy = FakePresenceSensorProxy(value=True)
  lerSensorPresenca = LerSensorPresenca(presenceSensorProxy)
  detectado = lerSensorPresenca.execute()
  assert detectado is True

def test_deveDetectarComodoSemPessoas() -> None:
  presenceSensorProxy = FakePresenceSensorProxy(value=False)
  lerSensorPresenca = LerSensorPresenca(presenceSensorProxy)
  detectado = lerSensorPresenca.execute()
  assert detectado is False