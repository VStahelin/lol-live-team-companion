import json
from collections import namedtuple
from dataclasses import dataclass

HTTP_METHODS = namedtuple(
    "HTTP_Methods",
    ["GET", "POST", "PUT", "PATCH", "DELETE"],
)(
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
)


MQTT_TOPICS = namedtuple(
    "MQTT_Topics",
    [
        "ACT",
        "ACT_TO_MASTER",
        "ACT_TO_CLIENT",
        "CLIENT_ABILITY",
        "CLIENT_ITEMS",
        "MATCH_DATA",
        "MATCH_EVENTS",
        "LOBBY",
    ],
)(
    "actions",
    "actions/master",
    "actions/client",
    "client/ability",
    "client/items",
    "match/data",
    "match/events",
    "lobby",
)


ACTS = namedtuple(
    "Acts",
    ["PING", "PONG", "DISCONNECT"],
)(
    "ping",
    "pong",
    "disconnect",
)


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
    ["PING", "PONG", "DISCONNECT"],
)(
    "ping",
    "pong",
    "disconnect",
)


@dataclass
class MqttMessage:
    topic: str
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
