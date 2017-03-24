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
    return x + y

def subtract_two_numbers(x,y):
    """ subtract two numbers """
    return x - y
	
def multiply_two_numbers(x,y):
	return x * y	

def divide_two_numbers(x,y):
	if y == 0:
		return "error"
	else:
		return x / y;

#Greeting
print("Hello! This is a simple program for simple calculations")

#Specify operation
print('\x1b[1;31m'+"What would you like to do today?"+'\x1b[0m')
#doToday = "add" #HACK
doToday = input("add for addition \nsubs for substraction\nmult for multiplication\ndivide for division\noperation:")
print("We will " + doToday + " two numbers now.")

var01 = input("First number: ")
var02 = input("Second number: ")
var1=float(var01)
var2=float(var02)

if doToday=="add":
    result = add_two_numbers(var1, var2)
elif doToday == "subs":
	result = subtract_two_numbers(var1 , var2)
elif doToday == "mult":
	result = multiply_two_numbers(var1 , var2)
else:
	result = divide_two_numbers(var1 , var2)	
	
print("This is the result:", result)
print("I hope it is correct...")
print("Bye, now!")
