import random



def play():
    print("I am thinking of a number between 1-500")
    computerCount = random.randint(1, 501)
    tries = 0
    guess = 0
    win = False
    while win == False:
        guess = int(input("What's your guess: "))
        if guess < computerCount:
            print("Your guess was to small")
            tries = tries+1
        elif guess > computerCount:
            print("Your guess was to big")
            tries = tries + 1
        elif guess == computerCount:
           print("You win in "+str(tries)+" tries")
           win = True
        else:
            print("That's not a number")

def playTimes(times):
    print("I am thinking of a number between 1-500")
    computerCount = random.randint(1, 501)
    tries = 0
    guess = 0
    play = True
    while play == True and tries <= (times-1):
        guess = int(input("What's your guess: "))
        if guess < computerCount:
            print("Your guess was to small")
            tries = tries+1
        elif guess > computerCount:
            print("Your guess was to big")
            tries = tries + 1
        elif guess == computerCount:
           print("You win in "+str(tries)+" tries")
           play = False
        elif tries == times:
            print("You ran out of tries")
        else:
            print("That's not a number")

def playAgain():
    playAgain = input("do you want to play again Y/N: ")
    if playAgain == "Y" or playAgain == "y":
        print("Okay")
        run = 1
    elif playAgain == "N" or playAgain == "n":
        print("Okay")
        run = 0
    else:
        print("You did not put a valid answer so I am going to stop the program")
        run = 0
    return run

def numberGuess():
    print("welcom to find the number")
    choice = input("would you like to play with a max amount of tries Y/N: ")
    if choice == "y" or choice == "Y":
        times = int(input("How many tries: "))
    run = 1
    while run == 1:
        if choice == "y" or choice == "Y":
            playTimes(times)
        else:
            play()
        run = playAgain()


numberGuess()
