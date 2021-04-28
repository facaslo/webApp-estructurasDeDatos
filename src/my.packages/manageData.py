import sys,os,pathlib
from pathlib import Path

base_path = Path(__file__).parent.parent.parent
database_path = os.path.join(base_path, '.\\data' )

import json
import DataStructures
import time
import csv


# start = time.time()

def cargarBaseJuegos(tipo):
    with open(database_path + '\\game_info.csv', newline="" , encoding='utf-8') as csvfile:
        csvTodosLosJuegos = csv.reader(csvfile, delimiter=',')
        next(csvTodosLosJuegos)
        if(tipo == "linked"):
            todosLosJuegos = DataStructures.LinkedList()        
            for row in csvTodosLosJuegos:
                juego = DataStructures.Array_Dinamic()
                for campo in row:
                    juego.pushBack(campo)
                todosLosJuegos.pushBack(juego)  
            
        
        elif(tipo == "dynamic"):
            todosLosJuegos = DataStructures.Array_Dinamic()
            for row in csvTodosLosJuegos:
                juego = DataStructures.Array_Dinamic()
                for campo in row:
                    juego.pushBack(campo)
                todosLosJuegos.pushBack(juego)   

    return todosLosJuegos

def cargarUsuarios(total , tipo):
    with open(database_path + '\\users.csv', newline="" , encoding='utf-8') as csvfile:
        coleccionUsuarios = csv.reader(csvfile, delimiter=',')
        next(coleccionUsuarios)

        if(tipo == "linked"):
            todosLosUsuarios = DataStructures.LinkedList()                    
            contador = 0
            while contador<total:
                usuario = DataStructures.LinkedList()
                for campo in next(coleccionUsuarios):
                    usuario.pushBack(campo)
                todosLosUsuarios.pushBack(usuario)  
                contador += 1

        elif(tipo == "dynamic"):
            todosLosUsuarios = DataStructures.Array_Dinamic()
            contador = 0
            while contador<total:
                usuario = DataStructures.Array_Dinamic()
                for campo in next(coleccionUsuarios):
                    usuario.pushBack(campo)
                todosLosUsuarios.pushBack(usuario)  
                contador += 1
            
        
        return todosLosUsuarios

def cargarDuplaUserPassword(tipo, user, password):
    if( tipo == "linked"):
        userPassword = DataStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        userPassword = DataStructures.Array_Dinamic()
        
    userPassword.pushBack(user)
    userPassword.pushBack(password)
    return userPassword

def agregarUsuarioEnEstructura(tipo, estructura, user, password):
    if( tipo == "linked"):
        nuevaEntrada = cargarDuplaUserPassword("linked" , user, password)
        
    elif(tipo == "dynamic"):
        nuevaEntrada = cargarDuplaUserPassword("dynamic" , user, password)

    estructura.pushFront(nuevaEntrada)   
    

def escribirUsuarioCSV(estructura):
    with open(database_path + "\\newDatabase.csv" , "w" , newline="") as outfile:
        writer = csv.writer(outfile)
        for elemento in estructura:            
            writer.writerow(elemento)


def escribirUsuarioJson(usuario):
    with open(database_path + "\\listasDeLosUsuarios.txt") as json_listas:
        listasDeUsuarios = json.load(json_listas)
        listasDeUsuarios[usuario] = {}
    with open(database_path + "\\listasDeLosUsuarios.txt" , "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

def recuperarListaUsuario(usuario, tipo):
    with open(database_path + "\\listasDeLosUsuarios.txt") as json_listas:
        listasDeUsuarios = json.load(json_listas)
    if( tipo == "linked"):
        colecciones = DataStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        colecciones = DataStructures.Array_Dinamic()

    for elemento in listasDeUsuarios[usuario]:
        colecciones.pushBack(elemento)

    return colecciones

def crearListaEnUsuario(usuario, nombreLista):
    with open(database_path + "\\listasDeLosUsuarios.txt") as json_listas:
        listasDeUsuarios = json.load(json_listas)
    listasDeUsuarios[usuario][nombreLista] = []

    with open(database_path + "\\listasDeLosUsuarios.txt", "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

    
def getContenidosLista(usuario, nom_lista, tipo):
    with open(database_path + "\\listasDeLosUsuarios.txt") as json_listas:
        listasDeUsuarios = json.load(json_listas)
        contenidos = listasDeUsuarios[usuario][nom_lista]

    if( tipo == "linked"):
        colecciones = DataStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        colecciones = DataStructures.Array_Dinamic()
    
    for elemento in contenidos:
        colecciones.pushBack(elemento)
    
    return colecciones

def escribirContenidosLista(usuario, nom_lista, slug, agregar):
    with open(database_path + "\\listasDeLosUsuarios.txt") as json_listas:
        listasDeUsuarios = json.load(json_listas)
        contenidos = listasDeUsuarios[usuario][nom_lista]

    if slug in contenidos and agregar == False:
        contenidos.remove(slug)
    elif slug not in contenidos and agregar == True:
        contenidos.append(slug) 

    with open(database_path + "\\listasDeLosUsuarios.txt", "w") as outfile:
        json.dump(listasDeUsuarios, outfile)
    

def gameInCollection(nombre_juego, todosLosJuegos):
    game = None
    for juego in todosLosJuegos:
        if nombre_juego == juego.getElement(1):            
            game = juego    
            break
    return game

def actualizarListasEnJSON(usuario, colecciones):
    with open(database_path + "\\listasDeLosUsuarios.txt") as json_listas:
        listasDeUsuarios = json.load(json_listas)
    for lista in listasDeUsuarios[usuario]:
        if colecciones.find(lista) == -1:
            del listasDeUsuarios[usuario][lista]
            break
    
    with open(database_path + "\\listasDeLosUsuarios.txt", "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

def searchGame(nombre, juegos, tipo):
    if( tipo == "linked"):
        resultado = DataStructures.LinkedList()
        
    elif( tipo == "dynamic"):
        resultado = DataStructures.Array_Dinamic()

    for juego in juegos:
        if nombre.lower() in juego.getElement(0).lower():
            resultado.sortedInsertion(juego)
    
    return resultado


    

        




    


#end = time.time()
#print(end-start)
