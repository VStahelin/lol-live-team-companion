import settings


def get_match_data():
    if settings.DEBUG:
        return {
            "game_id": 123456,
            "game_mode": "CLASSIC",
        }

    # TODO: Implement this
    raise NotImplementedError
