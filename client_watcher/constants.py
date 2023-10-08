from collections import namedtuple

MQTT_TOPICS = namedtuple(
    "MQTT_TOPICS",
    ["TEST", "COMPANION"],
)(
    "test",
    "COMPANION",
)
