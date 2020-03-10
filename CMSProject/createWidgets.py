# Name = Erik V.
# Student Number = 221122
import handleCSS
import handleHTML
import GUIClass
import shutil
import os

class createWidgetsClass(): 

    def __init__(self):

        self.__mainTitle = None
        self.__font = None # Times New Roman, Roboto, Courier New
        self.__txtColor = None # Text hex code
        self.__otherTitleColor = None # Color hex code
        self.__otherTitleUnderline = None # Underline yes or no
        self.__otherTitleMargin = None # Room between title and other widgets
        self.__imageMargin = None # Room between this image widgets and other widgets (like text)
        self.__imagePadding = None # Room between image border (outlining) and the image itself
        self.__imageBorderType = None # None, Solid, Groove, Double
        self.__imageRoundedCorners = None # Rounded corners yes or no
        self.__imageBorderWidth = None # Border width (max 5 pix)
        self.__html = handleHTML.handleHTML() # Instance of the handleHTML class
        self.__css = handleCSS.handleCSS() # Instance of the handleCSS class

        assign = False
        # Trying to read the list identifiers from the file. If we cant we set the assign variable to False so it will assign 0 to both the variables
        if (os.path.isfile("//ERIK-VIRTUALBOX/Web/listIDCount.txt")):
            with open("//ERIK-VIRTUALBOX/Web/listIDCount.txt", "r") as file:

                # Reading the line(s) of the file
                lines = file.readlines()

                # Checking if lines isn't empty
                if (len(lines) != 0):
                    # Checking if the first line isn't empty. if it is. the second line is as well.
                    if (len(lines[0]) > 1):
                    
                        # Splitting at the : to get the id value for the lists
                        temp, idValueUL = lines[0].split(":")
                        temp, idValueOL = lines[1].split(":")
                        self.__ulListIdentifier, self.__olListIdentifier = int(idValueUL), int(idValueOL)
                    else:
                        assign = True
                else:
                    assign = True
        else:
            assign = True

        if (assign == True):
            self.__ulListIdentifier = 0 # Used for unique id's for unordered list
            self.__olListIdentifier = 0 # Used for unique id's for ordered list

    def generate(self, name, settingsDic):
        """Will call the right private function to create the needed widgets / page"""

        if (name == "CP"):
            self.__generatePage(settingsDic)
        elif (name == "HT"):
            self.__generateHeaderText(settingsDic)
        elif (name == "HTI"):
            self.__generateHeaderTextImage(settingsDic)
        elif (name == "ADD"):
            self.__generateSummary(settingsDic)

    def __generateHeaderText(self, settingsDic):
        """Will add a header with text to the html file"""
        # Putting the header and the first <p> tag in the list
        addToHtml = ["<h2>" + settingsDic.get("title") + "</h2>", "<p>" ]

        # Getting the list containing the text to place and looping thru it while adding every line to the addToHtml List
        textList = settingsDic.get("fileContentList")
        for i in range(len(textList)):

            addToHtml.append(textList[i])

        # Adding the closing </p> tag
        addToHtml.append("</p>")

        # Writing the addToHtml to the file
        self.__html.addLinesHTML(addToHtml, "</body>")

    def __generateHeaderTextImage(self, settingsDic):
        """Will add a header with text and a image to the html file"""

        # Getting the file path and splitting it in a tuple, head and tail. then we get the tail only (filename only)
        temp = os.path.split(settingsDic.get("imagePath"))
        imgFileName = temp[1]
        imgFilePath = "Images/" + imgFileName

        # Checking if the img needs a border or not, then checking on which side the image needs to be placed and giving it the right ID.
        if (settingsDic.get("makeBorder") == True):
            if (settingsDic.get("placementSide") == "Left"):
                id = "id=\"byl\""
            elif(settingsDic.get("placementSide") == "Right"):
                id = "id=\"byr\""
        elif(settingsDic.get("makeBorder") == False):
            if (settingsDic.get("placementSide") == "Left"):
                id = "id=\"bnl\""
            elif(settingsDic.get("placementSide") == "Right"):
                id = "id=\"bnr\""

        # Checking on which side the image should be placed and writing the right line to the file
        if (settingsDic.get("placementSide") == "Left"):

            # Making the begin and the end and we will place our other content in between those.
            htiListBegin = ["<table width=\"100%\">", "<tr>", "<td>", "<img src=\"" + imgFilePath + "\" alt=\"" + settingsDic.get("altText") + "\" " + id + ">", "</td>", "<td>"]
            htiListEnd = ["</td>", "</tr>", "</table>"]

        elif (settingsDic.get("placementSide") == "Right"):
            
            htiListBegin = ["<table width=\"100%\">", "<tr>", "<td id=\"textLeft\">"]
            htiListEnd = ["</td>", "<td>", "<img src=\"" + imgFilePath + "\" alt=\"" + settingsDic.get("altText") + "\" " + id + ">" , "</td>", "</tr>", "</table>"]

        # First part of the content 
        contentList = ["<h2>" + settingsDic.get("title") + "</h2>", "<p>" ]
        # Second part of the content (text for in the <p> tags)
        textList = settingsDic.get("fileContentList")
        # Adding the text list to the  end of the contentList
        contentList.extend(textList)
        # Adding the closing </p> tag
        contentList.append("</p>")

        # Making the actual html file.
        addToHtml = htiListBegin
        addToHtml.extend(contentList)
        addToHtml.extend(htiListEnd)
        
        # Writing the addToHtml to the file
        self.__html.addLinesHTML(addToHtml, "</body>")

        # We get the img path, then we move the img inside the file share. then we can use it. (server cant get img from local pc something with security)
        imgPath = settingsDic.get("imagePath")
        destinationPath = "//ERIK-VIRTUALBOX/Web/Images"

        # Copying the img the user selected to the server file share images directory.
        shutil.copy2(imgPath, destinationPath)

    def __generateSummary(self, settingsDic):
        """Will add a summary to the html file"""

        def __saveListIDS():
            """Function to save the value of the (un)ordered list identifier which is used to make UNIQUE ID's for the list / summary's """

            with open("//ERIK-VIRTUALBOX/Web/listIDCount.txt", "w+") as file:
                file.writelines(["UL:" + str(self.__ulListIdentifier) + "\n", "OL:" + str(self.__olListIdentifier) + "\n"])

        listType = settingsDic.get("listType") 
        # Gettings the begin and end lines of the file depending on the type of list chosen
        if (listType == "Ordered List"):

            summaryBegin = "<ol id=\"ol" + str(self.__olListIdentifier) + "\">"
            summaryEnd = "</ol>"
            currentId = "ol" + str(self.__olListIdentifier)
        else:

            summaryBegin = "<ul id=\"ul" + str(self.__ulListIdentifier) + "\">"
            summaryEnd = "</ul>"
            currentId = "ul" + str(self.__ulListIdentifier)

        # Making the list to store the lines in that we want to add
        addToHtml = []
        # Adding the first part of the list
        addToHtml.append(summaryBegin)

        # Looping thru all the list items and placing them within <li> tags in the addToHtml list
        fileContent = settingsDic.get("fileContent")
        for i in range(len(fileContent)):

            addToHtml.append("<li>" + fileContent[i] + "</li>")

        # Adding the last part
        addToHtml.append(summaryEnd)
        self.__html.addLinesHTML(addToHtml, "</body>")
        
        addToCss = ["#" + currentId + " {"]
        
        # NOTE: i use an extra elif instead of else sometimes. i do this for readability.
        # Checking which list type
        if (listType == "Ordered List"):

            # Incrementing Identifier
            self.__olListIdentifier += 1
            # Checking which bullet type
            bulletType = settingsDic.get("orderedBulletType")

            if (bulletType == "Numbers (1, 2, 3)"):
                addToCss.append("list-style-type: decimal;")

            elif (bulletType == "Letters (A, B, C)"):
                addToCss.append("list-style-type: upper-alpha;")

        elif (listType == "Unordered List"):

            # Incrementing Identifier
            self.__ulListIdentifier += 1
            bulletType = settingsDic.get("unorderedBulletType")
            
            if (bulletType == "Disc (●)"):
                addToCss.append("list-style-type: disc;")            
            
            elif (bulletType == "Square (□)"):
                addToCss.append("list-style-type: square;")
            
            elif (bulletType == "Circle (○)"):
                addToCss.append("list-style-type: circle;")

        # Checking where the user wants the bullets (inside or outside)
        if (settingsDic.get("bulletPlacement") == "Inside"):
            addToCss.append("list-style-position: inside;")

        elif (settingsDic.get("bulletPlacement") == "Outside"):
            addToCss.append("list-style-position: outside;")

        # Closing this css entry and writing it to the file
        addToCss.append("}")
        self.__css.addLinesCSS(addToCss)

        # Saving the list identifiers
        __saveListIDS()

    def __generatePage(self, settingsDic):
        """Will create a new page for the html file"""

        ### FIRST ALL CSS ACTIONS
        colorDic = settingsDic.get("colorsDic")

        # In h1 we make margin bottom only, it will be at the top page and have no text above it so it is not needed on the top.
        # We got 4 ID's for img. one is for with a border and img on left(#byl) also for right (#byr) and two are for no border (#bnl / #bnr)
        addToCss = ["body {", "background-color: " + colorDic.get("bgColor") + ";", "font-family: \"" + settingsDic.get("font") + "\";", "color: " + colorDic.get("txtColor") + ";", "}",
                   "h1 {", "text-align: center;", "margin-bottom: " + settingsDic.get("roomTitleText") + "px;", "color: " + colorDic.get("mainTitleColor") + ";", "}",
                   "h2 {", "margin-top: " + settingsDic.get("roomTitleText") + "px;", "margin-bottom: " + settingsDic.get("roomTitleText") + "px;", "color: " + colorDic.get("otherTitleColor") + ";", "text-align: center;", "}",
                   "img {", "max-width: 150px;", "max-height: 150px;", "}" 
                   "#introtext {", "text-align: center;", "}",
                   "#byl {", "margin-right: " + settingsDic.get("roomImageText") + "px;", "padding: " + settingsDic.get("roomImageBorder") + "px;", 
                   "border: " + settingsDic.get("borderWidth") + "px " + settingsDic.get("imageBorder") + " " + colorDic.get("txtColor") + ";", "}",
                   "#byr {", "margin-left: " + settingsDic.get("roomImageText") + "px;", "padding: " + settingsDic.get("roomImageBorder") + "px;",  
                   "border: " + settingsDic.get("borderWidth") + "px " + settingsDic.get("imageBorder") + " " + colorDic.get("txtColor") + ";", "}",
                   "#bnl {", "margin-right: " + settingsDic.get("roomImageText") + "px;", "}",
                   "#bnr {", "margin-left: " + settingsDic.get("roomImageText") + "px;", "}",  
                   "#textLeft { text-align: right;}"
                   ]

        # Finding the index of the header 1 start and adding 1
        placementIndex = addToCss.index("h1 {") + 1
        
        # If main title needs to be italic
        if (settingsDic.get("mainTitleItalic") == "Yes"):
            addToCss.insert(placementIndex, "font-style: italic;")

        # If main title needs to be capitalized
        if (settingsDic.get("mainTitleCapital") == "Yes"):
            addToCss.insert(placementIndex, "text-transform: uppercase;")

        # If other titles need to be underlined
        if (settingsDic.get("otherTitleUnderline") == "Yes"):
            # Finding the index of the header 2 start and adding 1
            placementIndex = addToCss.index("h2 {") + 1
            addToCss.insert(placementIndex, "text-decoration: underline;")

        # If img needs 5px rounded corners
        if (settingsDic.get("roundedImgCorners") == "Yes"):
            placementIndexBy = addToCss.index("img {") + 1
            addToCss.insert(placementIndexBy, "border-radius: 5px;")

        # Adding all the lines to the css file
        self.__css.addLinesCSS(addToCss)

        ### SECOND ALL HTML ACTIONS
        # Adding the basic html page template to the empty file
        pageTemplate = ["<!DOCTYPE html>", "<html>", "<head>", "<link rel=\"stylesheet\" type=\"text/css\" href=\"cmsstylesheet.css\">", "</head>", "<body>", "</body>", "</html>"]
        self.__html.addLinesHTML(pageTemplate, " ")
        
        # Adding the main title to the file
        self.__html.addLinesHTML(["<title>" + settingsDic.get("mainTitle") + "</title>"], "</head>")
        # Adding h1 main title to the file
        self.__html.addLinesHTML(["<h1>" + settingsDic.get("mainTitle") + "</h1>"], "</body>")

        # Getting the introductionary text content list and adding <p> tags to it then placing it in the html file
        introTextList = settingsDic.get("fileContentList")
        introTextList.insert(0, "<p id=\"introtext\">")
        introTextList.append("</p>")
        self.__html.addLinesHTML(introTextList, "</body>")
        
    def startCMS(self):
        """This will ask the user what they would like to add/create and will then start the right function"""

        # Making a new instance of our GUI Class
        GUI = GUIClass.GUIHandlerClass()
        # Starting the GUI
        GUI.startGUI()