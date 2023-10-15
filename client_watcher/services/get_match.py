import settings


def get_match_id():
    if settings.DEBUG:
        return settings.DEBUG_MATCH_ID

    # TODO: Get match id user interface
    raise NotImplementedError
