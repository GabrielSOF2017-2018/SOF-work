print("This program finds the area of a rectangle")
print()

while True:
        L = float(input("What is the length: "))
        H = float(input("What is the height: "))
        print("Your area is " + str(L*H))
        yn = input("Would you like to calculate another rectangle Y/N: ")
        if yn == "n" or yn == "N":
            break
