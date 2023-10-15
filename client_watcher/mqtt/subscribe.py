import threading
import time

from constants import MqttMessage
from client_watcher.mqtt.message_handler import message_handler


class Subscribe(threading.Thread):
    def __init__(self, client_mqtt, topic: str, delay: int = 0):
        threading.Thread.__init__(self)
        self.client_mqtt = client_mqtt
        self.topic = topic
        self.delay = delay

    def receive_message(self, client, userdata, msg):  # noqa
        try:
            import json

            message = MqttMessage(**json.loads(msg.payload))
            message_handler(message, msg.topic)

        except Exception as e:
            print(f"Error in subscribe callback: {e}")
            print(f"Error in subscribe callback: {msg}")

    def subscribe(self):
        def on_message(client, userdata, msg):  # noqa
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        time.sleep(self.delay)

        self.client_mqtt.subscribe(self.topic)
        self.client_mqtt.on_message = self.receive_message

    def run(self):
        self.client_mqtt.loop_start()
        thread = threading.current_thread()
        self.subscribe()

        while getattr(thread, "do_run", True):
            time.sleep(0.1)
