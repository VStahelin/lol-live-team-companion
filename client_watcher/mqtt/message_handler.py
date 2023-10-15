import settings
from client_watcher.cache_manager import get_cache
from client_watcher.collector.services.actions import (
    client_act,
    global_act,
)

from constants import MqttMessage

MATCH_MQTT_TOPICS = get_cache("match_mqtt_topics")


def message_handler(message: MqttMessage, topic):
    print(get_cache("match_id"))
    if topic not in MATCH_MQTT_TOPICS:
        raise Exception("Topic not valid")

    try:
        match topic:
            case MATCH_MQTT_TOPICS.LOBBY:
                print(f"Message: {message}")
            case MATCH_MQTT_TOPICS.ACT_TO_CLIENT:
                if message.receiver != settings.CLIENT_ID:
                    return

                client_act(message)
            case MATCH_MQTT_TOPICS.ACT:
                global_act(message)
            case _:
                print("No action for this payload")

    except Exception as e:
        print(f"Error in message handler: {e}")
        print(f"Error in message handler: {message}")
