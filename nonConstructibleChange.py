# input
# an array of positive integers representing the values of coins
# coins can have any positive integer value
# they can repeat

# output
# fucntion that returns the minimum amount of change
# the minimum sum of $$ - that you CANNOT create

coins = [5, 7, 1, 1, 2, 3, 22]

def nonConstructibleChange(coins):
    coins.sort()
    change_combos = []
    min_change = 0
    for i in range(len(coins)):
        pass