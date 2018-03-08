import random

Big = random.randint(0,10)
Med = Big
while Med == Big:
    Med = random.randint(0,10)
Sma = Med
while Sma == Med or Sma == Big:
    Sma = random.randint(0,10)
secretNumber = [Big, Med, Sma]

print("This is the number gesser. I have a 3 digit number. try to guess in ten tries")

rightPlace = 0
rightDigit = 0
for i in range(11):
    Guess = input("What's your guess: ")
    if str(Big) in Guess:
        rightDigit = rightDigit + 1
    if str(Med) in Guess:
        rightDigit = rightDigit + 1
    if str(Sma) in Guess:
        rightDigit = rightDigit + 1
    
    if Big == int(Guess[0]):
        rightDigit = rightDigit - 1
        rightPlace = rightPlace + 1
    if Med == int(Guess[1]):
        rightDigit = rightDigit - 1
        rightPlace = rightPlace + 1
    if Sma == int(Guess[2]):
        rightDigit = rightDigit - 1
        rightPlace = rightPlace + 1

    print("you have "+str(rightPlace)+" in the right place and "+str(rightDigit)+" left in the right digit. You have used " +(str(i+1))+ " Guesses")
    if rightPlace == 3:
        print("You WIN!!!")
        win = True
        break
    rightDigit = 0
    rightPlace = 0
    win = False

if win != 1:
    print("Im sorry you have lost the number was "+str(secretNumber[0])+str(secretNumber[1])+str(secretNumber[2]))


    

    
