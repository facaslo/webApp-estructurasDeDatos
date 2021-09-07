import loadModules as lm
lm.loadModuleFlask()

from flask import Flask
from flask import redirect
from flask import render_template 
from flask import request
from flask import session
from flask import redirect

import loginForm as lf
import registerForm as rf
import createCollectionForm as cf
import searchForm as sf
import manageData 
import SequentialStructures
import time

app = Flask(__name__, template_folder='templates')
app.secret_key = "llave"

#Tipo de estructura de árbol 
tipoArbol = "avl"
# Total de usuarios para cargar, determina el tamaño de la tabla hash
totalUsuarios = 100000
# Límite de juegos para cargar en la base
limiteJuegos = 10000
# Parámetros para saber como lidiar con las colecciones de la tabla hash de usuarios
tipoSondeo = "linearProbing"
encadenamiento = False
# Arreglo dinámico ordenado por un heap o avl, que contendrá la información de los juegos
baseJuegos = None
# Tabla Hash que contendrá la información de los usuarios
usuarios = None
# Lista enlazada que contendrá los nombres de las colecciones de juegos
colecciones = None

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html") , 404

@app.route('/')
def index():         
    # Cargar la base de juegos 
    global baseJuegos
    if baseJuegos is None:
        baseJuegos = manageData.cargarBaseJuegos(tipoArbol,limiteJuegos)
        
    return render_template('index.html')

@app.route('/login' , methods = ['GET','POST'])
def login():     
    start = time.time()  
    # Cargar base de usuarios si no está cargada 
    global usuarios,totalUsuarios    
    if usuarios is None:
        usuarios = manageData.cargarUsuarios(totalUsuarios,encadenamiento, tipoSondeo )
        print ("Número de colisiones: {}".format(usuarios.numberOfCollisions))
    
    # Verificar y obtener información de formularios
    form = lf.LoginForm(request.form)    
    loginMessage = request.args.get("message" , "")      
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data 
        
        #Verificar si el usuario existe y la contraseña es la correspondiente
        if manageData.verificarValidezUsuario(usuarios,username,password, encadenamiento , tipoSondeo):                 
            session['username'] = username 
            end = time.time()
            tiempo = end - start
            print("Tiempo transcurrido login: {}".format(tiempo))
            
            global colecciones
            colecciones = manageData.recuperarListaUsuario(username) 
            session["autentication"] = True                     
            
            return redirect('/user?id={}'.format(username), code=302)    
        else:
            error = "Usuario o contraseña incorrectos"
            return redirect('/login?message={}'.format(error))                    
    
    return render_template('login.html', form = form, mensaje = loginMessage)    

@app.route('/logout')
def logout():    
    if 'username' in session:
        session.pop('username')
        session.pop('autentication')   

        global colecciones
        colecciones = None
    return redirect('/')
  
@app.route('/register' , methods = ['GET','POST'])
def register():    
    # Cargar base de usuarios si no está cargada
    global usuarios,totalUsuarios
    if usuarios is None:
        usuarios = manageData.cargarUsuarios(totalUsuarios)
    form = rf.RegisterForm(request.form)      
    registerMessage = request.args.get("message", "")    
    
    #Verificar si el usuario existe y la contraseña es la correspondiente
    if request.method == 'POST' and form.validate():
        user = form.username.data
        password = form.password.data        
        
        # verificar si el usuario ya está tomado
        if manageData.verificarExistenciaUsuario(usuarios,user,encadenamiento ,tipoSondeo):                        
            message = "El usuario ya existe"
            return redirect('/register?message={}'.format(message), code=302)

        # Crear usuario y escribirlo en el csv, redirigir a la pantalla de login
        else:
            message = "El usuario ha sido creado"                        
            manageData.escribirUsuarioCSV(user,password,totalUsuarios,encadenamiento,tipoSondeo)   
            usuarios = None                                               
            return redirect('/login?message={}'.format(message), code=302)
              
    return render_template('register.html', form = form, mensaje = registerMessage)

@app.route('/user' , methods = ['GET','POST'])
def usuario():    
    userParametro = request.args.get('id')       
    
    #Autenticar el usuario
    if session["autentication"] and userParametro == session['username']: 
        # Limpiar la tabla hash de usuarios de la memoria
        global usuarios
        usuarios = None       

        return render_template('user.html', usuario = userParametro , listaX = colecciones)        
    else:
        return render_template('401.html'), 401

@app.route('/<id>/crearColeccion' , methods = ['GET','POST'])
def crearColeccion(id):   
    
    # Formulario para crear colección
    form = cf.CreateCollecion (request.form)       
    crearColeccionMessage = request.args.get("message", "") 
    
    if session["autentication"] and id == session['username']:
        if request.method == 'POST' and form.validate():            
            if colecciones.empty():
                colecciones.pushBack(form.nombreColeccion.data)
                manageData.crearListaEnUsuario(id,form.nombreColeccion.data)
                return redirect("/user?id={}".format(id), code=302)
            else:
                #Asegurarse de que cada colección sea única
                for coleccion in colecciones:
                    if form.nombreColeccion.data != coleccion.data:                    
                        colecciones.pushBack(form.nombreColeccion.data)
                        manageData.crearListaEnUsuario(id,form.nombreColeccion.data)
                        return redirect("/user?id={}".format(id), code=302)
                    else:
                        mensaje = "La lista ya existe"
                        return redirect("/{}/crearColeccion?message={}".format(id,mensaje), code=302)
        
        return render_template('createCollection.html', form = form, mensaje = crearColeccionMessage, id = id)
    else:
        return render_template('401.html'), 401
    
@app.route('/<id>/<lista>' , methods = ['GET','POST'])
def coleccionJuegos(id, lista):    
    # Si no se especifica el parámetro juego, este es vacío por defecto
    juego = request.args.get("juego", "")             
    coleccion = manageData.getContenidosLista(id,lista)

    nombresColeccion = SequentialStructures.LinkedList()  
    
    # Cargar los elementos de la colección a nombresColeccion, para pasarlo al html
    for elemento in coleccion:
        nombresColeccion.pushBack(manageData.gameInCollection(elemento, baseJuegos).getElement(0))   
    
    if session["autentication"] and id == session['username']:        
        if juego == "":            
            return render_template('collection.html',  listaX = coleccion, nombre= lista , nombreUser = id , nombreJuegos = nombresColeccion)
        else:             
            infoJuego = manageData.gameInCollection(juego, baseJuegos)          
            if infoJuego == None:    
                return render_template('404.html'), 404    
            return render_template("juegoLista.html", info_juego = infoJuego, slug = infoJuego.getElement(1), nombre_Juego = infoJuego.getElement(0), nombre_lista= lista, id=id) 
    else:
        return render_template('401.html'), 401

@app.route('/<id>/<lista>/eliminar_coleccion' , methods = ['GET','POST'])
def eliminar(id, lista):   
    # Autenticar usuario
    if session["autentication"] and id == session['username']:  
        # Verificar existencia de la colección y borrarla de existir
        isInCollection = colecciones.find(lista)         
        if isInCollection != -1:
            colecciones.erase(isInCollection)
            manageData.actualizarListasEnJSON(id,colecciones)
        return redirect('/user?id={}'.format(id))    
    else:
        return render_template('401.html'), 401

@app.route('/<id>/<lista>/search' , methods = ['GET','POST'])
def buscarJuego(id, lista):
    form = sf.searchForm(request.form)
    # Autenticar usuario
    if session["autentication"] and id == session['username']:
        # Si se llenó el formulario de manera valida
        if request.method == 'POST' and form.validate():
            busqueda = form.gameName.data            
            resultado = manageData.searchGame(busqueda , baseJuegos)                  
            return render_template('search.html' , form = form, resultados=resultado, id= id, nombreLista = lista)
        else:
            return render_template('search.html', form = form)
    else:
        return render_template('401.html'), 401

@app.route('/<id>/<lista>/search/<slug_juego>' , methods = ['GET','POST'])
def Juego(id, lista, slug_juego): 
    # Autenticar usuario
    if session["autentication"] and id == session['username']:         
        # Obtener la información del juego
        for elemento in baseJuegos:
            if elemento.getElement(1) == slug_juego:
                juego = elemento
        return render_template("juegoResultado.html", info_juego = juego, id=id , nombre_lista=lista, slug=slug_juego)
        
    else:
        return render_template('401.html'), 401 

@app.route('/<id>/<lista>/search/<slug_juego>/agregarJuego' , methods = ['GET','POST'])
def agregarJuego(id, lista, slug_juego): 
    # Autenticar usuario
    if session["autentication"] and id == session['username']: 
        manageData.escribirContenidosLista(id,lista, slug_juego, True)
        return redirect('/{}/{}'.format(id,lista))
    else:
        return render_template('401.html'), 401 

@app.route('/<id>/<lista>/<slug_juego>/eliminarJuego' , methods = ['GET','POST'])
def eliminarJuego(id, lista, slug_juego): 
    # Autenticar usuario
    if session["autentication"] and id == session['username']: 
        manageData.escribirContenidosLista(id,lista, slug_juego, False)
        return redirect('/{}/{}'.format(id,lista))
    else:
        return render_template('401.html'), 401 

if __name__ == '__main__' :
    app.run(debug = True, port = 8000)