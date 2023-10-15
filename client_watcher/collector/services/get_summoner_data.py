import settings


def get_summoner_data(summoner_name):
    """
    Get summoner data by summoner name.
    """

    if settings.DEBUG:
        return {
            "nickname": "godao",
            "runes": {
                "primary": {
                    "name": "Precision",
                    "keystone": "Conqueror",
                    "keystone_image": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Conqueror/Conqueror.png",  # noqa
                },
                "secondary": {
                    "name": "Domination",
                    "keystone": "Ravenous Hunter",
                    "keystone_image": "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Domination/RavenousHunter/RavenousHunter.png",  # noqa
                },
            },
            "champion": {
                "name": "Aatrox",
                "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/champion/Aatrox.png",
            },
            "summoner_spells": {
                "summoner_spell_1": {
                    "name": "Flash",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/spell/SummonerFlash.png",
                },
                "summoner_spell_2": {
                    "name": "Ignite",
                    "image": "https://ddragon.leagueoflegends.com/cdn/11.16.1/img/spell/SummonerDot.png",
                },
            },
        }

    # TODO: get data from lol_watcher LCU and serialize it
    #  to the same format as the DEBUG data
    raise NotImplementedError
