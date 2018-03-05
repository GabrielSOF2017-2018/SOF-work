"""
This is alot of functions ment for univeral use for my D&D app
"""
import random
#this is rolling the dice
def d(number, times=1, modifier=0):
    role = 0 # This is the number rolled
    final = 0 # This is the sum
 #   individual = [] #This is the individual numbers
    for i in range(times):
        role = random.randint(1, (number+1))
        role = role + modifier
        final = role + final
 #       individual = individual+[role]
    return final

#this is the creation of the document

