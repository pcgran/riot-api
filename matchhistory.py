import sys
from RiotAPI import RiotAPI


def main():
    if len(sys.argv) == 3:
        summoner_name = sys.argv[1].lower()
        region = sys.argv[2]
        api = RiotAPI('key', region)
        r = api.get_match_history(summoner_name)
        print r
    else:
        print 'Invalid syntax'


if __name__ == "__main__":
    main()
