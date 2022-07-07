import xmltodict, json, requests

response = requests.get("https://raw.githubusercontent.com/Anime-Lists/anime-lists/master/anime-list-master.xml")
source_list = response.text

g = open("anime-list.xml", "w")
g.write(source_list)
g.close

with open("anime-list.xml", 'r') as myfile:
    obj = xmltodict.parse(myfile.read())

obj = obj['anime-list']
obj = obj['anime']

newList = []
for items in obj:
    if "name" in items:
        del items["name"]
    if "supplemental-info" in items:
        del items["supplemental-info"]
    if "@tmdbid" in items:
        del items["@tmdbid"]
    if "@episodeoffset" in items:
        del items["@episodeoffset"]
    if "@defaulttvdbseason" in items:
        del items["@defaulttvdbseason"]
    if "mapping-list" in items:
        del items["mapping-list"]
    if "before" in items:
        del items["before"]
    if "@anidbid" in items:
        items["anidb_id"] = items.pop("@anidbid")
    if "@imdbid" in items:
        items["imdb_id"] = items.pop("@imdbid")
    if "@tvdbid" in items:
        items["thetvdb_id"] = items.pop("@tvdbid")
    items = {k: v for k, v in items.items() if v}
    newList.append(items)

with open("animelist.json", "w") as write:
    json.dump(newList,write, indent=2)

