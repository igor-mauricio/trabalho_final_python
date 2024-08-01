import os
from flask import Flask, render_template # type: ignore
from flask_socketio import SocketIO, emit # type: ignore
import paho.mqtt.client as mqtt # type: ignore

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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*",)
client = mqtt.Client() 

@app.route("/")
def hello():
	return render_template('index.html')


@socketio.on('airConditionerSwitch')
def handleAirConditioner(message):
    # assert isinstance(message, bool)
    print('received message: ', message)
    client.publish(TOPICS['air_conditioner'], message)

@socketio.on('lampSwitch')
def handleLamp(message):
    # assert isinstance(message, bool)
    print('received message: ', message)
    client.publish(TOPICS['lamp'], message)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for topic in TOPICS.values():
        client.subscribe(topic)

def lampCallback(client, userdata, message):
    lampEnabled = message.payload.decode()
    print('lampCallback', lampEnabled)
    assert isinstance(lampEnabled, bool)
    emit('lamp', lampEnabled)

def airConditionerCallback(client, userdata, message):
    airConditionerEnabled = message.payload.decode()
    print('airConditionerCallback', airConditionerEnabled)
    assert isinstance(airConditionerEnabled, bool)
    emit('airConditioner', airConditionerEnabled)

def temperatureCallback(client, userdata, message):
    temperature = message.payload.decode()
    print('temperatureCallback', temperature)
    assert isinstance(temperature, float)
    emit('temperatureRequest', temperature)

def presenceSensorCallback(client, userdata, message):
    presence = message.payload.decode()
    print('presenceSensorCallback', presence)
    assert isinstance(presence, bool)
    emit('presenceSensorRequest', presence)
client.on_connect = on_connect

client.message_callback_add(TOPICS['lamp'], lampCallback)
client.message_callback_add(TOPICS['air_conditioner'], airConditionerCallback)
client.message_callback_add(TOPICS['temperatureResponse'], temperatureCallback)
client.message_callback_add(TOPICS['presenceSensorResponse'], presenceSensorCallback)
client.connect(BROKER, PORT)
if __name__ == "__main__":
    socketio.run(app, debug=True, port=3001, host='0.0.0.0', allow_unsafe_werkzeug=True)