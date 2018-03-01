#Import
import random
#Defing functions

"""
This first function was created in order not to have to recreate the below
function more then once or spliting it in two and it is in esence just a repetion
of the same thing for each operation
"""
score1 = [0] #This is to create a second table in order to bring more information out of the function

"""
This bellow allows me to add subtract multiply and devide values for the function
Proces in order to make the Proces function be able to work with more then just
multiplication
"""
def anoying(operation, Answer, a, b):
    if operation == "*":
        if Answer == a*b:
            return True
        else:
            return False
    elif operation == "/":
        if Answer == a:
            return True
        else:
            return False
    elif operation == "+":
        if Answer == a+b:
            return True
        else:
            return False
    elif operation == "-":
        if Answer == a-b:
            return True
        else:
            return False
    else:
        print("no input entered")
    return;


"""
This is the real meat of the funtion
This is where the random integers are retreived
andd it is also where the testing occurs
but the true and false answers are determend with the above
function
"""
def proces(times, operation, score):
    times = int(times)
    score = score1
    for i in range (times):
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        if operation != "/":
            print("What is", str(a), operation, str(b))
        else:
            print("What is", str(a*b), operation, str(b))
        Answer = int(input("Answer: "))
        if anoying(operation, Answer, a, b) == True:
            print("Corect")
            score[0] = score[0] + 1
        else:
            print("Incorect")
    return;

"""
Below we have the function that is not stored in any
function it is basicly the interface
"""
#Start of code including defing variables
print("Would you like to do a numbers quiz")
print()
while True:
    operation = input("what kind of quiz would you like * for multiplaction, / for division, + for addition, and - for subtraction: ")
    times = input("How many questions do you want: ")

    proces(times, operation, score1)
    print()
    print("quiz done")
    print("You got ", str(score1[0]), " out of ", str(times))
    c = input("Would you like to try again Y/N:")
    if c == "n" or c == "N":
        break
    print()
