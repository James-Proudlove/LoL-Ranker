import requests
import json
key = "RGAPI-cc0dcde0-d234-499b-8dfa-23b6b5fb0e12"
url = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s?api_key=" + key

request_types = {"list_champion": "/lol/static-data/v3/champions",
                 "get_champion_name": "/lol/platform/v3/champions/%s",
                 "summoner_id": "/lol/summoner/v3/summoners/by-name/%s"}

summoners = {"James": "JediJesus",
             "Mass": "PuddingSpoon",
             "Isaac": "SerTengu",
             "Charlie": "Chipmonkcheeks",
             "Rich": "Chaos1830"}

def main():
    #for name, summoner in summoners.items():
    #    print(name)
    #    riot_api = requests.get(url % summoner)
    #    results = riot_api.json()
    #    print("%s : %s" % (summoner, results))

    champ_list = get_champ_list()
    print(champ_list)

def get_champ_list():
    champ_name_list = []
    riot_api = requests.get(build_url("list_champion"))
    champ_list = riot_api.json()
    for champ in champ_list['data']:
        champ_name_list.append(champ)
    return champ_name_list

def build_url(req_type, additional_info=None):
    base_url = "https://euw1.api.riotgames.com"
    if additional_info:
        req_url = request_types.get(req_type % additional_info, "")
    else:
        req_url = request_types.get(req_type, "")
    api_url = "?api_key=" + key
    return "{0}{1}{2}".format(base_url, req_url, api_url)


main()
