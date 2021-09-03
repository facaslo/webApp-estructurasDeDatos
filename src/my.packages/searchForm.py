import loadModules as lm
lm.loadModuleWTForms()

from wtforms import Form
from wtforms import StringField, TextField, PasswordField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class searchForm(Form):
    gameName = StringField('Name', 
            [
                validators.DataRequired(message= 'El nombre del juego es requerido')
            ],
            render_kw={"placeholder": "Nombre del juego"}
            )