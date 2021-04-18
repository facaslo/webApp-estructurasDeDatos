import requests
import json

apiKey = "f82927e8dbbd48eab7d2b49482f026eb"
searchGame = "dragon"

'''
requestQuery = requests.get("https://api.rawg.io/api/games?key={}&search={}".format(apiKey,searchGame))

response = requestQuery.json() 

with open("response.txt", 'w') as outfile:
    json.dump(response, outfile)
'''


with open('response.txt') as json_file:
    data = json.load(json_file)
    print(len(data["results"])) 
    for p in data["results"]:
        print (p["name"])
