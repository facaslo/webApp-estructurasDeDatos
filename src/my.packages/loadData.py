import sys,os,pathlib
from pathlib import Path

base_path = Path(__file__).parent.parent.parent
database_path = os.path.join(base_path, '.\\data' )

import json
import LinkedLists
import time
import csv


# start = time.time()

def cargarBaseJuegos():
    with open(database_path + '\\game_info.csv', newline="" , encoding='utf-8') as csvfile:
        LinkedListsTodosLosJuegos = LinkedLists.LinkedList()
        coleccionTodosLosJuegos = csv.reader(csvfile, delimiter=',')
        for row in coleccionTodosLosJuegos:
            juego = LinkedLists.LinkedList()
            for campo in row:
                juego.pushBack(campo)
            LinkedListsTodosLosJuegos.pushBack(juego)  
 
#end = time.time()
#print(end-start)
