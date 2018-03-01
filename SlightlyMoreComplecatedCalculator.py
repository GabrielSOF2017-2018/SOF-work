import math


def simpMath(a, b, operation): #A and B are the values given and operation is the operation the user wants to do
# The operation is givin as an input so therfor must be tested for being the right string
    if operation == "*": # Multiplication
        return a*b # The actual operation is done based on what string was given
        # Everything else in this function is the same so no need to realy coment
    elif operation == "/": # divison
        return a/b
    elif operation == "+": # addition
        return a+b
    elif operation == "-": # Subtraction
        return a-b
    elif operation == "**": #Exponetial
        return a**b
    else:
        print("no input entered")

def trig(a, operation):
# The notes are the same as above for the actual work
# I picked most of the basic trig functions learnt in highschool math for the function trig
    if operation == "sin": # sine
        return math.sin(a)
    elif operation == "arcSin": # inverse or arc sine
        return math.asin(a)
    elif operation == "cos": # cosine
        return math.cos(a)
    elif operation == "arcCos": # arc cosine
        return math.acos(a)
    elif operation == "tan": # tangent
        return math.tan(a)
    elif operation == "arcTan": # arctangent
        return math.atan(a)
    else:
        print("no input entered")

def calculator():
    print("Would you like to do a basic(B) operation or a trig(T) operation") # These are the two operations I have now
    operationType = input("Operation Type: ")# I keep the prompt sepreat as to not run into errors in the future becuase of bad habbits
    if operationType == "b" or operationType == "B": # I don't know if the user will use capital or lowercase leters
        print("Would you like to do adition(+), subtraction(-), division(/), multiplication(*), or exponets(**)")#Here I give the user the difrent basic operations
        operation = input("Operation: ")
        print("What are your two values")# I ask the two values and their order is important for / and -
        a = input("Value 1: ")
        b = input("Value 2: ")
        print("Your answer is "+str(simpMath(float(a), float(b), operation)))# I only need the user to know the answer so I don't save it to a varible
        
# Bellow I have the same kind of if statment but becuase of slight difrences it makes no sense to put it in a function though

    if operationType == "T" or operationType == "t": # I don't know if the user will use capital or lowercase leters
        print("Would you like to do sine(sin), cosine(cos), tangent(tan), arcsine(arcSin), arc cosine(arcCos), or arc tangent(arcTan). Please keep your values within the limit of the function you have chosen")#Here I give the user the difrent tangent operations
        operation = input("Operation: ")
        print("What is your value")# I only need one value for the function in this componet
        a = input("Value: ")
        print("Your answer is "+str(trig(float(a), operation)))# I only need the user to know the answer so I don't save it to a varible



print("welcome to your calculator")#The opening
while True: # so the user can keep using the calculator
    calculator()# Here is all the real math
    print("Would you like to calculate again")
    choice = input("Y/N: ")
    if choice == "n" or choice == "N":
        break
    elif choice != "Y" and choice != "y":
        print("that was not one of the choice so I am going to stop the program")
        break
