import threading
import time

from client_watcher.cache_manager import set_cache, get_cache
from client_watcher.collector.data_collector import DataCollector
from client_watcher.constants import MqttMessage
from client_watcher.mqtt import Subscribe
from client_watcher.mqtt.publish import Publish
from client_watcher.services.get_match import get_match_id
from client_watcher.services.get_mqtt_host import get_mqtt_host
from client_watcher.services.make_mqtt_topic_list import (
    make_mqtt_topic_list_with_match_id,
)
from client_watcher.settings import (
    CLIENT_ID,
)
from client_watcher.shared_modules import (
    lock,
    client_mqtt,
)


class Core(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.client_mqtt = None
        self.first_loop = True

    def run(self):
        # TODO - step = Get host and port broker
        get_mqtt_host()

        # TODO - step = Get match id
        match_id = get_match_id()

        # Update the match mqtt topics
        MATCH_MQTT_TOPICS = make_mqtt_topic_list_with_match_id(match_id)  # noqa: F811
        set_cache("match_mqtt_topics", MATCH_MQTT_TOPICS)

        # Setting the mqtt client
        with lock:
            self.client_mqtt = client_mqtt

        mqtt_subscribe_thread = Subscribe(
            client_mqtt=self.client_mqtt,
            topic=MATCH_MQTT_TOPICS.LOBBY,
            delay=1,
        )

        mqtt_subscribe_thread.start()

        if self.first_loop:
            time.sleep(2)
            self.first_loop = False

        publisher = Publish(client_mqtt=self.client_mqtt)

        publisher.publish(
            MqttMessage(
                topic=MATCH_MQTT_TOPICS.LOBBY,
                sender=CLIENT_ID,
                data={
                    "message": f"Client: {CLIENT_ID} is now online!",
                },
            )
        )

        set_cache("backend_was_started", False)
        while not get_cache("backend_was_started"):
            publisher.publish(
                MqttMessage(
                    topic=MATCH_MQTT_TOPICS.ACT_TO_MASTER,
                    sender=CLIENT_ID,
                    data={
                        "action": "ping",
                        "timestamp": time.time(),
                    },
                )
            )

            time.sleep(5)

        time.sleep(5)
        data_collector = DataCollector()
        data_collector.run()

        try:
            while True:
                time.sleep(0.1)

        except KeyboardInterrupt:
            mqtt_subscribe_thread.do_run = False
            self.client_mqtt.disconnect()
            data_collector.stop()
            exit()


if __name__ == "__main__":
    core = Core()
    core.run()
