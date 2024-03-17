prompt = """Given a sorted array of integers, nums, and a target, return the index of the target within nums. If it does not exist, return the index of where target should be inserted"""

"""example 1""" 
example_1_nums = [1, 5, 8, 12]
example_1_target = 12
#return_valuwe =3


def return_index_target(array, target):
    #idx = 0
    for num in range(len(array)):
        if array[num]==target:
            return num
        #idx +=1
    return -1

example_1_solution = return_index_target(example_1_nums, example_1_target)
print(f"Answer to example 1 is: {example_1_solution}")


"""example 2"""
example_2_nums = [1,5,8,12]
example_2_target = 3
# return 2

def return_target_insert_index(array, target):
    for num in range(len(array)):
        if array[num]==target:
            return num
        elif array[num] <= target and array[num+1] >= target:
            return num +1
    
example_2_solution = return_target_insert_index(example_2_nums, example_2_target)
print(f"Answer to example 2 is: {example_2_solution}")

"""example 3"""
example_3_nums = [1,5,8,12]
example_3_target = 100
# return 3

def return_target_insert_index(array, target):
    for num in range(len(array)):
        if array[num]==target:
            return num
        elif array[num] >= target:
            return 0
        elif array[len(array)-1] <= target:
            return len(array)
        elif array[num] <= target and array[num+1] >= target:
            return num +1
    return -1
    
example_3_solution = return_target_insert_index(example_3_nums, example_3_target)
print(f"Answer to example 4 is: {example_3_solution}")