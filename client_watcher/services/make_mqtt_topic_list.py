from constants import MQTT_TOPICS


def make_mqtt_topic_list_with_match_id(match_id: str):
    return MQTT_TOPICS._replace(  # noqa
        **{
            field: f"{match_id}/" + getattr(MQTT_TOPICS, field)
            for field in MQTT_TOPICS._fields  # noqa
        }
    )
