URL = {
    'base': 'https://{proxy}.api.pvp.net/{url}',
    'global_base': 'https://global.api.pvp.net/{url}',
    'summoner_by_name': 'api/lol/{region}/v{version}/summoner/by-name/{names}',
    'match_history': 'api/lol/{region}/v{version}/matchhistory/{summoner_id}',
    'current_game': 'observer-mode/rest/consumer/getSpectatorGameInfo/{platform_id}/{summoner_id}',
    'lol_static_data': 'api/lol/static-data/{region}/v{version}/champion',
    'league_info': 'api/lol/{region}/v{version}/league/by-summoner/{summoner_ids}/entry'


    # https://euw.api.pvp.net/api/lol/euw/v1.4/summoner/by-name/conkii?api_key=key
    # https://euw.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/EUW1/23071574?api_key=key
    # https://euw.api.pvp.net/api/lol/euw/v2.5/league/by-summoner/26197810,19248536/entry?api_key=key
}

API_VERSIONS = {
    'summoner': '1.4',
    'match_history': '2.2',
    'current_game': '1.0',
    'lol_static_data': '1.2',
    'leagues': '2.5'
}

REGIONS = {
    'europe_west': 'euw',
    'north_america': 'na',
    'korea': 'kr'
}

PLATFORMS = {
    'europe_west': 'EUW1',
    'north_america': 'NA1',
    'korea': 'KR'
}

GAME_MODES = {
    'soloq': 'RANKED_SOLO_5x5'
}