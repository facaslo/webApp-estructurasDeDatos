from SequentialStructures import Array_Dinamic

class BinaryHeap:
    def __init__(self,size):        
        self.size = -1
        self.h = Array_Dinamic(size)       

    def IsEmpty(self):
        return self.h.IsEmpty()

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*i+1

    def rightChild(self, i):
        return 2*i+2

    def siftUp(self, i):
        while i>0 and self.h.getElement(self.parent(i)).getElement(0).lower() > self.h.getElement(i).getElement(0).lower():
            temp = self.h.getElement(self.parent(i))
            self.h.Set(self.parent(i),self.h.getElement(i))
            self.h.Set(i,temp)
            i = self.parent(i)

    def siftDown(self, i):
        maxindex = i
        l = self.leftChild(i)
        if l <= self.size and self.h.getElement(l).getElement(0).lower() < self.h.getElement(maxindex).getElement(0).lower():
            maxindex = l
        r = self.rightChild(i)
        if r <= self.size and self.h.getElement(r).getElement(0).lower() < self.h.getElement(maxindex).getElement(0).lower():
            maxindex = r
        if i != maxindex:
            temp = self.h.getElement(i)
            self.h.Set(i,self.h.getElement(maxindex))
            self.h.Set(maxindex,temp)
            self.siftDown(maxindex)

    def insert(self, p):        
        self.size += 1
        self.h.Append(p) 
        self.siftUp(self.size)

    def extractMin(self):
        result = self.h.getElement(0) 
        self.h.Set(0,self.h.getElement(self.size))          
        self.size -= 1
        self.siftDown(0)
        return result

    # def remove(self, i):
    #     self.h[i] = [None for i in range(28)]
    #     self.h[i][0] = "􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿"     #infinito para strings
    #     self.siftUp(i)
    #     self.extractMax

    def changePriority(self, i, p):
        oldp = self.h.getElement(i)
        self.h.Set(i,p)        
        if p > oldp:
            self.siftUp(i)
        else:
            self.siftDown(i)

#######################################################################

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key.getElement(0).lower() < root.key.getElement(0).lower():
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key.getElement(0).lower() < root.left.key.getElement(0).lower():     #left left
            return self.rightRotate(root)

        if balance < -1 and key.getElement(0).lower() > root.right.key.getElement(0).lower():   #right right
            return self.leftRotate(root)

        if balance > 1 and key.getElement(0).lower() > root.left.key.getElement(0).lower():     #left right
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key.getElement(0).lower() < root.right.key.getElement(0).lower():   #right left
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def delete(self, root, key):
        if not root:
            return root

        elif key.getElement(0).lower() < root.key.getElement(0).lower():
            root.left = self.delete(root.left, key)

        elif key.getElement(0).lower() > root.key.getElement(0).lower():
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:     #left left
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:   #right right
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:      #left right
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:    #right left
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def inOrderReturn(self, datastructure, root): #agrega los elementos a la estructura en orden inOrden (no los imprime)
        if not root:
            return
        self.inOrderReturn(datastructure, root.left)
        datastructure.pushBack(root.key)
        self.inOrderReturn(datastructure, root.right)

# Elementos heap:
# a = Array_Dinamic()
# b = Array_Dinamic()
# c = Array_Dinamic()
# a.Append("A")
# b.Append("C")
# c.Append("B")

# heap = BinaryHeap()
# heap.insert(a)
# heap.insert(b)
# heap.insert(c)

# for elemento in heap.h:
#     print(elemento.getElement(0), end="")

# print()

# while heap.size > 0 :
#     print(heap.extractMax().printArray())

