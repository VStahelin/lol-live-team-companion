from client_watcher.collector import request


def get_active_player():
    """
    Get active player data in game.
    """
    print("get_active_player")
    endpoint = "/liveclientdata/activeplayer"
    params = {}
    return request.get(endpoint=endpoint, params=params)
