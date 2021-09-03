import loadModules as lm
lm.loadModuleWTForms()

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
    