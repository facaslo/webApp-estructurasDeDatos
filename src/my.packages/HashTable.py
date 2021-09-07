import math
from SequentialStructures import LinkedList
from ctypes import c_int32
from hashFunctions import Hash, SecondHash, LinearProbing, QuadraticProbing

class Node:
    def __init__(self,key,data):
        self.key = key
        self.data = data
    def GetKey(self):
        return self.key
    def GetData(self):
        return self.data        

class hashTable:
    def __init__(self, numberOfKeys):
        self.loadFactor = 0
        self.numberOfCollisions = 0    
        self.flag = "***"    
        self.numberOfBuckets = math.ceil(numberOfKeys/0.75)
        self.arr = [None for i in range(self.numberOfBuckets)]        
     
    def InsertKey(self, key, data, chaining = False,probingMethod="doubleHashing"):       
        
        slot = Hash(key , self.numberOfBuckets)
        if not chaining:
            if self.arr[slot] is not None and self.arr[slot]!=self.flag:            
                i = 1
                if probingMethod == "doubleHashing" :                
                    while self.arr[slot] is not None and self.arr[slot] != self.flag :
                        self.numberOfCollisions += 1
                        slot = SecondHash(slot,i,key, self.numberOfBuckets//2 , self.numberOfBuckets)                            
                        i += 1            
                        
                elif probingMethod == "linearProbing":
                    while self.arr[slot] is not None and self.arr[slot] != self.flag :
                        self.numberOfCollisions += 1
                        slot = LinearProbing(slot,i, self.numberOfBuckets)
                        i += 1
                elif probingMethod == "quadraticProbing":
                    while self.arr[slot] is not None and self.arr[slot] != self.flag :
                        self.numberOfCollisions += 1
                        slot = QuadraticProbing(slot,i, self.numberOfBuckets)
                        i += 1

            self.arr[slot] = Node(key,data)   
            self.loadFactor += 1/self.numberOfBuckets                   
            

        else:
            if self.arr[slot] is None:
                list = LinkedList()
                list.pushBack(Node(key,data))
                self.arr[slot] = list
                self.loadFactor += 1/self.numberOfBuckets      
            
            else:
                self.numberOfCollisions += 1
                self.arr[slot].pushBack(Node(key,data))
              
        

    def getDataFromKey(self,key, chaining = False, probingMethod = "doubleHashing" ):
        slot = Hash(key , self.numberOfBuckets)

        data = None
        
        if not chaining:
            if self.arr[slot] is not None and self.arr[slot] != self.flag: 
                if self.arr[slot].GetKey() == key:
                    data = self.arr[slot].GetData()
            
                else:
                    i = 1
                    if probingMethod == "doubleHashing" :                
                        while self.arr[slot] is not None:                    
                            try:
                                if self.arr[slot].GetKey() == key:
                                    data = self.arr[slot].GetData()
                                    break
                            except:
                                pass                        
                                
                            slot = SecondHash(slot,i,key, self.numberOfBuckets//2, self.numberOfBuckets)                            
                            i += 1 
                            
                    elif probingMethod == "linearProbing":
                        while self.arr[slot] is not None :
                            try:
                                if self.arr[slot].GetKey() == key:
                                    data = self.arr[slot].GetData()
                                    break
                            except:
                                pass                      
                            slot = LinearProbing(slot,i, self.numberOfBuckets)
                            i += 1

                    elif probingMethod == "quadraticProbing":
                        while self.arr[slot] is not None:
                            try:
                                if self.arr[slot].GetKey() == key:
                                    data = self.arr[slot].GetData()
                                    break
                            except:
                                pass               
                                
                            slot = QuadraticProbing(slot,i, self.numberOfBuckets)
                            i += 1
        
        else:
            if self.arr[slot] is not None:              
            
                for elemento in self.arr[slot]:
                    if elemento.data.GetKey() == key:
                        data = elemento.data.GetData()
                        break           
            
        return data
    
    def HasKey(self, key, chaining = False, probingMethod="doubleHashing"):
        return self.getDataFromKey(key,chaining,probingMethod) is not None
        
        
    def DeleteKey(self, key, chaining = False, probingMethod="doubleHashing"):

        slot = Hash(key , self.numberOfBuckets)
        if self.arr[slot] is not None and self.arr[slot] != self.flag:            
            if self.arr[slot].GetKey() == key:
                self.arr[slot] = self.flag
            
        else:
            i = 1
            if probingMethod == "doubleHashing" :                
                while self.arr[slot] is not None:                    
                    try:
                        if self.arr[slot].GetKey() == key:
                            self.arr[slot] == None
                            break
                    except:
                        pass                        
                        
                    slot = SecondHash(slot,i,key, self.numberOfBuckets//2, self.numberOfBuckets)                            
                    i += 1 
                    
            elif probingMethod == "linearProbing":
                while self.arr[slot] is not None :
                    try:
                        if self.arr[slot].GetKey() == key:
                            self.arr[slot] == None
                            break
                    except:
                        pass                      
                    slot = LinearProbing(slot,i, self.numberOfBuckets)
                    i += 1

            elif probingMethod == "quadraticProbing":
                while self.arr[slot] is not None:
                    try:
                        if self.arr[slot].GetKey() == key:
                            self.arr[slot] == None
                            break
                    except:
                        pass               
                           
                    slot = QuadraticProbing(slot,i, self.numberOfBuckets)
                    i += 1
            
            
############################################################################

# lista = ["HOla" , "Soy" , "Programador" , "d" , "f"]
# table = hashTable(len(lista))

# for entrada in lista:
#     table.InsertKey(entrada, entrada+"-valor", True)

# print(table.HasKey("Soy", True))
# print(table.getDataFromKey("zoy",True))



# print(table.numberOfCollisions)

# for elemento in table.arr:
#     print()
#     try:
#         for entrada in elemento:
#             print(entrada.data.GetData(), end=" ")        
#     except:
#         print(elemento, end=" ")



