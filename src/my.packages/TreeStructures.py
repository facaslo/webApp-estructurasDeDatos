class BinaryHeap:
    def __init__(self):
        self.maxisize = 5000
        self.size = -1
        self.h = [None for i in range(self.maxisize)]

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*i+1

    def rightChild(self, i):
        return 2*i+2

    def siftUp(self, i):
        while i>0 and self.h[self.parent(i)].getElement(0).lower() < self.h[i].getElement(0).lower():
            self.h[self.parent(i)], self.h[i] = self.h[i], self.h[self.parent(i)]
            i = self.parent(i)

    def siftDown(self, i):
        maxindex = i
        l = self.leftChild(i)
        if l <= self.size and self.h[l].getElement(0).lower() > self.h[maxindex].getElement(0).lower():
            maxindex = l
        r = self.rightChild(i)
        if r <= self.size and self.h[r].getElement(0).lower() > self.h[maxindex].getElement(0).lower():
            maxindex = r
        if i != maxindex:
            self.h[i], self.h[maxindex] = self.h[maxindex], self.h[i]
            self.siftDown(maxindex)

    def insert(self, p):
        if self.size == self.maxisize:
            print("Límite del arreglo alcanzado")
            return
        self.size += 1
        self.h[self.size] = p
        self.siftUp(self.size)

    def extractMax(self):
        result = self.h[0]
        self.h[0] = self.h[self.size]
        self.size -= 1
        self.siftDown(0)
        return result

    def remove(self, i):
        self.h[i] = [None for i in range(28)]
        self.h[i][0] = "􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿"
        self.siftUp(i)
        self.extractMax

    def changePriority(self, i, p):
        oldp = self.h[i]
        self.h[i] = p
        if p > oldp:
            self.siftUp(i)
        else:
            self.siftDown(i)