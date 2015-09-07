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


def main():
    if len(sys.argv) == 3:
        summoner_name = sys.argv[1].lower()
        region = sys.argv[2].lower()
        platform_id = get_platform_id(region)

        api = RiotAPI('key', region)

        r = api.get_current_game(summoner_name, platform_id)

        if r != 'error':

            players = r['participants']

            for i in range(0, len(players)):
                print players[i]['summonerName'] + ': ' + api.get_champion_name(players[i]['championId'])

        else:
            print 'This summoner is not in a game'

    else:
        print 'Invalid syntax'


if __name__ == "__main__":
    main()
