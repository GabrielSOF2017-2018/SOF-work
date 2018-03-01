import random
print("numbers quiz")
print()
print("Its going to be your times table")
score = 0

while True:
    t = input("How many times do you want to multiply: ")
    t = int(t)
    for i in range (t):
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        print("What is", str(a), "times", str(b))
        Answer = int(input("Answer: "))
        if Answer == a*b:
            print("Correct")
            score = score + 1
        else:
            print("Incorect")

    print()
    print("quiz done")
    print("You got ", str(score), " out of ", str(t))
    c = input("Would you like to try again Y/N:")
    if c == "n" or c == "N":
        break
    score = 0
