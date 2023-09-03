array = [1, 2, 3, 5, 6, 8, 9]
array_2 = [-3, 1, 5, 6]

def sortedSquaredArray(array):
    new_array = [abs(i)**2 for i in array]
    return sorted(new_array)

print(sortedSquaredArray(array))
print(sortedSquaredArray(array_2))

def sortedSquaredArray_while(array):
    for i in array:
        if i == 0:
            pass
        elif i >0:
            pos_array = [i**2]
        else:
            neg_array = [i**2]
    return sorted(pos_array+neg_array)

#print(sortedSquaredArray_while(array))
#print(sortedSquaredArray_while(array_2))

def sortedSquaredArray_for(array):
    pos_array = []
    neg_array = []
    ## need to instantiate these values in case conditionals not met
    
    for i in array:
        if i == 0:
            pos_array.append(0)
        elif i >0:
            pos_array.append(i**2)
        else:
            neg_array.append(i**2)
    
    return sorted(pos_array+neg_array)

print(sortedSquaredArray_for(array))
print(sortedSquaredArray_for(array_2))