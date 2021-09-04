from LikedList import LinkedList

class HashMap():

    def __init__(self, Cap = 4):
        self.CapArray = Cap
        self.hArray = [None]*self.CapArray
    
    def StringHash(self, key):
        if type(key) != type(str):
            key = str(key)
        keyValue = 0
        for i in key:
            keyValue += ord(i)
        return keyValue % self.CapArray

    def SizeHArray(self):
        Size = 0
        for i in range(len(self.hArray)):
            if self.hArray[i] != None:
                Size += 1
        return Size

    def HasKey(self, key):
        if self.SizeHArray == 0 or self.hArray[self.StringHash(key)] == None:
            return False
        L = self.hArray[self.StringHash(key)]
        while(type(L.topBack()) == LinkedList):
            if L.topFront() == key:
                return True
            L = L.topBack()
        return L.topFront() == key


    def Rehash(self):
        Loadfactor = self.SizeHArray()/self.CapArray()
        if Loadfactor > 0.75:
            T = []*(2*self.SizeHArray)
            self.CapArray = 2*self.CapArray
            for O in self.hArray:
                T[self.StringHash(O)] = O
            self.hArray = T

    def Get(self, key):
        L = self.hArray[self.StringHash(key)]
        if L == None:
            return None
        while(type(L.topBack()) == LinkedList):
            if L.topFront() == key:
                k = L.topFront()
                L.popFront()
                v = L.topFront()
                L.pushFront(k)
                return v
            L = L.topBack()
        if L.topFront() == key:
            k = L.topFront()
            L.popFront()
            v = L.topFront()
            L.pushFront(k)
            return v
        return None

    def Set(self, key, value):
        L = self.hArray[self.StringHash(key)]
        if L == None:
            List = LinkedList()
            List.pushFront(key)
            List.pushBack(value)
            self.hArray[self.StringHash(key)] = List
            return
        while(type(L.topBack()) == LinkedList):
            if L.topFront() == key:
                k = L.topFront()
                L.popFront()
                L.popFront()
                L.pushFront(value)
                L.pushFront(k)
                return 
            L = L.topBack()
        if L.topFront() == key:
            k = L.topFront()
            L.popFront()
            L.popFront()
            L.pushFront(value)
            L.pushFront(k)
            return
        List = LinkedList()
        List.pushFront(key)
        List.pushBack(value)
        L.pushBack(List)

