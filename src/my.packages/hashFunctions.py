import ctypes
import hashlib
from os import urandom

def rsHash(string):
    b = 378551
    a = 63689
    hash = 0
    i = 0

    for i in range(len(string)):
        # Ord regresa el código de unicode
        hash = hash * a + ord(string[i])
        a = a*b
    
    # Para truncar a 32 bits el hash
    return ctypes.c_int32(hash).value
    #return hash


Hash = lambda key, size : rsHash(key) % size
SecondHash = lambda slot,i,key,p,size : (slot + i * (1 + rsHash(key) % p)) % size
LinearProbing = lambda slot,i,size : (slot + i) % size
QuadraticProbing = lambda slot,i,size : (slot + i**2) % size
#Para generar una sal para agregarle a la contraseña hasheada.
generateSalt = lambda : urandom(32)
# Esta función no se utilizara para almacenar en la tabla hash, tan solo para almacenar la contraseña hasheada en el csv y hacer validaciones.
hashPassword = lambda password, salt:  hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100)

# Salt y expected hash se leeran de un fichero y están codificados de manera hexadecimal
def verifyPasswordHash( password, salt , expectedHash):    
    hash = hashPassword(password, bytes.fromhex(salt))    
    return hash == bytes.fromhex(expectedHash)
    