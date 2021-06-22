"""Print first 100 odd numbers in Python"""

#using counter to compare to said value. The counter counts how many times the while loop is performed. 
#using while

n = 1
counter = 0 
while counter < 100:
    n += 2
    print(n)
    counter += 1


#using for loop 
#y is acting as the counter in this case
n = 1
for y in range(1, 101):
    n += 2 
    print(n)