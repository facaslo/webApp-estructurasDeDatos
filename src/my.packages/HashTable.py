import math
from ctypes import c_int32

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
    return c_int32(hash) 



class hashTable:
    def __init__(self,buckets):
        self.loadFactor = 0
        self.arr = [None for i in range(math.ceil(buckets/0.75))]            

    def hashmethod(self, type):
        pass        
    
