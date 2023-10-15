import time
from threading import Thread

from client_watcher import settings
from client_watcher.cache_manager import get_cache
from client_watcher.collector.api.player import (
    get_active_player,
)
from client_watcher.constants import (
    MqttMessage,
)
from client_watcher.mqtt import Publish

from client_watcher.shared_modules import lock, client_mqtt

MATCH_MQTT_TOPICS = get_cache("match_mqtt_topics")


class DataCollector:
    def __init__(self):
        self.user_collector_thread = Thread(target=self.get_data_from_client)
        self.client_mqtt = None
        self.mqtt_publisher = None

    def get_data_from_client(self):
        while True:
            message = (
                get_active_player().json()
                if not settings.DEBUG
                else {"message": "This is a test message"}
            )

            self.mqtt_publisher.publish(
                MqttMessage(
                    topic=MATCH_MQTT_TOPICS.LOBBY,
                    sender=settings.CLIENT_ID,
                    data=message,
                )
            )
            time.sleep(5)

    def stop(self):
        self.user_collector_thread.do_run = False
        self.user_collector_thread.join()

    def run(self):
        with lock:
            self.client_mqtt = client_mqtt

        self.mqtt_publisher = Publish(client_mqtt=self.client_mqtt)

        self.user_collector_thread.start()
