import xmltodict, json, requests


def genList():
    response = requests.get("https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml")
    source_list = response.text

    g = open("animelist.xml", "w")
    g.write(source_list)
    g.close

    with open("animelist.xml", 'r') as myfile:
        obj = xmltodict.parse(myfile.read())

    obj = obj['anime-list']
    obj = obj['anime']

    newList = []
    for anime in obj:
        animeDict = {}
        if anime["@tvdbid"].isnumeric() and anime["@tvdbid"] != "":
            animeDict["thetvdb_id"] = int(anime["@tvdbid"])
        if anime["@imdbid"] != "" and anime["@imdbid"] != "unknown":
            animeDict["imdb_id"] = anime["@imdbid"].split(',')[0]
        if anime["@anidbid"].isnumeric() and anime["@anidbid"] != "":
            animeDict["anidb_id"] = int(anime["@anidbid"])
        

        newList.append(animeDict)


    with open("animelist.json", "w") as write:
        json.dump(newList,write, indent=2)

    print("animelist.json Generated")