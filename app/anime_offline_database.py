import json
import requests

def genList():

    url = "https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json"
    response = requests.get(url)
    response = response.json()
    response = response["data"]
    newList = []
    secondList = []
    finalList = []

    for items in response:
        if "sources" in items:
            newList.append(items["sources"])

    for anime in newList:
        animeDict = {}
        for id in anime:
            if "myanimelist" in id:
                id = int((id.partition("anime/")[2]))
                animeDict["mal_id"] = id
            elif "anidb.net" in id:
                id = int(id.partition("anime/")[2])
                animeDict["anidb_id"] = id
            elif "anilist.co" in id:
                id = int(id.partition("anime/")[2])
                animeDict["anilist_id"] = id
            elif "kitsu" in id:
                id = id.partition("anime/")[2]
                if id.isdigit():
                    id = int(id)
                    animeDict["kitsu_id"] = id
            elif "livechart" in id:
                id = int(id.partition("anime/")[2])
                animeDict["livechart_id"] = id
        secondList.append(animeDict)

    for anime in secondList:
        if "anidb_id" in anime:
            finalList.append(anime)
            


    with open("anime_offline_database.json", "w") as write:
        json.dump(finalList, write, indent=2)
    print("anime_offline_database.json Generated")
