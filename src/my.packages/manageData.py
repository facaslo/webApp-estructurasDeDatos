import sys,os,pathlib
import json
import SequentialStructures
import TreeStructures
import csv
from pathlib import Path

def getGamesPath():
    base_path = Path(__file__).parent.parent.parent
    if sys.platform.startswith('linux'):
        games_path = os.path.join(base_path, './data/game_info.csv' )
    else:
        games_path = os.path.join(base_path, '.\\data\\game_info.csv' )
    return games_path

def getUsersPath():
    base_path = Path(__file__).parent.parent.parent
    if sys.platform.startswith('linux'):
        users_path = os.path.join(base_path, './data/users.csv' )
    else:
        users_path = os.path.join(base_path, '.\\data\\users.csv' )
    return users_path

def getUsersListPath():
    base_path = Path(__file__).parent.parent.parent
    if sys.platform.startswith('linux'):
        users_path = os.path.join(base_path, './data/listasDeLosUsuarios.txt' )
    else:
        users_path = os.path.join(base_path, '.\\data\\listasDeLosUsuarios.txt' )
    return users_path

def cargarBaseJuegos(tipo): 
    with open(getGamesPath(), newline="" , encoding='utf-8') as csvfile:
        csvTodosLosJuegos = csv.reader(csvfile, delimiter=',')
        next(csvTodosLosJuegos)
        if(tipo == "linked"):
            todosLosJuegos = SequentialStructures.LinkedList()        
            for row in csvTodosLosJuegos:
                juego = SequentialStructures.Array_Dinamic()
                for campo in row:
                    juego.pushBack(campo)
                todosLosJuegos.pushBack(juego)  
            
        elif(tipo == "dynamic"):
            todosLosJuegos = SequentialStructures.Array_Dinamic()
            for row in csvTodosLosJuegos:
                juego = SequentialStructures.Array_Dinamic()
                for campo in row:
                    juego.pushBack(campo)
                todosLosJuegos.pushBack(juego)   

    return todosLosJuegos

def cargarUsuarios(total , tipo):
    with open(getUsersPath(), newline="" , encoding='utf-8') as csvfile:
        coleccionUsuarios = csv.reader(csvfile, delimiter=',')        

        if(tipo == "linked"):
            todosLosUsuarios = SequentialStructures.LinkedList()                    
            contador = 0
            while contador<total:
                usuario = SequentialStructures.LinkedList()
                for campo in next(coleccionUsuarios):
                    usuario.pushBack(campo)
                todosLosUsuarios.pushBack(usuario)  
                contador += 1

        elif(tipo == "dynamic"):
            todosLosUsuarios = SequentialStructures.Array_Dinamic()
            contador = 0
            while contador<total:
                usuario = SequentialStructures.Array_Dinamic()
                for campo in next(coleccionUsuarios):
                    usuario.pushBack(campo)
                todosLosUsuarios.pushBack(usuario)  
                contador += 1
            
        
        return todosLosUsuarios

def cargarDuplaUserPassword(tipo, user, password):
    if( tipo == "linked"):
        userPassword = SequentialStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        userPassword = SequentialStructures.Array_Dinamic()
        
    userPassword.pushBack(user)
    userPassword.pushBack(password)
    return userPassword

def agregarUsuarioEnEstructura(tipo, estructura, user, password):
    if( tipo == "linked"):
        nuevaEntrada = cargarDuplaUserPassword("linked" , user, password)
        
    elif(tipo == "dynamic"):
        nuevaEntrada = cargarDuplaUserPassword("dynamic" , user, password)

    estructura.pushFront(nuevaEntrada)

    return estructura   
    

def escribirUsuarioCSV(estructura):
    with open(getUsersPath(), "w" , newline="") as outfile:
        writer = csv.writer(outfile)
        for elemento in estructura:            
            writer.writerow(elemento)


def escribirUsuarioJson(usuario):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
        listasDeUsuarios[usuario] = {}
    with open(getUsersListPath(), "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

def recuperarListaUsuario(usuario, tipo):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
    if( tipo == "linked"):
        colecciones = SequentialStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        colecciones = SequentialStructures.Array_Dinamic()

    for elemento in listasDeUsuarios[usuario]:
        colecciones.pushBack(elemento)

    return colecciones

def crearListaEnUsuario(usuario, nombreLista):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
    listasDeUsuarios[usuario][nombreLista] = []

    with open(getUsersListPath(), "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

    
def getContenidosLista(usuario, nom_lista, tipo):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
        contenidos = listasDeUsuarios[usuario][nom_lista]

    if( tipo == "linked"):
        colecciones = SequentialStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        colecciones = SequentialStructures.Array_Dinamic()
    
    for elemento in contenidos:
        colecciones.pushBack(elemento)
    
    return colecciones

def escribirContenidosLista(usuario, nom_lista, slug, agregar):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
        contenidos = listasDeUsuarios[usuario][nom_lista]

    if slug in contenidos and agregar == False:
        contenidos.remove(slug)
    elif slug not in contenidos and agregar == True:
        contenidos.append(slug) 

    with open(getUsersListPath(), "w") as outfile:
        json.dump(listasDeUsuarios, outfile)
    

def gameInCollection(nombre_juego, todosLosJuegos):
    game = None
    for juego in todosLosJuegos:
        if nombre_juego == juego.getElement(1):            
            game = juego    
            break
    return game

def actualizarListasEnJSON(usuario, colecciones):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
    for lista in listasDeUsuarios[usuario]:
        if colecciones.find(lista) == -1:
            del listasDeUsuarios[usuario][lista]
            break
    
    with open(getUsersListPath(), "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

def searchGame(nombre, juegos, tipo):
    if( tipo == "linked"):
        resultado = SequentialStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        resultado = SequentialStructures.Array_Dinamic()

    #for juego in juegos:
    #    if nombre.lower() in juego.getElement(0).lower():
    #        resultado.sortedInsertion(juego)
    
    heap = TreeStructures.BinaryHeap()

    for juego in juegos:
        if nombre.lower() in juego.getElement(0).lower():
            heap.insert(juego)

    while heap.size >= 0:
        resultado.pushFront(heap.extractMax())
    
    return resultado

