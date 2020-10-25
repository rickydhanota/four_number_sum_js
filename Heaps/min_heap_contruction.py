# Min Heap Construction
# Implement a MinHeap class that supports:
    # -Building a Min Heap from an input array of integers
    # -Inserting integers in the heap
    # -Removing the heaps minimum / root value
    # -Peeking at the heaps minimum / root value
    # -Sifting integers up and down the heap, which is to be used when inserting and removing values

# Note that the heap should be represented in the form of an array
# array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

# All operations below are performed sequentially

# MinHeap(array): - # instantiate a MinHeap (calls the buildHeap method and populated the heap)
# buildHeap(array): - #[-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
# insert (76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
# peek(): -5
# remove(): -5 # [2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
# peek(): 2
# remove(): 2 # [6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
# peek(): 6
# insert(87): - [6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76, 87]

class MinHeap: # A min heap means in the branch of things the root node is the smaller value in comparison to its children nodes. A heap is not sorted
    def __init__(self, arrar):
        self.heap = self.buildHeap(array)
    
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2 #floor devision, it just rounds down
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

#In order to find the first child of our root node, we do 2i + 1, and to find the second child we do 2i + 2. The root node is i = 0, in other words, it is our initial index position

#To find the parent node of a child, we do ((i-1)//2) to find the "floor" of the parent node. 