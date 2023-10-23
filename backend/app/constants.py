import json
from collections import namedtuple
from dataclasses import dataclass

MQTT_TOPICS = [
    "actions",
    "actions/master",
    "actions/client",
    "client/ability",
    "client/items",
    "match/data",
    "match/events",
    "lobby",
]

ACTS = namedtuple(
    "Acts",
    ["PING", "PONG", "DISCONNECT"],
)(
    "ping",
    "pong",
    "disconnect",
)


CACHE_KEYS = namedtuple(
    "CacheKeys",
    ["MQTT_CLIENT", "SUBSCRIBER_THREAD", "RUNNING_MATCHES"],
)(
    "mqtt_client",
    "subscriber_thread",
    "running_matches",
)


@dataclass
class MqttMessage:
    topic: MQTT_TOPICS
    sender: str
    data: dict
    receiver: str = None

    @property
    def json(self):
        return {
            "topic": self.topic,
            "sender": self.sender,
            "receiver": self.receiver,
            "data": self.data,
        }

    @property
    def json_str(self):
        return json.dumps(self.json)
