"""Write a function to print hello_USERNAME! USERNAME is the input of the function. The first line of the code has been defined as below.""" 
# looking for def function not user input

def hello_name(user_name): 
    print("hello_" + user_name.title() + "!")
hello_name("eric")

# for user input
user_name = input("Enter Username ")
print("hello_" + user_name.title() + "!")