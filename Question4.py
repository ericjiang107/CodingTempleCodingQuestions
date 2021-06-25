"""Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false)"""

"Must be divisible by 4"
"Not divisible by 100 unless divisible by 400"
"Return True or False"

#for divisible, use modulo (no remainder)
#for not divisible, use modulo (a remainder)
#unless means another condition
#0 always read False, any other number reads True
#Whenever you use a condition, use if
#Can use if statement within if statement because first if reads true, continue to next if or else go to else statement

def is_leap_year(a_year):
    if (a_year) % 4 == 0:
        if (a_year) % 100 != 0:
            return True
        elif (a_year) % 400 == 0:
            return True
    return False

print(is_leap_year(1700))

