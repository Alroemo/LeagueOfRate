URL = {
    'base' : 'https://global.api.pvp.net/api/{url}',
    'summoner_by_name' : 'lol/na/v{version}/summoner/by-name/{names}?champData=stats',
    'summoner_summonerId_rune' : 'lol/na/v{version}/summoner/{ids}/runes',
    'summoner_summonerId_masteries' : 'lol/na/v{version}/summoner/{ids}/masteries',
    'champions' : 'lol/static-data/na/v{version}/champion',
    'champion_by_id': 'lol/static-data/na/v{version}/champion/{ids}',
    'get_champion_stats' : 'lol/static-data/na/v1.2/champion/{ids}?champData=stats',
    'get_champion_info' : 'lol/static-data/na/v1.2/champion/{ids}?champData=info',
    'get_champion_spells' : 'lol/static-data/na/v1.2/champion/{ids}?champData=spells',
    'get_rune_by_id' : 'lol/static-data/na/v{version}/rune/{ids}',
    'get_rune_stats_by_id' : 'lol/static-data/na/v{version}/rune/{ids}?runeData=all'
}

API_VERSIONS = {
    'champion': 1.2,
    'current-game': 1.0,
    'featured-games': 1.0,
    'game': 1.3,
    'league': 2.5,
    'lol-static-data': 1.2,
    'lol-status': 1.0,
    'match': 2.2,
    'matchhistory': 2.2,
    'matchlist': 2.2,
    'stats': 1.3,
    'summoner': 1.4,
    'team': 2.4
}

REGIONS = {
    'GLOBAL' : 'global',
    'BRAZIL' : 'br',
    'EUROPE_NORDIC_EAST' : 'eune',
    'EUROPE_WEST' : 'euw',
    'KOREA' : 'kr',
    'LATIN_AMERICA_NORTH' : 'lan',
    'LATIN_AMERICA_SOUTH' : 'las',
    'NORTH_AMERICA' : 'na',
    'OCEANIA' : 'oce',
    'RUSSIA' : 'ru',
    'TURKEY' : 'tr'
}
