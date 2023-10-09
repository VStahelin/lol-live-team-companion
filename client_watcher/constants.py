from collections import namedtuple

MQTT_TOPICS = namedtuple(
    "MQTT_TOPICS",
    ["TEST", "COMPANION"],
)(
    "test",
    "COMPANION",
)


HTTP_METHODS = namedtuple(
    "HTTP_METHODS",
    ["GET", "POST", "PUT", "PATCH", "DELETE"],
)(
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
)
