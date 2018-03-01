import random

def choices():
    choices = []
    while True:
        choice = input("What value do you want to add to your random string picker or N to start making your choices: ")
        if choice == "N" or choice =="n":
            if choices == []:
                return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            return choices
        else:
            choices = choices + [choice]

def pick(items):
    
    itemLength = len(items)
    
    choice = random.randint(0, itemLength-1)

    print(items[choice])


while True:
    print("This is your random string picker")
    items = choices()
    while True:
        pick(items)
        again = input("Would you like to try again N or Enter: ")
        if again == "N" or again == "n":
            break
