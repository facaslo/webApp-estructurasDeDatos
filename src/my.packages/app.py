import sys,os,pathlib
from pathlib import Path

base_path = Path(__file__).parent.parent.parent
flask_path = os.path.join(base_path, '.\\lib\\Flask-1.1.2\\src' )
sys.path.append(flask_path)

from flask import Flask
from flask import redirect
from flask import render_template 
from flask import request
from flask import make_response
from flask import session
from flask import redirect
from flask import url_for
from flask import flash

import loginForm as lf
import registerForm as rf
import createCollectionForm as cf
import searchForm as sf
import manageData 
import DataStructures
import csv

app = Flask(__name__, template_folder='templates')
app.secret_key = "llave"

tipo = "dynamic"
juegos = manageData.cargarBaseJuegos(tipo)  
usuarios = manageData.cargarUsuarios(5000, tipo)
colecciones = None
autentication = False  

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html") , 404


@app.route('/')
def index():    
    if 'username' in session:
        username = session['username']        
    return render_template('index.html')

@app.route('/login' , methods = ['GET','POST'])
def login():    
    form = lf.LoginForm(request.form)    
    loginMessage = request.args.get("message" , "")  
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data        
       
        insertedInfo = manageData.cargarDuplaUserPassword(tipo, username, password)       

        if usuarios.find(insertedInfo) != -1:                         
            session['username'] = username 
            global colecciones
            colecciones = manageData.recuperarListaUsuario(username, tipo) 
            global autentication 
            autentication = True
            return redirect('/user?id={}'.format(username), code=302)           
    
    return render_template('login.html', form = form, mensaje = loginMessage)    

@app.route('/logout')
def logout():    
    if 'username' in session:
        session.pop('username')
        global autentication
        autentication = False
        global colecciones
        colecciones = None
    return redirect('/')
  
@app.route('/register' , methods = ['GET','POST'])
def register():    
    form = rf.RegisterForm(request.form)      
    registerMessage = request.args.get("message", "")    

    if request.method == 'POST' and form.validate():
        user = form.username.data
        password = form.password.data
        message = "El usuario ha sido creado"                        
        for usuario in usuarios:
            if usuario.getElement(0) == user:
                message = "El usuario ya existe"   
                password = form.password.data  
                return redirect('/register?message={}'.format(message), code=302)
        
        
        manageData.agregarUsuarioEnEstructura(tipo , usuarios , user , password)
        manageData.escribirUsuarioCSV(usuarios)
        manageData.escribirUsuarioJson(user)

        return redirect('/login?message={}'.format(message), code=302)
              
    return render_template('register.html', form = form, mensaje = registerMessage)

@app.route('/user' , methods = ['GET','POST'])
def usuario():    
    userParametro = request.args.get('id')        
    
    if autentication and userParametro == session['username']:     
               
        return render_template('user.html', usuario = userParametro , listaX = colecciones)
    else:
        return render_template('401.html'), 401

@app.route('/<id>/crearColeccion' , methods = ['GET','POST'])
def crearColeccion(id):   
    form = cf.CreateCollecion (request.form)       
    crearColeccionMessage = request.args.get("message", "") 

    if autentication and id == session['username']:
        if request.method == 'POST' and form.validate():
            if form.nombreColeccion.data not in colecciones:
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
    juego = request.args.get("juego", "")         

    coleccion = manageData.getContenidosLista(id,lista, tipo)

    if tipo == "linked":
        nombresColeccion = DataStructures.LinkedList()
    elif tipo == "dynamic":
        nombresColeccion = DataStructures.Array_Dinamic()   

    for elemento in coleccion:
        nombresColeccion.pushBack(manageData.gameInCollection(elemento, juegos).getElement(0))   
    
    if autentication and id == session['username']:        
        if juego == "":            
            return render_template('collection.html',  listaX = coleccion, nombre= lista , nombreUser = id , nombreJuegos = nombresColeccion)
        else: 
            
            infoJuego = manageData.gameInCollection(juego, juegos)          
            if infoJuego == None:    
                return render_template('404.html'), 404    
            return render_template("juegoLista.html", info_juego = infoJuego, slug = infoJuego.getElement(1), nombre_Juego = infoJuego.getElement(0), nombre_lista= lista, id=id) 

    else:
        return render_template('401.html'), 401

@app.route('/<id>/<lista>/eliminar_coleccion' , methods = ['GET','POST'])
def eliminar(id, lista):   
    if autentication and id == session['username']:  
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
    if autentication and id == session['username']:
        if request.method == 'POST' and form.validate():
            busqueda = form.gameName.data

            resultado = manageData.searchGame(busqueda, juegos, tipo)                  

            return render_template('search.html' , form = form, resultados=resultado, id= id, nombreLista = lista)
        else:
            return render_template('search.html', form = form)
    else:
        return render_template('401.html'), 401

@app.route('/<id>/<lista>/search/<slug_juego>' , methods = ['GET','POST'])
def Juego(id, lista, slug_juego): 
    
    if autentication and id == session['username']: 
        for elemento in juegos:
            if elemento.getElement(1) == slug_juego:
                juego = elemento
        return render_template("juegoResultado.html", info_juego = juego, id=id , nombre_lista=lista, slug=slug_juego)

        
    else:
        return render_template('401.html'), 401 

@app.route('/<id>/<lista>/search/<slug_juego>/agregarJuego' , methods = ['GET','POST'])
def agregarJuego(id, lista, slug_juego): 
    if autentication and id == session['username']: 
        manageData.escribirContenidosLista(id,lista, slug_juego, True)
        return redirect('/{}/{}'.format(id,lista))
    else:
        return render_template('401.html'), 401 

@app.route('/<id>/<lista>/<slug_juego>/eliminarJuego' , methods = ['GET','POST'])
def eliminarJuego(id, lista, slug_juego): 
    if autentication and id == session['username']: 
        manageData.escribirContenidosLista(id,lista, slug_juego, False)
        return redirect('/{}/{}'.format(id,lista))
    else:
        return render_template('401.html'), 401 


if __name__ == '__main__' :
    app.run(debug = True, port = 8000)

