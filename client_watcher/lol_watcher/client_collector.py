import time
from threading import Thread

from client_watcher.constants import (
    MQTT_TOPICS,
    MqttMessage,
    MESSAGE_TYPES,
    ACTION_TYPES,
)
from client_watcher.lol_watcher.endpoints.live_client_data.player import (
    get_active_player,
)
from client_watcher.mqtt import Publish
from client_watcher.shared_modules import lock, client_mqtt


class ClientCollector:
    def __init__(self):
        self.user_collector_thread = Thread(target=self.get_data_from_client)
        self.client_mqtt = None
        self.mqtt_publisher = None

    def get_data_from_client(self):
        while True:
            self.mqtt_publisher.publish(
                MqttMessage(
                    topic=MQTT_TOPICS.COMPANION,
                    type=MESSAGE_TYPES.ACTION,
                    action=ACTION_TYPES.USER_DATA_UPDATE,
                    message=get_active_player().json(),
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
