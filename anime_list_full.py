from unittest import result
import animelist, anime_offline_database, json
from datetime import datetime
from collections import defaultdict


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

print(type(fullList))


with open("anime_list_full.json", "w") as write:
    json.dump(fullList,write, indent=2)









#### Generates time stamp for Readme file ####
now = datetime.now()
d2 = now.strftime("Last Generated at: %B %d, %Y at %I:%M %p")

with open("README.md","r") as file:
    data = file.readlines()

data[1] = d2
print(data[1])

with open("README.md", "w") as file:
    file.writelines( data )
