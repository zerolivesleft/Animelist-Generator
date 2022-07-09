import requests, json, os

def genList():
    print("Generating tmdb.json")
    list1 = json.load(open('anime_list_full.json'))
    list2 = []
    apikey = os.environ.get("apikey")
    for anime in list1:
        if "imdb_id" in anime:
            url = ("https://api.themoviedb.org/3/movie/" + anime["imdb_id"] + "?api_key=" + apikey)
            response = requests.get(url).json()
            if "id" in response:
                anime["themoviedb_id"] = response["id"]
                list2.append(anime)
            else:
                url2 = ("https://api.themoviedb.org/3/show/" + anime["imdb_id"] +"?api_key=" + apikey)
                response2 = requests.get(url2).json()
                if "id" in response:
                    anime["themoviedb_id"] = response["id"]
                    list2.append(anime)



    with open("tmdb.json", "w") as write:
        json.dump(list2,write, indent=2)
    print("tmdb.json Generated")