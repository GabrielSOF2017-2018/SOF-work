import random

def maxToMin(table):
    for i in range(len(table)+1):
        testingNumber = i-1
        for i in range(len(table)):
            if table[testingNumber] >= table[i]:
                tempA = table[testingNumber] 
                tempB = table[i]
                table[testingNumber] = tempB
                table[i] = tempA


theList = []

for i in range(100):
    theList = theList + [random.randint(1, 1000)]

maxToMin(theList)

print(theList)
