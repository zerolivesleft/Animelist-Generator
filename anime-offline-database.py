import json, requests
from turtle import done

url = "https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json"
response = requests.get(url)
response = response.json()
response = response["data"]
newList = []
finalList = []


for items in response:
    if "sources" in items:
        newList.append(items["sources"])

for anime in newList:
    for id in anime:
        if "myanimelist" in id:
            id = 
    print("Next Anime!!!!!!!!!")

with open("anime-offline-database.json", "w") as write:
    json.dump(finalList,write, indent=2)