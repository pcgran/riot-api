import Constants as Consts
import requests
import logging


class RiotAPI(object):
    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region

    # private method
    # api_url: summoners, match history, etc
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value

        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                url=api_url
            ),
            params=args
        )

        logging.warning(response.url)

        if response.status_code == 200:
            return response.json()
        else:
            return 'error'

    def _global_request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value

        response = requests.get(
            Consts.URL['global_base'].format(
                url=api_url
            ),
            params=args
        )

        logging.warning(response.url)

        if response.status_code == 200:
            return response.json()
        else:
            return 'error'

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            region=self.region,
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )

        return self._request(api_url)

    # Given a summoner name, returns its id
    def get_summoner_id(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            region=self.region,
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )

        response = self._request(api_url)

        return response[name]['id']

    # Given a summoner name, returns its match history
    def get_match_history(self, name):
        api_url = Consts.URL['match_history'].format(
            region=self.region,
            version=Consts.API_VERSIONS['match_history'],
            summoner_id=self.get_summoner_id(name)
        )

        return self._request(api_url)

    # Given a summoner name, returns the info of its current game
    def get_current_game(self, name, platf_id):
        api_url = Consts.URL['current_game'].format(
            version=Consts.API_VERSIONS['current_game'],
            platform_id=platf_id,
            summoner_id=self.get_summoner_id(name)
        )

        return self._request(api_url)

    # Returns a champion name from its ID
    def get_all_champions(self):
        api_url = Consts.URL['lol_static_data'].format(
            region=self.region,
            version=Consts.API_VERSIONS['lol_static_data']
        )

        response = self._global_request(api_url)

        return response

    # returns the leagues info of all the participants
    def get_summoners_info(self, participants):

        summoner_ids = ''
        for element in participants:
            summoner_ids += str(element['summonerId']) + ','

        summoner_ids = summoner_ids.strip(',')

        api_url = Consts.URL['league_info'].format(
            region=self.region,
            version=Consts.API_VERSIONS['leagues'],
            summoner_ids=summoner_ids
        )

        return self._request(api_url)
