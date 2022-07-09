import animelist, anime_offline_database, tmdb, json, os
from datetime import datetime
from collections import defaultdict

def genList():
    list1 = open('anime_offline_database.json')
    list2 = open('animelist.json')

    list1 = json.load(list1)
    list2 = json.load(list2)

    fullList = []
    d = defaultdict(dict)
    for l in (list1, list2):
        for anime in l:
            d[anime["anidb_id"]].update(anime)
    fullList = list(d.values())



    with open("anime_list_full.json", "w") as write:
        json.dump(fullList,write, indent=2)
    print("anime_list_full.json Generated")


def updateReadme():
    #### Generates time stamp for Readme file ####
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../README.md')
    now = datetime.now()
    d2 = now.strftime("Last Generated at: %B %d, %Y at %I:%M %p UTC")

    with open(filename,"r") as file:
        data = file.readlines()

    data[1] = d2


    with open(filename, "w") as file:
        file.writelines( data )
    print("README.md updated")

def mergeTMDB():
    ogList = json.load(open('anime_list_full.json'))
    tmdbList = json.load(open('tmdb.json'))

    mergedList = []
    d = defaultdict(dict)
    for l in (ogList, tmdbList):
        for anime in l:
            d[anime["anidb_id"]].update(anime)
    mergedList = list(d.values())
    with open("anime_list_full.json", "w") as write:
        json.dump(mergedList,write, indent=2)
    print("Lists Merged")

anime_offline_database.genList()
animelist.genList()
today = datetime.now().strftime("%d")
genList()
if "01" in today or os.path.exists("tmdb.json") == False:
    tmdb.genList()
mergeTMDB()

updateReadme()



