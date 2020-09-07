# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one
# a subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1,3,4] for a subsequence of the array [1,2,3,4], and so do the numbers [2,4]. Note that a single number in an array and the array itself are both valid sequences of the array.

#example input: array = [5,1,22,25,6,-1,8,10]
#sequence = [1,6,-1,10]

#Sample output is true

# def isValidSubsequence(array, sequence):
#     seqIDX = 0
#     for i in range(len(array)-1):
#         if array[i] != sequence[seqIDX]:
#             continue
#         if array[i] == sequence[seqIDX]:
#             seqIDX += 1
#             if seqIDX == len(sequence)-1:
#                 return True    

def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence) #output is True if they equal one another

print(isValidSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,10]))