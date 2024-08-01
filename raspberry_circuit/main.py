import os
import paho.mqtt.client as mqtt
from Peripherals import FakePeripherals
from ControlService import ControlService

peripherals = FakePeripherals()
control_service = ControlService(peripherals)
client = mqtt.Client()

BROKER = os.getenv('MQTT_BROKER', 'localhost')
PORT = int(os.getenv('PORT', 1883))

TOPICS = {
    'lamp': 'home/lamp',
    'air_conditioner': 'home/air_conditioner',
    'presenceSensorRequest': 'home/presence',
    'presenceSensorResponse': 'home/presence/response',
    'temperatureRequest': 'home/temperature',
    'temperatureResponse': 'home/temperature/response'
}

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for topic in TOPICS.values():
        client.subscribe(topic)

def lampCallback(client, userdata, message):
    value = message.payload.decode()
    print('lampCallback', value)
    assert isinstance(value, bool)
    control_service.switchLamp(value)

def airConditionerCallback(client, userdata, message):
    value = message.payload.decode()
    print('airConditionerCallback', value)
    assert isinstance(value, bool)
    control_service.switchAirConditioner(value)

def temperatureRequestCallback(client, userdata, message):
    temperature = control_service.readTemperature()
    print('temperatureRequestCallback', temperature)
    client.publish(TOPICS['temperatureResponse'], temperature)

def presenceSensorRequestCallback(client, userdata, message):
    presence = control_service.sensePresence()
    print('presenceSensorRequestCallback', presence)
    client.publish(TOPICS['presenceSensorResponse'], presence)


client.on_connect = on_connect
client.message_callback_add(TOPICS['lamp'], lampCallback)
client.message_callback_add(TOPICS['air_conditioner'], airConditionerCallback)
client.message_callback_add(TOPICS['temperatureRequest'], temperatureRequestCallback)
client.message_callback_add(TOPICS['presenceSensorRequest'], presenceSensorRequestCallback)
client.connect(BROKER, PORT)
client.loop_forever()