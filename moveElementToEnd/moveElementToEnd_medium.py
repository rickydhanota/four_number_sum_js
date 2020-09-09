# you're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the aray and returns the array

#the Function should perform this in place (i.e., it should mutate the input array) and doesnt need to maintain the order of the other integers

# example - array = [2 , 1, 2, 2, 2, 3, 4, 2], toMove = 2
#output: [1, 3, 4, 2, 2, 2, 2, 2]

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i< j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array


print(moveElementToEnd([2 , 1, 2, 2, 2, 3, 4, 2], 2))