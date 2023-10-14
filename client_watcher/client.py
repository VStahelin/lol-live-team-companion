import threading
import time

from client_watcher.settings import CLIENT_ID
from client_watcher.constants import MQTT_TOPICS, MqttMessage, MESSAGE_TYPES
from client_watcher.lol_watcher.client_collector import ClientCollector
from client_watcher.mqtt import Subscribe
from client_watcher.mqtt.publish import Publish
from client_watcher.shared_modules import lock, client_mqtt


class Core(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.client_mqtt = None
        self.first_loop = True

    def run(self):
        with lock:
            self.client_mqtt = client_mqtt

        print("Subscribing to the broker topic: ", MQTT_TOPICS.COMPANION)

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

        message = MqttMessage(
            topic=MQTT_TOPICS.COMPANION,
            type=MESSAGE_TYPES.LOG,
            message=f"Client: {CLIENT_ID} is now online!",
        )

        publisher.publish(message)

        time.sleep(5)
        client_collector = ClientCollector()
        client_collector.run()

        try:
            while True:
                time.sleep(0.1)

        except KeyboardInterrupt:
            mqtt_subscribe_thread.do_run = False
            self.client_mqtt.disconnect()
            client_collector.stop()
            exit()


if __name__ == "__main__":
    core = Core()
    core.run()
