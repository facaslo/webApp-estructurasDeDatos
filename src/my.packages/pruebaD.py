import json
import LinkedLists
import time

start = time.time()
games = LinkedLists.LinkedList()
with open('C:\\Users\\Daniel\\Downloads\\webApp-estructurasDeDatos\\src\\my.packages\\Ejemplo1.json') as json_file:
    data = json.load(json_file)
    print(len(data["results"])) 
    for game in data["results"]:
        gamelist = LinkedLists.LinkedList()
        for atri in game:
            if atri == "name" or atri == "released" or atri == "background_image" or atri == "rating" or atri == "ratings-count" or atri == "updated" or atri == "platforms":
                if atri == "platforms":
                    plat = LinkedLists.LinkedList()
                    for platform in game["platforms"]:
                        plat.pushBack(platform["platform"]["name"])
                    gamelist.pushBack(plat)
                else:
                    gamelist.pushBack(game[str(atri)])
        games.pushBack(gamelist)
end = time.time()
print(end-start)