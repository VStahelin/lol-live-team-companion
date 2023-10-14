import json
from collections import namedtuple
from dataclasses import dataclass

MQTT_TOPICS = [
    "clients",
    "commands",
    "stats",
    "test",
    "COMPANION",
]

MESSAGE_TYPES = namedtuple(
    "Message_Types",
    ["MESSAGE", "ACTION", "LOG"],
)(
    "message",
    "action",
    "log",
)

ACTION_TYPES = namedtuple(
    "Action_Types",
    ["PING", "USER_DATA_UPDATE", "USER_DATA_REQUEST"],
)(
    "ping",
    "user_data",
    "user_data_request",
)


@dataclass
class MqttMessage:
    topic: MQTT_TOPICS
    type: MESSAGE_TYPES
    message: str
    action: ACTION_TYPES = None

    @property
    def json(self):
        return {
            "topic": self.topic,
            "type": self.type,
            "message": self.message,
            "action": self.action,
        }

    @property
    def json_str(self):
        return json.dumps(self.json)
