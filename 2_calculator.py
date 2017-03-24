"""
This is a simple calculator program.
Exercise:
1. Make sure it works correctly.
2. Fix any problems with this program
3. Commit the fix to your repository
3. Add feature to use existing subtraction function
4. Commit
5. Add multiplication and division (requires writing new function)

"""


def add_two_numbers(x,y):
    """ Adds two numbers """
    return float(x) + float(y)

def subtract_two_numbers(x,y):
    """ subtract two numbers """
    return float(x) - float(y)

#Greeting
print("Hello! This is a simple program for simple calculations")

#Specify operation
print('\x1b[1;31m'+"What would you like to do today?"+'\x1b[0m')
#doToday = "add" #HACK
doToday = input("add for addition \nsubs for substraction\noperation:")
print("We will " + doToday + " two numbers now.")

var1 = input("First number: ")
var2 = input("Second number: ")

if doToday=="add":
    result = add_two_numbers(var1, var2)
else:
	result = subtract_two_numbers(var1 , var2)

print("This is the result:", result)
print("I hope it is correct...")
print("Bye, now!")
