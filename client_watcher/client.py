import threading
import time

from client_watcher.configs import CLIENT_ID
from client_watcher.constants import MQTT_TOPICS
from client_watcher.mqtt import connect_mqtt, Subscribe
from client_watcher.mqtt.publish import Publish
from client_watcher.utils import json_to_str


class Core(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.client_mqtt = connect_mqtt()
        self.first_loop = True

    def run(self):
        mqtt_subscribe_thread = Subscribe(
            client_mqtt=self.client_mqtt,
            topic=MQTT_TOPICS.COMPANION,
            delay=1,
        )
        mqtt_subscribe_thread.start()

        if self.first_loop:
            time.sleep(2)
            self.first_loop = False

        publisher = Publish(client_mqtt=self.client_mqtt)

        publisher.publish(
            json=json_to_str({"message": f"Client: {CLIENT_ID} is now online!"}),
        )

        time.sleep(5)
        publisher.publish(
            json=json_to_str({"action": "ping"}),
        )

        try:
            while True:
                time.sleep(5)
                print("Looping...")
        except KeyboardInterrupt:
            mqtt_subscribe_thread.do_run = False
            self.client_mqtt.disconnect()
            exit()


if __name__ == "__main__":
    core = Core()
    core.run()
