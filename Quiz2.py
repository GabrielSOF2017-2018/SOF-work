#Import
import random
#Defing functions

"""
This first function was created in order not to have to recreate the below
function more then once or spliting it in two and it is in esence just a repetion
of the same thing for each operation
"""
score1 = [0] #This is to create a second table in order to bring more information out of the function

def anoying(operation, Answer, a, b):
    if operation == "*":
        if Answer == a*b:
            return True
        else:
            return False
    elif operation == "/":
        if Answer == a/b:
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



def proces(times, operation, score):
    times = int(times)
    score = score1
    for i in range (times):
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        print("What is", str(a), operation, str(b))
        Answer = int(input("Answer: "))
        if anoying(operation, Answer, a, b) == True:
            print("Corect")
            score[0] = score[0] + 1
        else:
            print("Incorect")
    return;

#Start of code including defing variables
print("Would you like to do a numbers quiz")
print()
while True:
    operation = input("what kind of quiz would you like * for multiplaction more added later: ")
    times = input("How many questions do you want: ")

    proces(times, operation, score1)
    print()
    print("quiz done")
    print("You got ", str(score1[0]), " out of ", str(times))
    c = input("Would you like to try again Y/N:")
    if c == "n" or c == "N":
        break
    print()
    print(anoying("*", 10, 2, 5))
