"""
The function callline prints an individual line from any text document based
on the line that the user wants to put.

    If i want to maximize computer memory I could probably do this in interviels
    based on the line asked for
"""
def calLine(path, line, filetype = "utf-8"):
    file = open(path, encoding = filetype)#The file I picked
    for i in range(line): # Going to the line the program asked for
        """
        The file.read() makes the program go one line further just by reading it
        and the if statment test my end of a text doc in order to not make it
        go into an infinet loop.
        """
        if file.readline() == ";;;":
            print("This line is to far in the document")
            return


        """
        The code below creats the string that is being outputed
        """
    string = "" #defing the varible with nothing becuase the first use refrences itself
    while True:
        charcter = file.read(1) #puling a charcter from the document
        if charcter == "\n": # this is the new line sequence AKA the end of the called line
            file.close()
            return string
        
        string = string+charcter #this creats the string outputed
        
        if string == ";;;": # At this point the document is over so nothing is returned
            return






        
"""
This function does the complete opiste of the above function as it takes
a qoute and see's if it is in a file while checking which line
"""
def checkLine(path, string, filetype = "utf-8"):
    file = open(path, encoding = filetype)
    testString = "" #this is the varible that holds each string being tested
    counter = 0 #writes what line your string is on
    charcter = "" # same as test string defing before using
    while testString != ";;;":
 #       testString = testString + charcter # this line adds the new charcter to the string being tested
        
        charcter = file.read(1) #It brings out a new charcter from the text
        if charcter == "\n":
            charcter = ""
            if testString == string: #Tests if this is the string being looked for
                file.close()
                return counter # This returns what line the string is on
            
            elif testString == ";;;": #This is the end of the doc and stops the checkline as the string does not exsist
                return
                print("test")
#Below is the code designed to reset the proces for a new line
#I cant put a multiine coment here for somereason this is a coment to remind myself to ask why

            else:
                testString = "" # this resets the test string to nothing for a new line
                counter = counter+1 #Adds to the counter
        testString = testString + charcter


