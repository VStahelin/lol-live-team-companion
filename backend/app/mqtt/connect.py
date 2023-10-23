from paho.mqtt import client as mqtt_client

import settings


class Connector:
    def __init__(self):
        self.client_mqtt = None

    def connect_mqtt(self):
        def on_connect(client_mqtt, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client_id = settings.CLIENT_ID
        self.client_mqtt = mqtt_client.Client(client_id)
        self.client_mqtt.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
        self.client_mqtt.on_connect = on_connect
        self.client_mqtt.connect("localhost", port=settings.MQTT_PORT)

        return self.client_mqtt
