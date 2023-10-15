"""
Actions from client to server
- ping
- pong
- get_match_data
- get_match_events
- get_match_timeline
- get_match_timeline_events

Actions from server to client
- ping
- pong
- disconnect
- update_client_data
"""

ACTION_FROM_CLIENT = {
    "topic": "<match-id>/actions/master",
    "sender": "vitor-pc",
    "receiver": "master",  # From client, actions just always go to master
    "data": {
        "action": "ping",
        "timestamp": 123456,
    },
}

ACTION_FROM_MASTER = {
    "topic": "<match-id>/actions/client",
    "sender": "master",
    "receiver": "vitor-pc",
    "data": {
        "action": "pong",
        "timestamp": 123456,
    },
}

MATCH_DATA = {
    "topic": "<match-id>/match/data",
    "sender": "vitor-pc",
    "data": {
        "game_id": 123456,
        "game_mode": "CLASSIC",
    },
}

MATCH_EVENTS = {
    "topic": "<match-id>/match/events",
    "sender": "vitor-pc",
    "data": {
        "CHAMPION_KILL": {
            "timestamp": 123456,
            "summoner_killed": "godao",
            "summoner_assassin": "ciclano",
            "summoners_assist": ["fulano", "beltrano"],
        }
    },
}

MATCH_EVENTS2 = {
    "topic": "<match-id>/match/events",
    "sender": "vitor-pc",
    "data": {
        "TOWER_KILL": {
            "timestamp": 123456,
            "summoner_killed": "godao",
            "summoner_assassin": "ciclano",
            "summoners_assist": ["fulano", "beltrano"],
        }
    },
}

"""
When server receives the register, will vinculate the summoner
name with the sender client
"""
CLIENT_CHAMPION_REGISTER = {
    "topic": "<match-id>/lobby",
    "sender": "vitor-pc",
    "data": {
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
    },
}


CLIENT_ABILITY = {
    "topic": "<match-id>/client/ability",
    "sender": "vitor-pc",
    "data": {
        "q": {
            "cooldown": 10,
            "level": 1,
            "is_active": False,
            "is_ultimate": False,
        },
        "w": {
            "cooldown": 10,
            "level": 1,
            "is_active": False,
            "is_ultimate": False,
        },
        "e": {
            "cooldown": 10,
            "level": 1,
            "is_active": False,
            "is_ultimate": False,
        },
        "r": {
            "cooldown": 10,
            "level": 1,
            "is_active": False,
            "is_ultimate": True,
        },
    },
}


CLIENT_ITENS = {
    "topic": "<match-id>/client/itens",
    "sender": "vitor-pc",
    "data": {
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
    },
}
