from paho.mqtt import client as mqtt_client

import settings


def connect_mqtt():
    def on_connect(client_mqtt, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    print("Creating connection to MQTT Broker...")

    client_id = settings.CLIENT_ID
    client_mqtt = mqtt_client.Client(client_id)
    client_mqtt.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    client_mqtt.on_connect = on_connect
    client_mqtt.connect("localhost", port=settings.MQTT_PORT)
    print(client_mqtt.__dict__)
    return client_mqtt


class Connector:
    client_mqtt = None

    def __init__(self):
        self.client_mqtt = connect_mqtt()
