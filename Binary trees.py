__author__ = 'barberj'
values = [90, 6, 70, 23, 1, 11, 420]

array = []

for i in range(0, len(values)):
    array.append([values[i], "", ""])

for i in range(1, len(values)):

    pointer = 0
    #location = 0

    ##while loop
    while pointer != "":
    #while array[i-1][1] == "" and array[i-1][2] == "":

        #if the previous node value is bigger than current val, go left
        if array[pointer][0] > array[i][0]:

            #if the pointer is blank, then we can set it, otherwise follow it
            if array[pointer][1] == "":
                array[pointer][1] = i
                break
            else:
                pointer = array[pointer][1]

        #if the previous value is less than current value go right
        elif array[pointer][0] < array[i][0]:

            if array[pointer][2] == "":
                array[pointer][2] = i
                break
            else:
                pointer = array[pointer][2]
    ##make sure you are starting at first node and comparing the values and continuing to follow the left/right pointers
    #until you hit ""

print(array)

def inOrder():
#inorder traversal

    global array
    inOrderArray = []
    backPointer = -1
    pointer = 0

    #left side
    while pointer != "":
        #if left pointer not blank, go to left pointer
        if array[pointer][1] != "":
            backPointer = pointer
            pointer = array[pointer][1]
        #if left pointer is blank we are at the furthest left
        #so we append it and the value behind it
        else:
            inOrderArray.append(array[pointer][0])
            pointer = array[pointer][1]
            inOrderArray.append((array[backPointer][0]))

    #reset the pointer to the value above the furthest left value
    pointer = backPointer
    #start of the right root
    rightRoot = 2
    left = None

    #first right
    while left == None:
        #if right pointer not blank, follow that link
        if array[pointer][2] != "":
            backPointer = pointer
            pointer = array[pointer][2]
        #if there is no right pointer, follow the left link
        elif array[pointer][2] == "" and array[pointer][1] != "":
            backPointer = pointer
            pointer = array[pointer][1]
        #if both pointers are blank you are at the bottom
        elif array[pointer][2] == "" and array[pointer][1] == "":
            inOrderArray.append(array[pointer][0])
            inOrderArray.append(array[backPointer][0])
            inOrderArray.append(array[rightRoot][0])
            pointer = 0
            left = "done"

    #now we only need to concentrate on the right side
    right = None

    while right == None:
        #append the top root
        if pointer == 0:
            inOrderArray.append(array[pointer][0])
        #check if there is a right root to follow
        #if there is, follow the right link
        if array[pointer][2] != "":
            backPointer = pointer
            pointer = array[pointer][2]
        #check if there is a left link
        elif array[pointer][1] != "" and array[pointer][2] == "":
            backPointer = pointer
            pointer = array[pointer][1]
        #check if you are at the bottom
        elif array[pointer][1] == "" and array[pointer][2] == "":
            inOrderArray.append(array[pointer][0])
            inOrderArray.append(array[backPointer][0])
            right = "done"


    print(inOrderArray)

inOrder()