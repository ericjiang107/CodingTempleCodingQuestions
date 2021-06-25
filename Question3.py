"""Write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.""" 


def max_num_in_list(a_list):
    maxNum = 0
    for currNum in a_list:
        if currNum > maxNum:
            maxNum = currNum
    return maxNum


print(max_num_in_list([1, 2, 3, 4, 5, 10, 1, 2, 3, 7]))