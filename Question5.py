"""Write a function to check to see if all numbers in list are consecutive numbers. For example, [2, 3, 4, 5, 6, 7] are consecutive are consecutive numbers, but [1, 2, 4, 5] are not consecutive numbers. The return should be boolean Type."""

"consecutive lists" 
"check through list"
"print true or false"

#range(len(a_list)-1) reads the position of the list, not the value itself
#a_list[i+1] means the position adds 1 to the next position, not the value itself
#return function only looks at the first 2 values and stops once the condition is met (it doesn't look at the other values in the index)
#pass skips through the function. Skips something, keeps on going
def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        if a_list[i] + 1 == a_list[i + 1]:
            pass
        else:
            return False
    return True
    

print(is_consecutive([1,2,3,4,5]))


#Other way
#Continue means it meets the condition and continues onto the for loop in this case
def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        if a_list[i] + 1 == a_list[i + 1]:
            continue
        else:
            return False
    return True
    

print(is_consecutive([1,2,6,4,5]))


#easier way of doing this
def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        if a_list[i] + 1 != a_list[i + 1]:
            return False
    return True
    

print(is_consecutive([1,2,3,4,5]))