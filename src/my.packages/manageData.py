import sys,os
import json

from werkzeug import datastructures
import SequentialStructures
import TreeStructures
import HashTable
import csv
import time
from pathlib import Path
from hashFunctions import verifyPasswordHash, generateSalt, hashPassword

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
        users_path = os.path.join(base_path, './data/Users.csv' )
    else:
        users_path = os.path.join(base_path, '.\\data\\Users.csv' )
    return users_path

def getUsersListPath():
    base_path = Path(__file__).parent.parent.parent
    if sys.platform.startswith('linux'):
        users_path = os.path.join(base_path, './data/listasDeLosUsuarios.txt' )
    else:
        users_path = os.path.join(base_path, '.\\data\\listasDeLosUsuarios.txt' )
    return users_path

# Métodos de registro

def verificarExistenciaUsuario(tablaHash,username,encadenado=False, tipoSondeo = "doubleHashing"):    
    print("Verificando si el usuario está disponible ...")
    if tablaHash.HasKey(username,encadenado,tipoSondeo):
        print("El usuario ya existe.")
        return True
    else:
        print("El usuario está disponible.")
        return False
    

def escribirUsuarioCSV(username,password, total, encadenado = False ,tipoSondeo="doubleHashing"):    
    nuevaEntrada = SequentialStructures.Array_Dinamic()
    nuevaEntrada.Append(username)
    salt = generateSalt()
    nuevaEntrada.Append(salt.hex())
    hashedPassword = hashPassword(password,salt)
    nuevaEntrada.Append(hashedPassword.hex())       

    with open( getUsersPath(), "a" , newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(nuevaEntrada)  

# Métodos de login

def cargarUsuarios(total, encadenado = False ,tipoSondeo="doubleHashing"):
    start = time.time()
    with open(getUsersPath(), newline="" , encoding='utf-8') as csvfile:
        coleccionUsuarios = csv.reader(csvfile, delimiter=',')           
        todosLosUsuarios = HashTable.hashTable(total)        
        print("Agregando usuarios ...")
        
        numeroUsuarios = 0
        for fila in coleccionUsuarios: 
            print ("Numero de usuarios cargados {}".format(numeroUsuarios))
            if numeroUsuarios == total:
                break
            contador = 0
            entradaUsuario = SequentialStructures.Array_Dinamic()
            llave = None
            for columna in fila:
                if contador == 0:
                    llave = columna
                else:                    
                    entradaUsuario.pushBack(columna)
                contador += 1    
                    
            todosLosUsuarios.InsertKey(llave,entradaUsuario, chaining = encadenado, probingMethod = tipoSondeo)                  
            numeroUsuarios += 1

        print("Usuarios agregados.")
        
        end = time.time()
        tiempo = end - start
        print("Tiempo de creación de tabla hash: {} ".format(tiempo))
        return todosLosUsuarios

def verificarValidezUsuario(tablaHash,username,password, encadenado=False, tipoSondeo = "doubleHashing"):
    print("Verificando usuario y contraseña ...")
    verificado = False
    datosUsuario = tablaHash.getDataFromKey(username, chaining = encadenado, probingMethod = tipoSondeo)    
    if datosUsuario is not None:
        salt = datosUsuario.getElement(0)
        expectedHash = datosUsuario.getElement(1)
        verificado = verifyPasswordHash(password, salt, expectedHash)
    
    print("Verificación finalizada.")
    return verificado

# Método de cargar base de juegos

def cargarBaseJuegos(tipoArbol, totalJuegos): 
    todosLosJuegos = SequentialStructures.Array_Dinamic()
    print("Cargando bases de juegos ...")
    with open(getGamesPath(), newline="" , encoding='utf-8') as csvfile:

        start = time.time()
        csvTodosLosJuegos = csv.reader(csvfile, delimiter=',')
        next(csvTodosLosJuegos)        
        juegosAgregados = 0

        if tipoArbol == "heap":

            print("Agregando juegos al heap ...")
            
            heap = TreeStructures.BinaryHeap()       
            
            for row in csvTodosLosJuegos:                            
                if juegosAgregados == totalJuegos:
                    break
                juego = SequentialStructures.Array_Dinamic()
                for campo in row:
                    juego.pushBack(campo)
                heap.insert(juego)                
                juegosAgregados += 1
                               
            
            print("Ordenando los juegos con heap sort...")

            while heap.size >= 0:
                todosLosJuegos.pushFront(heap.extractMax())   
            
        elif tipoArbol == "avl":
            print("Agregando juegos al AVL ...")
            avltree = TreeStructures.AVL()
            root = None            

            for row in csvTodosLosJuegos:                         
                if juegosAgregados == totalJuegos:
                    break
                juego = SequentialStructures.Array_Dinamic()
                for campo in row:
                    juego.pushBack(campo)         
                
                root = avltree.insert(root, juego)
                juegosAgregados += 1
            
            print("Ordenando los juegos con el inorder del AVL...")
            avltree.inOrderReturn(todosLosJuegos, root)
        
        end = time.time()
        print("El tiempo tardado en ordenar la base es: {}".format(end-start))
    print("Base de juegos cargada.")
    return todosLosJuegos
    

# Metodos para las colecciones de los usuarios.

def escribirUsuarioJson(usuario):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
        listasDeUsuarios[usuario] = {}
    with open(getUsersListPath(), "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

def recuperarListaUsuario(usuario):
    colecciones = SequentialStructures.LinkedList() 
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
        if usuario not in listasDeUsuarios:
            escribirUsuarioJson(usuario)
        else:            
            for elemento in listasDeUsuarios[usuario]:
                colecciones.pushBack(elemento)
    return colecciones


def crearListaEnUsuario(usuario, nombreLista):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
    listasDeUsuarios[usuario][nombreLista] = []
    with open(getUsersListPath(), "w") as outfile:
        json.dump(listasDeUsuarios, outfile)



def getContenidosLista(usuario, nom_lista):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
        contenidos = listasDeUsuarios[usuario][nom_lista]
        colecciones = SequentialStructures.Array_Dinamic()    
    for elemento in contenidos:
        colecciones.pushBack(elemento)
    
    return colecciones

# Actualizar fichero json con las nuevas colecciones
def actualizarListasEnJSON(usuario, colecciones):
    with open(getUsersListPath()) as json_listas:
        listasDeUsuarios = json.load(json_listas)
    for lista in listasDeUsuarios[usuario]:
        if colecciones.find(lista) == -1:
            del listasDeUsuarios[usuario][lista]
            break    
    with open(getUsersListPath(), "w") as outfile:
        json.dump(listasDeUsuarios, outfile)

# Actualizar elementos de una colección
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
    
# Verificar si un juego está en la colección de un usuario
def gameInCollection(nombre_juego, todosLosJuegos):
    game = None
    for juego in todosLosJuegos:
        if nombre_juego == juego.getElement(1):            
            game = juego    
            break
    return game

# Usaremos divideAndConquer para hacer una busqueda de múltiples elementos que comiencen por value
def divideAndConquer(dynamicArray, value):    
    print("Buscando juegos ...")
    resultado = SequentialStructures.Array_Dinamic() 

    index = dynamicArray.Size // 2         
    # por cuanto se va a incrementar o decrementar un intervalo        
    paso = dynamicArray.Size // 2         
    # Indice del primer elemento encontrado
    foundIndex = -1

    while paso > 0:
        compareTo = dynamicArray.getElement(index)
        if compareTo.getElement(0).lower().startswith(value.lower()):
            foundIndex = index
            resultado.Append(compareTo)
            break
        else:            
            paso = paso // 2
            print(paso)
            if value.lower() < compareTo.getElement(0).lower():        
                index -= paso

            elif value.lower() > compareTo.getElement(0).lower():
                index += paso

    if not resultado.IsEmpty():
        # Buscar hacia atrás del resultado encontrado
        while index >= 0:
            index -= 1            
            elemento = dynamicArray.getElement(index)
            if not elemento.getElement(0).lower().startswith(value.lower()):
                break
            else:
                resultado.pushFront(elemento)
            
        index = foundIndex
        # Buscar hacia delante del resultado encontrado
        while index < dynamicArray.size():
            index += 1
            elemento = dynamicArray.getElement(index)
            if not elemento.getElement(0).lower().startswith(value.lower()):
                break
            else:
                resultado.pushBack(elemento)

    print("Juegos encontrados.")    
    return resultado      


def searchGame(cadenaBusqueda, baseJuegos):        
    return divideAndConquer(baseJuegos, cadenaBusqueda)   

    

