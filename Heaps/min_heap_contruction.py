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