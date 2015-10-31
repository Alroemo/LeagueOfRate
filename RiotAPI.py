import requests
import string
import RiotConsts as Consts

class RiotAPI(object):

    def __init__(self, api_key, region=Consts.REGIONS['NORTH_AMERICA']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
                if key not in args:
                    args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
                ),
            params=args
            )
        return response.json()

    def get_summoner_by_name(self,name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
            )
        return self._request(api_url)


    def get_summoner_rune(self, id):

        api_url = Consts.URL['summoner_summonerId_rune'].format(
            version=Consts.API_VERSIONS['summoner'],
            ids = id
        )
        return self._request(api_url)

    def get_rune_by_id(self, id):
        api_upl = Consts.URL['get_rune_by_id'].format(
            version=Consts.API_VERSIONS['lol-static-data'],
            ids = id
        )
        return self._request(api_upl)

    def get_rune_stats_by_id(self, id):
        api_upl = Consts.URL['get_rune_stats_by_id'].format(
            version=Consts.API_VERSIONS['lol-static-data'],
            ids = id
        )
        return self._request(api_upl)

    def get_summoner_masteries(self, id):
        api_url = Consts.URL['summoner_summonerId_masteries'].format(
            version=Consts.API_VERSIONS['summoner'],
            ids = id
        )
        return self._request(api_url)


    def get_champions(self):
        api_url = Consts.URL['champions'].format(
            version=Consts.API_VERSIONS['lol-static-data'],
        )
        return self._request(api_url)

    def get_champion_stats(self, id):
        api_url = Consts.URL['get_champion_stats'].format(
            version=Consts.API_VERSIONS['lol-static-data'],
            ids = id
        )
        return self._request(api_url)

    def get_champion_by_name(self, championId):
        api_url = Consts.URL['champion_by_id'].format(
            version=Consts.API_VERSIONS['lol-static-data'],
            ids = championId
        )
        return self._request(api_url)

    def get_champion_info(self, championId):
        api_url = Consts.URL['get_champion_info'].format(
            version=Consts.API_VERSIONS['lol-static-data'],
            ids=championId
        )
        return  self._request(api_url)

    def get_champion_spells(self, id):
        api_url = Consts.URL['get_champion_spells'].format(
            version=Consts.API_VERSIONS['lol-static-data'],
            ids = id
        )
        return  self._request(api_url)