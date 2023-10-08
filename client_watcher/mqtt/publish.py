import time

from paho.mqtt import client as mqtt_client

from client_watcher.constants import MQTT_TOPICS
from client_watcher.utils import json_to_str


class Publish:
    def __init__(self, client_mqtt: mqtt_client, topic: str = MQTT_TOPICS.COMPANION):
        self.client_mqtt = client_mqtt
        self.topic = topic

    def publish(self, topic: str = None, json: str = ""):
        topic = topic if topic else self.topic
        result = self.client_mqtt.publish(topic, json)
        status = result[0]
        if status == 0:
            print(f"Send `{json}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def publish_tester(self):
        msg_count = 1
        while True:
            time.sleep(1)
            msg = json_to_str({"msg": f"msg {msg_count}"})
            self.publish(self.topic, msg)
            msg_count += 1
