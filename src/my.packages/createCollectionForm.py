import sys,os,pathlib
from pathlib import Path
flaskwtf_path = base_path = Path(__file__).parent.parent.parent
flask_path = os.path.join(base_path, './lib/wtforms' )
sys.path.append(flaskwtf_path)

from wtforms import Form
from wtforms import StringField, TextField, PasswordField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class CreateCollecion(Form):
    nombreColeccion = StringField('Coleccion', 
            [
                validators.DataRequired(message= 'El nombre es requerido'),
                validators.length(min=1, max=25, message="La lista no debe tener nombre vacío")                 
            ],
            render_kw={"placeholder": "Nombre"}
            )
    