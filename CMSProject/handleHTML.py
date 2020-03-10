# Name = Erik V.
# Student Number = 221122

class handleHTML:
    """This class will place the desired lines in the html file"""

    def __init__(self):

        self.__htmlLines = []

    def __getIndex(self, tag):
        """Will return the index at which the given tag is located in our list of html lines. Note: only works if there is only one occurance (ex. </head>)"""
        
        for i in range(len(self.__htmlLines)):

            # If tag is found in the string on the current list index we return the index
            if tag in self.__htmlLines[i]:

                return i

        # If there is nothing in the file yet we want to start at index 0
        else:

            return 0

    def __getAllLines(self):
        """Will get all the lines from our html file and save them in a list which it will return"""
        htmlFileLines = []

        # Using a context manager for the file so we are sure it will close and we wont have any "leaks"
        # Opening the file in read mode
        with open("//ERIK-VIRTUALBOX/Web/index.html", "r") as file:

            # Removing the newline char and adding the line to our list. we do this for every line in the file
            for line in file:
                
                lineToAdd = line.replace("\n", "")
                htmlFileLines.append(lineToAdd)

        return htmlFileLines
    
    def __saveLinesToFile(self):
        """Will save the list of html lines to the html file""" 

        # Using a context manager for the file so we are sure it will close and we wont have any "leaks"
        # Opening the file in write mode and adding all our lines from our list to our html file
        with open("//ERIK-VIRTUALBOX/Web/index.html", "w") as file:

            # Writing line by line to the file
            for i in range(len(self.__htmlLines)):
                file.write(self.__htmlLines[i] + "\n")


    def addLinesHTML(self, listOfLines, addBeforeThisTag):
        """Will add the given list of strings before the given tag in our file. (tag must be only occure once)"""

        # Clearing the html lines list in case it wasn't empty
        self.__htmlLines.clear()
        
        # Adding all the lines from the html file to the list
        self.__htmlLines = self.__getAllLines()

        # Getting the index of the tag given and removing one so we have the index before the tag.
        addToIndex = self.__getIndex(addBeforeThisTag)

        for i in range(len(listOfLines)):

            # Adding line number i to the list at index before the given tag.
            self.__htmlLines.insert(addToIndex, listOfLines[i])

            # Increasing the index since we just added something
            addToIndex += 1

        # Actually adding the list to the file
        self.__saveLinesToFile()