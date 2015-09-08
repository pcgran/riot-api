import sys
from RiotAPI import RiotAPI
import Constants as Consts


def get_platform_id(region):
    if region == Consts.REGIONS['europe_west']:
        return 'EUW1'
    elif region == Consts.REGIONS['north_america']:
        return 'NA1'
    else:
        return 'KR'


def get_champion_name(champions, champion_id):
    # when we loop through a dictionary, if we don't use key, value, it only takes the key as a string!!!
    for key, value in champions['data'].iteritems():
        if value['id'] == champion_id:
            return value['name']


def main():
    if len(sys.argv) == 3:
        summoner_name = sys.argv[1].lower()
        region = sys.argv[2].lower()
        platform_id = get_platform_id(region)

        api = RiotAPI('key', region)

        champions = api.get_all_champions()

        r = api.get_current_game(summoner_name, platform_id)

        if r != 'error':

            players = r['participants']

            for i in range(0, len(players)):
                print players[i]['summonerName'] + ': ' + get_champion_name(champions, players[i]['championId'])

        else:
            print 'This summoner is not in a game'

    else:
        print 'Invalid syntax'


if __name__ == "__main__":
    main()
