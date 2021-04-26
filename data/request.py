#import requests
import json
import csv

import sys,os,pathlib
from pathlib import Path

base_path = str(Path(__file__).parent)



""" apiKey = "f82927e8dbbd48eab7d2b49482f026eb"
searchGame = "dragon"


requestQuery = requests.get("https://api.rawg.io/api/games?key={}&search={}".format(apiKey,searchGame))

response = requestQuery.json() 

with open("response.txt", 'w') as outfile:
    json.dump(response, outfile) """

'''
#Ejemplo de parseo de json
diccionarioUsuarios = {}
total = 5000

with open(base_path + '\\users.csv', newline="" , encoding='utf-8') as csvfile:    
    csvUsuarios = csv.reader(csvfile, delimiter=',')
    next(csvUsuarios)           
    contador = 0
    while contador < total:
        diccionarioUsuarios[next(csvUsuarios)[0]] = {}
        contador += 1
    for row in csvUsuarios:        
        usuario = row[0] 
        diccionarioUsuarios[usuario] = {}
    
    
with open(base_path + "\\listasDeLosUsuarios.txt" , "w") as outfile:
    json.dump(diccionarioUsuarios, outfile)
'''



