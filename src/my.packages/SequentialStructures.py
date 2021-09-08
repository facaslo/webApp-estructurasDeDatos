import math
import ctypes

class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None
        self.prev = None        

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.index = None
        self.count = 0

    def size(self):
        return self.count

    def pushFront(self, data):
        self.node = Node(data)
        self.node.next = self.head
        if self.head != None:
            self.head.prev = self.node
        self.head = self.node
        if self.tail == None:
            self.tail = self.head
        self.count += 1

    def topFront(self):
        if self.head == None:
            print("Error: lista vacía.")
            return
        return self.head.data

    def popFront(self):
        if self.head == None:
            print("Error: lista vacía.")
        else:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            self.count -= 1

    def pushBack(self, data):
        self.node = Node(data)
        if self.tail == None:
            self.tail = self.node
            self.head = self.tail
        else:
            self.tail.next = self.node
            self.node.prev = self.tail
            self.tail = self.node
        self.count += 1

    def topBack(self):
        if self.tail == None:
            print("Error: lista vacía.")
            return
        return self.tail.data
        
    def popBack(self):
        if self.head == None:
            print("Error: lista vacía.")
        elif self.head == self.tail:
            self.tail = None
            self.head = self.tail
            self.count -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1

    def find(self, data):
        self.copy = self.head
        self.index = 0
        while(self.copy != None):            
            if self.copy.data == data:
                return self.index
            self.copy = self.copy.next
            self.index += 1
        return -1

    def erase(self, index):
        if index == 0:
            self.popFront()
        elif index == self.count - 1:
            self.popBack()
        elif index > 0 and index < self.count - 1:
            self.pre = self.head
            for i in range(index-1):
                self.pre = self.pre.next
            self.dlt = self.pre.next
            self.aft = self.dlt.next
            self.pre.next = self.aft
            self.count -= 1
        else:
            print("Índice no válido")
    
    def empty(self):
        return self.head == None

    def addAfter(self, node, data):
        self.node_2 = Node(data)
        self.node_2.next = node.next
        self.node_2.prev = node
        node.next = self.node_2
        if self.node_2.next != None:
            self.node_2.next.prev = self.node_2
        if self.tail == node:
            self.tail = self.node_2
        self.count += 1

    def addBefore(self, node, data):
        self.node_2 = Node(data)
        self.node_2.next = node
        self.node_2.prev = node.prev
        node.prev = self.node_2
        if self.node_2.prev != None:
            self.node_2.prev.next = self.node_2
        if self.head == node:
            self.head = self.node_2
        self.count += 1

    def sortedInsertion(self, data , increasing= True):
        newNode = Node(data)
        if increasing:
            if self.head == None:
                self.head = newNode
                self.tail = newNode            
            elif newNode.data < self.head.data:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
            elif newNode.data > self.tail.data:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                temp = self.head.next
                while temp.data < newNode.data:
                    temp = temp.next            
                temp.prev.next = newNode
                newNode.prev = temp.prev
                temp.prev = newNode
                newNode.next = temp
        else:
            if self.head == None:
                self.head = newNode
                self.tail = newNode            
            elif newNode.data > self.head.data:
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
            elif newNode.data < self.tail.data:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                temp = self.head.next
                while temp.data > newNode.data:
                    temp = temp.next            
                temp.prev.next = newNode
                newNode.prev = temp.prev
                temp.prev = newNode
                newNode.next = temp
        self.count += 1 
           

    def impr(self):
        if self.head != None:
            self.copy = self.head
            while self.copy != None:
                if type(self.copy.data) == LinkedList:
                    self.copy.data.impr()
                else:
                    print(self.copy.data, end=' ')
                self.copy = self.copy.next
        else:
            print("Lista vacía.")
    
    def getElement(self, elementNumber):   
        if elementNumber > self.count-1 or elementNumber < 0:
            return None
        if elementNumber <= math.floor((self.count-1)/2):
            self.index = self.head
            contador = 0
            while contador < elementNumber:
                self.index = self.index.next
                contador += 1            
        else:
            self.index = self.tail
            contador = self.count-1            
            while contador > elementNumber:
                self.index = self.index.prev
                contador -= 1
        return self.index.data    

    def sortList(self, increasing):
        if self.head == None:
            print("La lista está vacía")
        elif self.head.next == None:
            print("La lista solo tiene un elemento")
        else:            
            currentNode = self.head    
            while(currentNode.next != None):  
                  
                self.index = currentNode.next   
                while(self.index != None):                          
                    if(currentNode.data > self.index.data and increasing == True):    
                        temp = currentNode.data
                        currentNode.data = self.index.data  
                        self.index.data = temp  
                    elif(currentNode.data < self.index.data and increasing == False): 
                        temp = currentNode.data
                        currentNode.data = self.index.data  
                        self.index.data = temp  
                    self.index = self.index.next    
                currentNode = currentNode.next    

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        return str(list(self))

    def __eq__(self,other):     
        equal = False 
        if isinstance(other, LinkedList):
            if self.count == other.count:
                equal = True
                for selfElement, otherElement in zip(self,other):
                    if (selfElement.data != otherElement.data):
                        equal = False
                        break
        return equal
    
    def lessThan(self,other,i):
        lessThan = False
        if self.count == other.count and self.count > 0 and self.getElement(i) < other.getElement(i):
            lessThan = True
        return lessThan
    
    def __lt__(self, other):
        lessThan = False
        if isinstance(other, LinkedList) and self.count == other.count and self.count > 0:
            if self.getElement(0) < other.getElement(0):
                lessThan = True
        return lessThan

#############################################################


class Array_Dinamic():

    def __init__(self, capacity = 1):
        if type(capacity) != int:
            raise ValueError("La capacidad debe ser un número")
        self.Size = 0
        self.capacity = capacity
        self.ArrayType = ctypes.py_object * capacity
        self.Arr = self.ArrayType()

    def getElement(self, Index):
        if Index > self.Size or Index < 0:
            raise IndexError("Indice fuera del rango")
        return self.Arr[Index]

    def Set(self, Index, Value):
        if Index > self.Size or Index < 0:
            raise IndexError("Indice fuera del rango")
        if self.Arr[Index] == None:
            self.Size += 1
        self.Arr[Index] = Value
    
    def insertInPosition(self, position, value):
        if position > self.Size or position < 0:
            raise IndexError("Indice fuera del rango")
        if self.Size == self.capacity:
            self.ArrayType = ctypes.py_object * (self.capacity*2)
            Arr1 = self.ArrayType()
            for i in range(position):
                Arr1[i] = self.Arr[i] 
            Arr1[position]  = value
            for i in range(position, self.Size):
                Arr1[i+1] = self.Arr[i]
            self.Arr = Arr1
            self.capacity *= 2
        else:
            for i in range(self.Size, position, -1):
                self.Arr[i] = self.Arr[i-1]
            self.Arr[position] = value
        self.Size += 1   

    def pushFront(self, value):
        self.insertInPosition(0,value)

    def pushBack(self,value):
        self.insertInPosition(self.Size,value)

    def Append(self, Value):
        if self.capacity == self.Size:
           self.ArrayType = ctypes.py_object * (self.capacity * 2)
           Arr1 = self.ArrayType()
           for i in range(self.Size):
               Arr1[i] = self.Arr[i]
           self.Arr = Arr1
           self.capacity *= 2
        self.Arr[self.Size] = Value
        self.Size += 1

    def erase(self, Index):
        if Index > self.Size or Index < 0:
            raise IndexError("Indice fuera del rango")
        for i in range(Index , self.Size-2):
            self.Arr[i] = self.Arr[i+1]
        self.Size -= 1

    def emptyList(self):
        while self.size() > 0 :
            self.erase(0)
    
    def IsEmpty(self):
        return self.Size == 0

    def find(self, data):
        for i in range(self.Size):
            if data == self.getElement(i):
                return i
        return -1

    def size(self):
        return self.Size

    def printArray(self):
        for i in range(self.Size):
            print(self.Arr[i], end = " " )
        print()    

    def __iter__(self):
        for i in range(self.Size):
            yield self.getElement(i)            

    def __eq__(self,other):    
        equal = False    
        if isinstance(other,Array_Dinamic):
            if self.Size == other.Size:
                equal = True
                for selfElement, otherElement in zip(self,other):
                    if (selfElement != otherElement):
                        equal = False
                        break
        return equal

    def __lt__(self,other):
        lessThan = False      
        if isinstance(other, Array_Dinamic) and self.size() == other.size() and self.size() > 0:
            if self.getElement(0) < other.getElement(0):
                lessThan = True
        return lessThan
    
    def lessThan(self,other,i):
        lessThan = False
        if self.Size == other.Size and self.Size > 0 and self.getElement(i) < other.getElement(i):
            lessThan = True
        return lessThan     
    
    def sortedInsertion(self, value ,increasing = True):
        self.Size += 1
        index = 0
        if self.Size == 1:
            self.Arr[0] = value
        elif increasing:      
            if self.Size > self.capacity:
                self.capacity *= 2
                self.ArrayType = ctypes.py_object * self.capacity
                arr1 = self.ArrayType()
                while value > self.getElement(index):                   
                    index += 1
                    if(index == self.Size-1):
                        break                                                           
                for i in range(index):
                    arr1[i] = self.getElement(i)
                arr1[index] = value
                for i in range(index, self.size() -1):
                    arr1[i+1] =  self.getElement(i)
                self.Arr = arr1
                
            else:            
                while value > self.getElement(index):
                    index += 1
                    if(index == self.Size-1):
                        break  
                for i in range(self.size()-2, index-1, -1):
                    self.Arr[i+1] = self.Arr[i]
                self.Arr[index] = value                
            
        elif not increasing:            
            if self.Size > self.capacity:   
                self.capacity*=2       
                self.ArrayType = ctypes.py_object * self.capacity
                arr1 = self.ArrayType()                      
                while value < self.getElement(index) :
                    index += 1
                    if(index == self.Size-1):
                        break
                for i in range(index):
                    arr1[i] = self.getElement(i)
                arr1[index] = value
                for i in range(index, self.size() -1):
                    arr1[i+1] =  self.getElement(i)
                self.Arr = arr1
            else:            
                while value < self.getElement(index):
                    index += 1
                    if(index == self.Size-1):
                        break
                for i in range(self.size()-2, index-1, -1):
                    self.Arr[i+1] = self.Arr[i]
                self.Arr[index] = value                     
    


            

#############################################################




class Stack:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, data):
        self.node = Node(data)
        if self.tail == None:
            self.tail = self.node
            self.head = self.tail
        else:
            self.tail.next = self.node
            self.node.prev = self.tail
            self.tail = self.node
        self.count += 1

    def Top(self):
        return self.tail.data

    def Pop(self):
        if self.head == None:
            print("Error: lista vacía.")
        elif self.head == self.tail:
            self.value = self.tail.data
            self.tail = None
            self.head = self.tail
            self.count -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
        return self.value

    def empty(self):
        return self.head == None


#########################
