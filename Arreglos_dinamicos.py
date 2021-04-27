class Array_Dinamic():

    def __init__(self, Cap = 0):
        if type(Cap) != int:
            raise ValueError("El tamaño y la capacidad debe ser un número")
        self.Size = 0
        self.Cap = Cap
        self.Arr = [None for i in range(Cap)]

    def Get(self, Index):
        if Index > self.Size or Index < 0:
            raise IndexError("Indice fuera del rango")
        return self.Arr[Index]

    def Set(self, Index, Value):
        if Index > self.Size or Index < 0:
            raise IndexError("Indice fuera del rango")
        if Arr[index] == None:
            self.Size += 1
        self.Arr[Index] = Value

    def Append(self, Value):
        if self.Cap == self.Size:
           Arr1 = [None for i in range(self.Cap*2)]
           for i in range(self.Size):
               Arr1[i] = self.Arr[i]
           self.Arr = Arr1
           self.Cap *= 2
        self.Arr[self.Size] = Value
        self.Size += 1

    def Remove(self, Index):
        if Index > self.Size or Index < 0:
            raise IndexError("Indice fuera del rango")
        for i in range(Index , self.Size-2):
            self.Arr[i] = self.Arr[i+1]
        self.Size -= 1

    def size(self):
        return self.Size

    def printArray(self):
        for i in range(self.Size):
            print(self.Arr[i], end = " " )
        print()
        


Arr = Array_Dinamic(1)
for i in range(1,33):
    Arr.Append(-i)
    Arr.printArray()