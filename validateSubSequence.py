# Prompt: Given 2 non-empty arrays of integers,
# write a fucntion that determines whether the 2nd array
# is a subsequence of the 1st array.

array_1 = [1, 2, 3, 4, 5]
array_2 = [2,3]

array_3 = [1,2,3,4]
array_4 = [2,5]

## start with 2 pointers, 1 for each array
# initialize both pointers to 0
# use a loop to go throguh each element in the 1st array
# check if the currnet element in the 1st array is == current element in 2nd array
# if yes, move the pointer 'j' of the 2nd array to the next position in the 1st array
# If j reaches the length of the second array  -all elements found

# WHILE LOOP solution
def isSubsequence(array_1, array_2):
    i = 0
    j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] == array_2[j]:
            i += 1
            j += 1
        else:
            j += 1
    return j == len(array_2)
print(isSubsequence(array_1, array_2))
print(isSubsequence(array_3, array_4))

# FOR LOOP solution
def is_subsequence(array_1, array_2):
    j = 0

    for i in array_1:
        if j == len(array_2):
            break
        if i == array_2[j]:
            j += 1
    return j == len(array_2)

print(is_subsequence(array_1, array_2))
print(is_subsequence(array_3, array_4))