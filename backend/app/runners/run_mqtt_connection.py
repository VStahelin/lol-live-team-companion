from cache_manager import set_cache
from constants import CACHE_KEYS
from mqtt.connect import Connector
from mqtt.subscriber import Subscriber


def run_mqtt_connection():
    mqtt_client = Connector().connect_mqtt()
    subscriber = Subscriber(client_mqtt=mqtt_client)
    subscriber.start()

    set_cache(CACHE_KEYS.MQTT_CLIENT, mqtt_client)
    set_cache(CACHE_KEYS.SUBSCRIBER_THREAD, subscriber)
