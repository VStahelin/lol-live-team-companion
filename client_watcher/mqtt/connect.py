from paho.mqtt import client as mqtt_client

from client_watcher.configs import BROKER, PORT, USER, PASSWORD, CLIENT_ID


def connect_mqtt():
    def on_connect(client_mqtt, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    print("Creating connection to MQTT Broker...")

    client_id = CLIENT_ID
    client_mqtt = mqtt_client.Client(client_id)
    client_mqtt.username_pw_set(USER, PASSWORD)
    client_mqtt.on_connect = on_connect
    client_mqtt.connect(BROKER, port=PORT)
    return client_mqtt


class Connector:
    client_mqtt = None

    def __init__(self):
        self.client_mqtt = connect_mqtt()
