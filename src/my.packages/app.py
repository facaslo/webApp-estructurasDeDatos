import sys,os,pathlib
from pathlib import Path

base_path = Path(__file__).parent.parent.parent
flask_path = os.path.join(base_path, '.\\lib\\Flask-1.1.2\\src' )
sys.path.append(flask_path)

from flask import Flask
from flask import render_template 
from flask import request
import loginForm as lf
import registerForm as rf

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():       
    return render_template('index.html')

@app.route('/login' , methods = ['GET','POST'])
def login():    
    form = lf.LoginForm(request.form)  
    
    if request.method == 'POST' and form.validate():
        user = form.username.data
        password = form.password.data    
        
    else:
        print("Error en el formulario")        

    return render_template('login.html', form = form)

@app.route('/register' , methods = ['GET','POST'])
def register():    
    form = rf.RegisterForm(request.form)  
    
    if request.method == 'POST' and form.validate():
        user = form.username.data
        password = form.password.data    
        
    else:
        print("Error en el formulario")        

    return render_template('register.html', form = form)

@app.route('/user' , methods = ['GET','POST'])
def usuario():    
    lista = ["ColeccionA", "ColeccionB", "ColeccionC"]
    return render_template('user.html',  coleccion = lista )

@app.route('/usuario/infojuego' , methods = ['GET','POST'])
def juego():    
    lista = ["JuegoA"
    "https://estaticos.muyinteresante.es/media/cache/760x570_thumb/uploads/images/article/5d2dadd45cafe83452ba52d7/game-development-2.jpg",
    "Descripción de juego A"] 
    return render_template('user.html',  coleccion = lista)


if __name__ == '__main__' :
    app.run(debug = True, port = 8000)

