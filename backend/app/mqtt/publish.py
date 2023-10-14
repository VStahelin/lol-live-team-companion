from paho.mqtt import client as mqtt_client

from constants import MqttMessage


class Publish:
    def __init__(self, client_mqtt: mqtt_client):
        self.client_mqtt = client_mqtt

    def publish(self, message: MqttMessage):
        result = self.client_mqtt.publish(message.topic, message.json_str)
        status = result[0]
        if status == 0:
            print(f"Send {message}")
        else:
            print(f"Failed to send message to topic {message.topic}")
