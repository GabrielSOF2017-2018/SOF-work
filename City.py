import textAlt

def hotelCost(days):
    #userInput = int(input("How many days do you plan to stay"))
    return (90*days)
def planeRideCost(destination):
    #userInput = input("Enter which city you want to travel to: ")
    if city == "Charlotte":
        return(185)
    elif city == "Tampa":
        return(22)
    elif city == "Pittsburgh":
        return(175)

def rentalCarCost(days):
    cost=40*days
    if days>7:
        cost=cost-40
    elif days >= 3 and days <5:
        cost=cost-20
    return cost
    
def tripCost(days, city, spendingMonney):
    return hotelCost(days)+rentalCarCost(days)+planeRideCost(city)+spendingMonney


city = input("what city are you going to: ")
days = int(input("for how long: "))
spendingMonney = int(input("how much spending monney do you have: "))

print("the cost of your trip is"+(tripCost(days, city, spendingMonney)))
