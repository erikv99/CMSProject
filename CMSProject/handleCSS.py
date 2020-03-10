# Name = Erik V.
# Student Number = 221122

class handleCSS:
    """This class wil place the desired lines in to the css file"""
    
    def addLinesCSS(self, linesToAdd):
        """Will save the list of css lines to the css file""" 

        # Using a context manager for the file so we are sure it will close and we wont have any "leaks"
        # Opening the file in append mode and adding all the lines to the end of the current file
        with open("//ERIK-VIRTUALBOX/Web/cmsstylesheet.css", "a+") as file:

            # Writing line by line to the file
            for i in range(len(linesToAdd)):
                file.write(linesToAdd[i] + "\n")