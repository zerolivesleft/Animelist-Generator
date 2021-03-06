import animelist, anime_offline_database, tmdb, json, os
from dateutil import tz
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
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/Chicago')

def updateReadme():
    #### Generates time stamp for Readme file ####
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../README.md')
    now = datetime.now()
    d2 = now.strftime("%Y-%m-%d %H:%M:%S")
    utc = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    central = central.strftime("%B %d, %Y %I:%M %p %Z")

    with open(filename,"r") as file:
        data = file.readlines()

    data[1] = "Last generated at: " + central + "\n"


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



