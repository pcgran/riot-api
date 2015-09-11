URL = {
    'base': 'https://{proxy}.api.pvp.net/{url}',
    'global_base': 'https://global.api.pvp.net/{url}',
    'summoner_by_name': 'api/lol/{region}/v{version}/summoner/by-name/{names}',
    'match_history': 'api/lol/{region}/v{version}/matchhistory/{summoner_id}',
    'current_game': 'observer-mode/rest/consumer/getSpectatorGameInfo/{platform_id}/{summoner_id}',
    'lol_static_data': 'api/lol/static-data/{region}/v{version}/champion'


    # https://euw.api.pvp.net/api/lol/euw/v1.4/summoner/by-name/conkii?api_key=key
    # https://euw.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/EUW1/23071574?api_key=key
}

API_VERSIONS = {
    'summoner': '1.4',
    'match_history': '2.2',
    'current_game': '1.0',
    'lol_static_data': '1.2'
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
