import settings


def get_items():
    """
    Get items from active player.
    """

    if settings.DEBUG:
        return {
            "itens": [
                {
                    "name": "Divine Sunderer",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/item/6632.png",
                },
                {
                    "name": "Plated Steelcaps",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/item/3047.png",
                },
                {
                    "name": "Sterak's Gage",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/item/3053.png",
                },
                {
                    "name": "Black Cleaver",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/item/3071.png",
                },
                {
                    "name": "Death's Dance",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/item/6333.png",
                },
                {
                    "name": "Sterak's Gage",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/item/3053.png",
                },
            ]
        }

    # TODO: Implement this
    raise NotImplementedError
