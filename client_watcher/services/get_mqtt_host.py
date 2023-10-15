import settings


def get_mqtt_host():
    if settings.DEBUG:
        return

    # TODO: Get host and port broker user interface
    raise NotImplementedError
