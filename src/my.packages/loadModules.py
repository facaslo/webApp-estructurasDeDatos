import sys,os
from pathlib import Path

def loadModuleFlask():
    base_path = Path(__file__).parent.parent.parent
    if sys.platform.startswith('linux'):
        flask_path = os.path.join(base_path, './lib/Flask-1.1.2/src' )
    else:
        flask_path = os.path.join(base_path, '.\\lib\\Flask-1.1.2\\src' )
    sys.path.insert(0,flask_path)

def loadModuleWTForms():
    base_path = Path(__file__).parent.parent.parent
    if sys.platform.startswith('linux'):
        wtforms_path = os.path.join(base_path, './lib' )
    else:
        wtforms_path = os.path.join(base_path, '.\\lib' )
    sys.path.insert(0,wtforms_path)

def loadModuleRequests():
    base_path = Path(__file__).parent.parent.parent
    if sys.platform.startswith('linux'):
        wtforms_path = os.path.join(base_path, './lib' )
    else:
        wtforms_path = os.path.join(base_path, '.\\lib' )
    sys.path.insert(0,wtforms_path)
