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
            self.index += 1
            if self.copy.data == data:
                return self.index
            self.copy = self.copy.next
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

    def orderedInsertion(self, data):
        newNode = Node(data)
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
            

    def impr(self):
        if self.head != None:
            self.copy = self.head
            while self.copy != None:
                if type(self.copy.data) == LinkedList:
                    self.copy.data.impr()
                else:
                    print(self.copy.data)
                self.copy = self.copy.next
        else:
            print("Lista vacía.")

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


