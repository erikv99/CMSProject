# Name = Erik V.
# Student Number = 221122
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter.font import Font
from PIL import ImageTk, Image
import os.path
import webbrowser
import createWidgets

class GUIHandlerClass():
    """Will let the user select the settings using the GUI, then the GUI will send the settings to the right class"""

    def __init__(self):

        self.__CW = createWidgets.createWidgetsClass()
        self.__currentFrame = None
        self.__MCFRame, HTFrame, HTIFrame, AddFrame, CPFrame = None, None, None, None, None
        self.__root = None
        self.__wWidth, __wHeight = None, None
        self.__pageHasBeenCreated = False 
        self.__colors = {}
        self.__padX = 10
        self.__padY = 10
        # For saving the logo img so it doesnt get garbage collected
        self.__img = None
        # For saving the content of the selected file in any of our browse methods, gets cleared after being send to the class that needs it
        self.__fileContent = []
        # For saving the selected image path, gets cleared after being send to the class that needs it
        self.__imagePath = None

    def __quitProgram(self):
        """Will quit the cms program"""
        self.__root.destroy()

    def __showFrame(self, frameName):
        """Will show the frame and make the __currentFrame hidden / removed"""

        def __hideCorrectFrame():
            """Will hide the correct frame"""
            if (self.__currentFrame == "MCFrame"):
                self.__MCFrame.grid_forget()
            elif(self.__currentFrame == "HTFrame"):
                self.__HTFrame.grid_forget()
            elif(self.__currentFrame == "HTIFrame"):
                self.__HTIFrame.grid_forget()
            elif(self.__currentFrame == "AddFrame"):
                self.__AddFrame.grid_forget()
            elif(self.__currentFrame == "CPFrame"):
                self.__CPFrame.grid_forget()

        def __pageCreatedCheck():
            """Will check if a page has been created and send error message if not"""
            if (self.__pageHasBeenCreated == False):
                tk.messagebox.showerror("Error", "A page must first be made in order to add anything to it!")
                return False
            else: 
                return True

        # Checking which frame was entered
        if (frameName == "MCFrame"):
            
            # Hiding the __currentFrame 
            __hideCorrectFrame()
            # Showing the correct frame (frameName)
            self.__MCFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.N+tk.E+tk.W+tk.S)
            # Assigning the current frame name to our global __currentFrame variable
            self.__currentFrame = frameName

        elif (frameName == "HTFrame"):            
            # Checking if a page has already been created and refusing access otherwise
            if (__pageCreatedCheck() == False):
                return
            __hideCorrectFrame()
            self.__HTFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.N+tk.E+tk.W+tk.S)
            self.__currentFrame = frameName

        elif (frameName == "HTIFrame"):           
            if (__pageCreatedCheck() == False):
                return
            __hideCorrectFrame()
            self.__HTIFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.N+tk.E+tk.W+tk.S)
            self.__currentFrame = frameName

        elif (frameName == "AddFrame"):           
            if (__pageCreatedCheck() == False):
                return
            __hideCorrectFrame()
            self.__AddFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.N+tk.E+tk.W+tk.S)
            self.__currentFrame = frameName

        elif (frameName == "CPFrame"):       
            # If a page has already been created we deny making another one
            if (self.__pageHasBeenCreated):
                self.__error("A page has already been created!")
                return
            __hideCorrectFrame()
            self.__CPFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.N+tk.E+tk.W+tk.S)
            self.__currentFrame = frameName

    def __getFileContent(self, textVar):
        """Opens a file browser for the user to select a txt file and will assign the opened file in read mode to our global variable"""

        # Opening the browse file window, only letting the user select txt files.
        file = tkinter.filedialog.askopenfile(mode = "r", filetypes = (("txt files", "*.txt"),))
        # If the file isn't empty 
        if (file != None):
            
            # Removing unessisary \n and saving each line to our __fileContent list.
            for line in file:

                nLine = line.replace("\n", "")
                self.__fileContent.append(nLine)

            textVar.set("Selected: Yes")

    def __error(self, msg):
        """Will display error msg"""
        tk.messagebox.showerror("Error", msg)

    def __createMCFrame(self):
        """Will make the main choice frame and return it"""
        # The first (MC) frame will have the same color as the image so they match seemless
        s = ttk.Style()
        s.configure("new.TFrame", background="#F7F7F7")
        MCFrame = tk.ttk.Frame(self.__root, width=self.__wWidth, height=self.__wHeight, style="new.TFrame", padding=10,)
        MCFrame.columnconfigure(0, weight=1)
        MCFrame.rowconfigure(0, weight=1)
        MCFrame.rowconfigure(1, weight=1)
        MCFrame.rowconfigure(2, weight=1)
        MCFrame.rowconfigure(3, weight=1)
        MCFrame.rowconfigure(4, weight=1)
        MCFrame.rowconfigure(5, weight=1)
        MCFrame.rowconfigure(6, weight=1)
        MCFrame["borderwidth"] = 2
        MCFrame["relief"] = "ridge"
        MCFrame.grid(column=0, row=0,  sticky=tk.W+tk.N+tk.E+tk.S)
        return MCFrame

    def __createHTFrame(self):
        """Will make the header + text frame and return it"""
        HTFrame = tk.ttk.Frame(self.__root, width=self.__wWidth, height=self.__wHeight)
        HTFrame.columnconfigure(0, weight=1)
        HTFrame.columnconfigure(1, weight=1)
        HTFrame.columnconfigure(2, weight=1)
        HTFrame.rowconfigure(0, weight=1)
        HTFrame.rowconfigure(1, weight=1)
        HTFrame.rowconfigure(2, weight=1)
        HTFrame.rowconfigure(3, weight=1)
        HTFrame["borderwidth"] = 2
        HTFrame["relief"] = "ridge"
        HTFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.W+tk.N+tk.E+tk.S)
        return HTFrame

    def __createHTIFrame(self):
        """Will make the header + text + image frame and return it"""
        HTIFrame = tk.ttk.Frame(self.__root, width=self.__wWidth, height=self.__wHeight)
        HTIFrame.columnconfigure(0, weight=6)
        HTIFrame.columnconfigure(1, weight=1)
        HTIFrame.columnconfigure(2, weight=1)
        HTIFrame.rowconfigure(0, weight=1)
        HTIFrame.rowconfigure(1, weight=1)
        HTIFrame.rowconfigure(2, weight=1)
        HTIFrame.rowconfigure(3, weight=1)
        HTIFrame.rowconfigure(4, weight=1)
        HTIFrame.rowconfigure(5, weight=1)
        HTIFrame.rowconfigure(6, weight=1)
        HTIFrame.rowconfigure(7, weight=1)
        HTIFrame["borderwidth"] = 2
        HTIFrame["relief"] = "sunken"
        HTIFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.W+tk.N+tk.E+tk.S)
        return HTIFrame

    def __createAddFrame(self):
        """Will make the addition frame and return it"""
        AddFrame = tk.ttk.Frame(self.__root, width=self.__wWidth, height=self.__wHeight)
        AddFrame.columnconfigure(0, weight=6)
        AddFrame.columnconfigure(1, weight=1)
        AddFrame.columnconfigure(2, weight=1)
        AddFrame.rowconfigure(0, weight=1)
        AddFrame.rowconfigure(1, weight=1)
        AddFrame.rowconfigure(2, weight=1)
        AddFrame.rowconfigure(3, weight=1)
        AddFrame.rowconfigure(4, weight=1)
        AddFrame.rowconfigure(5, weight=1)
        AddFrame.rowconfigure(6, weight=1)
        AddFrame["borderwidth"] = 2
        AddFrame["relief"] = "sunken"
        AddFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.W+tk.N+tk.E+tk.S)
        return AddFrame

    def __createCPFrame(self):
        """Will make the create page frame and return it"""
        CPFrame = tk.ttk.Frame(self.__root, width=self.__wWidth, height=self.__wHeight)
        CPFrame.columnconfigure(0, weight=6)
        CPFrame.columnconfigure(1, weight=1)
        CPFrame.columnconfigure(2, weight=1)
        # Sadly there is no way to do this easier
        CPFrame.rowconfigure(0, weight=1)
        CPFrame.rowconfigure(1, weight=1)
        CPFrame.rowconfigure(2, weight=1)
        CPFrame.rowconfigure(3, weight=1)
        CPFrame.rowconfigure(4, weight=1)
        CPFrame.rowconfigure(5, weight=1)
        CPFrame.rowconfigure(6, weight=1)
        CPFrame.rowconfigure(7, weight=1)
        CPFrame.rowconfigure(8, weight=1)
        CPFrame.rowconfigure(9, weight=1)
        CPFrame.rowconfigure(10, weight=1)
        CPFrame.rowconfigure(11, weight=1)
        CPFrame.rowconfigure(12, weight=1)
        CPFrame.rowconfigure(13, weight=1)
        CPFrame.rowconfigure(14, weight=1)
        CPFrame.rowconfigure(15, weight=1)
        CPFrame.rowconfigure(16, weight=1)
        CPFrame.rowconfigure(17, weight=1)
        CPFrame.rowconfigure(18, weight=1)
        CPFrame.rowconfigure(19, weight=1)
        CPFrame.rowconfigure(20, weight=1)
        CPFrame["borderwidth"] = 2
        CPFrame["relief"] = "sunken"
        CPFrame.grid(column=0, row=0, padx=self.__padX, pady=self.__padY, sticky=tk.W+tk.N+tk.E+tk.S)
        return CPFrame

    def __createWidgetsInMc(self, frame):
        """Creates the widgets in the first main choices menu frame"""

        def __openPage():
            """Will open the cms webpage"""
            url = "http://erik-virtualbox/"
            webbrowser.open(url, new=0, autoraise=True)
            
        # creating a frame to hold our image and title togheter when resizing happens
        s = ttk.Style()
        s.configure("new.TFrame", background="#F7F7F7")
        titleFrame = tk.ttk.Frame(frame, width=700, height=100, style="new.TFrame")
        titleFrame["relief"] = "flat"
        titleFrame.columnconfigure(0, weight=1)
        titleFrame.rowconfigure(0, weight=1)
        titleFrame.grid(column=0, row=0, sticky=tk.N+tk.S)

        # Adding image
        global __img 
        # We need to assign the img to a global other wise it will get "garbage collected" at the end of the function
        __img = ImageTk.PhotoImage(Image.open("C://Users/erikv/Documents/CMSFiles/DoNotEdit/PCMSLOGOSMALL.png").resize((80, 70)))
        imgLab = tk.Label(titleFrame, image=__img, bg="#F7F7F7")
        imgLab.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E)

        # Adding label with our title
        titleLab = tk.Label(titleFrame, text="Python Content Management System", bg="#F7F7F7" , font="Times 28 bold")
        titleLab.grid(column=1, row=0, sticky=tk.N+tk.W+tk.S)

        # Creating 5 buttons
        padY = 4
        padX = 110
        backgroundColor = "#cfd3d4"
        buttonFont = Font(family="Georgia", size=22)
        but1 = tk.Button(frame, text="Create new page (max 1)", bg=backgroundColor, font = buttonFont, command= lambda: self.__showFrame("CPFrame"))
        but2 = tk.Button(frame, text="Create Header + Text", bg=backgroundColor, font = buttonFont, command= lambda: self.__showFrame("HTFrame"))
        but3 = tk.Button(frame, text="Create Header + Text + Image", bg=backgroundColor, font = buttonFont, command= lambda: self.__showFrame("HTIFrame"))
        but4 = tk.Button(frame, text="Create Addition / List", bg=backgroundColor, font = buttonFont, command= lambda: self.__showFrame("AddFrame"))
        but5 = tk.Button(frame, text="Open CMS web page", bg=backgroundColor, font = buttonFont, command= lambda: __openPage())
        but6 = tk.Button(frame, text="Quit program", bg=backgroundColor, font = buttonFont, command= lambda: self.__quitProgram())
        lab1 = tk.Label(frame, text="Python Content Management System (PCMS)")
        but1.grid(column=0, row=1, columnspan=2,  pady=padY, padx=padX, sticky=tk.N+tk.W+tk.E+tk.S)
        but2.grid(column=0, row=2, columnspan=2, pady=padY, padx=padX, sticky=tk.N+tk.W+tk.E+tk.S)
        but3.grid(column=0, row=3, columnspan=2, pady=padY, padx=padX, sticky=tk.N+tk.W+tk.E+tk.S)
        but4.grid(column=0, row=4, columnspan=2, pady=padY, padx=padX, sticky=tk.N+tk.W+tk.E+tk.S)
        but5.grid(column=0, row=5, columnspan=2, pady=padY, padx=padX, sticky=tk.N+tk.W+tk.E+tk.S)
        but6.grid(column=0, row=6, columnspan=2, pady=padY, padx=padX, sticky=tk.N+tk.W+tk.E+tk.S)

    def __createWidgetsInHT(self, frame):
        """Creates the widgets in the header + text frame"""

        def __save():
            """Will check the input and save it"""

            # Checking if the file content of the given file isnt empty
            if (len(self.__fileContent) < 1):
                self.__error("Selected file is empty!")
                return

            # Checking if title is not empty
            if (len(enterTitleEntry.get()) < 1):
                self.__error("Title entry is empty!")
                return

            headerTextDic = {"title" : enterTitleEntry.get(), "fileContentList" : self.__fileContent}

            # sending the settings dic to the createWidgets class so it can be user
            self.__CW.generate("HT", headerTextDic)

            # Clearing the content of __fileContent so it can be used again
            self.__fileContent = []
            textVar1.set("Selected: No ")

            # Going back to the main menu + Sending confirmation message
            tk.messagebox.showinfo("Section added!", "A new section has been created and added to the page!")
            self.__showFrame("MCFrame")

        # Setting main font
        frame.option_add("*Font", "Roboto 22")
        # Creating a font for the title
        mainTitleFont = Font(family="Georgia", size=35)

        # Making a subframe to put our 2 subframes in to places them nice and togheter instead of them being far away from each other
        subFrame3 = tk.ttk.Frame(frame, width=700, padding=10)
        # Making 2 subframes so we can place certain widgets in it to bundle them togheter for layout purposes.
        subFrame1 = tk.ttk.Frame(subFrame3, width=700, padding=10)
        subFrame2 = tk.ttk.Frame(subFrame3, width=700, padding=10)

        # Creating all the widgets needed
        titleLab = tk.Label(frame, text="Add title and text to the website")
        titleLab.configure(font=mainTitleFont)
        enterTitleLab = tk.Label(subFrame1, text="Enter title:")
        enterTitleEntry = tk.Entry(subFrame1)
        selTextLab = tk.Label(subFrame2, text="Select text file:")
        selectTxtFileBut = tk.Button(subFrame2, text="Select file", command= lambda: self.__getFileContent(textVar1)) 
        textVar1 = tk.StringVar()
        textVar1.set("Selected: No ")
        textFileSelected = tk.Label(subFrame2, textvariable=textVar1)
        returnBut = tk.Button(frame, text="Return", command= lambda: self.__showFrame("MCFrame"))
        saveBut = tk.Button(frame, text="Save", command= lambda: __save())

        # Padding for all the widgets in this frame
        HTPadX = 10
        HTPadY = 2  

        # Placing the widgets in the subFrame1
        enterTitleLab.pack(side=tk.LEFT, padx=HTPadX, pady=HTPadY)
        enterTitleEntry.pack(side=tk.LEFT, padx=HTPadX, pady=HTPadY)
        # Placing the widgets in the subFrame2
        selTextLab.pack(side=tk.LEFT, padx=HTPadX, pady=HTPadY)
        selectTxtFileBut.pack(side=tk.LEFT, padx=HTPadX, pady=HTPadY)
        textFileSelected.pack(side=tk.LEFT, padx=HTPadX, pady=HTPadY)
        # Placing the 2 subframes in our subFrame3 
        subFrame2.pack(side=tk.BOTTOM, anchor=tk.W)
        subFrame1.pack(side=tk.BOTTOM, anchor=tk.W)

        # Placing the widgets / frame(s) in the main frame
        titleLab.grid(row=0, column=0, columnspan=3, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.E)
        subFrame3.grid(row=1, column=0, columnspan=3, padx=10, sticky=tk.N+tk.S+tk.W+tk.E)
        returnBut.grid(row=3, column=0, padx=20, pady=10, sticky=tk.W+tk.S)
        saveBut.grid(row=3, column=2, padx=20, pady=10, sticky=tk.E+tk.S)       

    def __createWidgetsInHTI(self, frame):
        """Creates the widgets in the header + text + image frame"""    

        def __getImage(textVar):
            """Will let the user select a image and will save the path"""

            # Opening the browse file window, only letting the user select .jpg and .png files and getting the _io.textiowrapper as a return
            file = tkinter.filedialog.askopenfile(mode = "r", filetypes = (("images", ".jpg .png"),))
            # checking if the textiowrapper isnt empty 
            if (file != None):
                    
                imagePath = file.name
                self.__imagePath = imagePath
                textVar.set("Selected: Yes")

        def __save():
            """Will check the input and save it"""

            # Checking if the file content, title or imagepath isnt empty
            if (len(self.__fileContent) < 1 or len(enterTitleEntry.get()) < 1 or self.__imagePath == None or borderVal.get() == None or len(altTextEntry.get()) < 1):
                tk.messagebox.showerror("Error", "One or more settings are not filled in (correctly)!")
                return

            headerTextImageDic = {"title" : enterTitleEntry.get(), "fileContentList" : self.__fileContent, "imagePath" : self.__imagePath,
                                  "makeBorder" : borderVal.get(), "altText" : altTextEntry.get(), "placementSide" : placementChoice.get()}

            # sending the settings dic to the createWidgets class so it can be user
            self.__CW.generate("HTI", headerTextImageDic)

            # Clearing the content of __fileContent and __imagePath so it can be used again
            self.__fileContent = []
            self.__imagePath = None
            textVar1.set("Selected: No ")
            textVar2.set("Selected: No ")

            # Going back to the main menu + Sending confirmation message
            tk.messagebox.showinfo("Section added!", "A new section has been created and added to the page!")
            self.__showFrame("MCFrame")

        # Setting main font
        frame.option_add("*Font", "Roboto 13")
        # Creating a font for the title
        mainTitleFont = Font(family="Georgia", size=40)

        # Creating all the widgets needed
        titleLab = tk.Message(frame, text="Add title, text and image to the website", width=700)
        titleLab.configure(font=mainTitleFont)
        enterTitleLab = tk.Label(frame, text="Enter title:")
        enterTitleEntry = tk.Entry(frame)
        selTextLab = tk.Label(frame, text="Select text file:")
        selectTxtFileBut = tk.Button(frame, text="Select file", command= lambda: self.__getFileContent(textVar1)) 
        textVar1 = tk.StringVar()
        textVar1.set("Selected: No ")
        textFileSelected = tk.Label(frame, textvariable=textVar1)
        selImageLab = tk.Label(frame, text="Select image:")
        textVar2 = tk.StringVar()
        textVar2.set("Selected: No ")
        selImageBut = tk.Button(frame, text="Select image", command= lambda: __getImage(textVar2))
        imageFileSelected = tk.Label(frame, textvariable=textVar2)
        altTextLab = tk.Label(frame, text="Enter alternative text:")
        altTextEntry = tk.Entry(frame)
        placementLab = tk.Label(frame, text="IMG placement side:")
        placementChoice = tk.ttk.Combobox(frame, values=["Left", "Right"])
        placementChoice.current(0)
        borderLab = tk.Label(frame, text="Create IMG border:")
        borderVal = tk.BooleanVar()
        borderRB1 = tk.Radiobutton(frame, text="Yes", variable=borderVal, value=True)
        borderRB2 = tk.Radiobutton(frame, text="No", variable=borderVal, value=False)
        returnBut = tk.Button(frame, text="Return", command= lambda: self.__showFrame("MCFrame"))
        saveBut = tk.Button(frame, text="Save", command= lambda: __save())
       
       # Padding for all the widgets in this frame
        HTPadX = 10
        HTPadY = 20

        titleLab.grid(row=0, column=0, columnspan=3, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.E+tk.S)
        enterTitleLab.grid(row=1, column=0, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        enterTitleEntry.grid(row=1, column=1, padx=HTPadX, pady=HTPadY, sticky=tk.E+tk.W+tk.N+tk.S)
        selTextLab.grid(row=2, column=0, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        selectTxtFileBut.grid(row=2, column=1, padx=HTPadX, pady=HTPadY, sticky=tk.E+tk.W+tk.N+tk.S)
        textFileSelected.grid(row=2, column=2, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        selImageLab.grid(row=3, column=0, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        selImageBut.grid(row=3, column=1, padx=HTPadX, pady=HTPadY, sticky=tk.E+tk.W+tk.N+tk.S)
        imageFileSelected.grid(row=3, column=2, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        altTextLab.grid(row=4, column=0, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        altTextEntry.grid(row=4, column=1, padx=HTPadX, pady=HTPadY, sticky=tk.E+tk.W+tk.N+tk.S)
        placementLab.grid(row=5, column=0, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        placementChoice.grid(row=5, column=1, padx=HTPadX, pady=HTPadY, sticky=tk.E+tk.W+tk.N+tk.S)
        borderLab.grid(row=6, column=0, columnspan=2, padx=HTPadX, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        borderRB1.grid(row=6, column=1, padx=50, pady=HTPadY, sticky=tk.W+tk.N+tk.S)
        borderRB2.grid(row=6, column=1, padx=50, pady=HTPadY, sticky=tk.E+tk.N+tk.S)
        returnBut.grid(row=7, column=0, padx=20, pady=10, sticky=tk.W+tk.S)
        saveBut.grid(row=7, column=2, padx=20, pady=10, sticky=tk.E+tk.S)  
        
    def __createWidgetsInAdd(self, frame):
        """Creates the widgets in the addition (list) frame"""

        def __save():
            """Will check the input and save it"""

            # Checking if the file content of the given file isnt empty
            if (len(self.__fileContent) < 1):

                self.__error("Selected file is empty!")
                return

            additionSettingsDic = {
                "fileContent" : self.__fileContent, 
                "listType" : listTypeChoice.get(), 
                "orderedBulletType" : selBulStyleOrChoice.get(), 
                "unorderedBulletType" : selBulStyleUnOrChoice.get(),
                "bulletPlacement" : bulPlacementChoice.get()
                }
            
            # sending the settings dic to the createWidgets class so it can be user
            self.__CW.generate("ADD", additionSettingsDic)

            # Clearing the content of __fileContent so it can be used again
            self.__fileContent = []
            textVar.set("Selected: No ")
            
            # Going back to the main menu + Sending confirmation message
            tk.messagebox.showinfo("Section added!", "A new section has been created and added to the page!")
            self.__showFrame("MCFrame")

        # Setting main font + making a font for the title of the page
        frame.option_add("*Font", "Roboto 13")
        mainTitleFont = Font(family="Georgia", size=40)

        # Creating the widgets needed
        mainTitle = tk.Label(frame, text="Add summary to the website")
        mainTitle.configure(font=mainTitleFont)
        selListLab = tk.Label(frame, text="Select list file:")
        textVar = tk.StringVar()
        selListBut = tk.Button(frame, text="Select list", command= lambda: self.__getFileContent(textVar), height=1, width=10)
        textVar.set("Selected: No ")
        listSelected = tk.Label(frame, textvariable=textVar)
        listTypeLab = tk.Label(frame, text="Select list type:")
        listTypeChoice = ttk.Combobox(frame, values=["Ordered List", "Unordered List"])
        listTypeChoice.current(0)
        selBulletStyleOrLab = tk.Label(frame, text="Select bullet style for ordered list:")
        selBulStyleOrChoice = ttk.Combobox(frame, values=["Numbers (1, 2, 3)", "Letters (A, B, C)"])
        selBulStyleOrChoice.current(0)
        selBulletStyleUnOrLab = tk.Label(frame, text="Select bullet style for unordered list:")
        selBulStyleUnOrChoice = ttk.Combobox(frame, values=["Disc (●)", "Square (□)", "Circle (○)"])
        selBulStyleUnOrChoice.current(0)
        bulPlacementLocLab = tk.Label(frame, text="Placement of the bullet points:")
        bulPlacementChoice = ttk.Combobox(frame, values=["Inside", "Outside"])
        bulPlacementChoice.current(0)
        returnBut = tk.Button(frame, text="Return", command= lambda: self.__showFrame("MCFrame"), height=2, width=10)
        saveBut = tk.Button(frame, text="Save", command= lambda: __save(), height=2, width=10)

        # Placing the widgets
        padX = 10
        padY = 30
        mainTitle.grid(row=0, column=0, columnspan=3, padx=padX, pady=padY, sticky=tk.N+tk.W+tk.E+tk.S)
        selListLab.grid(row=1, column=0, columnspan=2, padx=padX, pady=padY, sticky=tk.N+tk.W+tk.S)
        selListBut.grid(row=1, column=1, padx=padX, pady=padY, sticky=tk.W+tk.E)
        listSelected.grid(row=1, column=2, padx=padX, pady=padY, sticky=tk.N+tk.W+tk.S)
        listTypeLab.grid(row=2, column=0, columnspan=2, padx=padX, pady=padY, sticky=tk.N+tk.W+tk.S)
        listTypeChoice.grid(row=2, column=1, padx=padX, pady=padY, sticky=tk.W+tk.E+tk.N+tk.S)
        selBulletStyleOrLab.grid(row=3, column=0, columnspan=2, padx=padX, pady=padY, sticky=tk.N+tk.W+tk.S)
        selBulStyleOrChoice.grid(row=3, column=1, padx=padX, pady=padY, sticky=tk.W+tk.E+tk.N+tk.S)
        selBulletStyleUnOrLab.grid(row=4, column=0, columnspan=2, padx=padX, pady=padY, sticky=tk.N+tk.W+tk.S)
        selBulStyleUnOrChoice.grid(row=4, column=1, padx=padX, pady=padY, sticky=tk.W+tk.E+tk.N+tk.S)
        bulPlacementLocLab.grid(row=5, column=0, columnspan=2, padx=padX, pady=padY, sticky=tk.N+tk.W+tk.S)
        bulPlacementChoice.grid(row=5, column=1, padx=padX, pady=padY, sticky=tk.W+tk.E+tk.N+tk.S)
        returnBut.grid(row=6, column=0, padx=20, pady=10, sticky=tk.W+tk.S)
        saveBut.grid(row=6, column=2, padx=20, pady=10, sticky=tk.E+tk.S)

    def __createWidgetsInCP(self, frame):
        """Creates the widgets in the create page frame"""

        def __savePageHasBeenMade():
            """Will save the state of the pagehasbeenmade variable to a file"""

            with open("//ERIK-VIRTUALBOX/Web/pagehasbeenmade.txt", "w+") as file:

                file.write("True")

        def __save():
            """Will save the selected settings and return to main choice menu"""

            # Getting all entries and placing them in a dictionary
            settingsDic = {
                "mainTitle" : titleEntry.get(), "fileContentList" : self.__fileContent, "colorsDic" : self.__colors,
                "font" : fontChoice.get(), "mainTitleItalic" : italicChoice.get(), "mainTitleCapital" : capitalChoice.get(),
                "otherTitleUnderline" : titleUnderlineChoice.get(), "roomTitleText" : roomTitleTextEntry.get(),
                "roomImageText" : roomImageTextEntry.get(), "imageBorder" : selBorderChoice.get(),
                "roundedImgCorners" : roundedCornersChoice.get(), "borderWidth" : borderWidthEntry.get(), "roomImageBorder" : roomImageBorderEntry.get()  
                }

            # Checking if the entrys that require number input are only numbers and not negative numbers or letters, -1 will return False at isDigit()
            if not (settingsDic["roomTitleText"].isdigit() and settingsDic["roomImageText"].isdigit() and settingsDic["roomImageBorder"].isdigit() and settingsDic["borderWidth"].isdigit()):
                self.__error("Numeric input is not allowed to be negative or contain letters!")
                return

            # Checking if not all the entries have at least a lenght of more then 0 (not empty) (4 in colorsDic)
            if not (len(settingsDic["mainTitle"]) > 0 and len(settingsDic["fileContentList"]) > 0 and len(settingsDic["font"]) > 0 and len(settingsDic["mainTitleItalic"]) > 0 
                and len(settingsDic["mainTitleCapital"]) > 0 and len(settingsDic["otherTitleUnderline"]) > 0 and len(settingsDic["roomTitleText"]) > 0 
                and len(settingsDic["roomImageText"]) > 0 and len(settingsDic["imageBorder"]) > 0 and len(settingsDic["roundedImgCorners"]) > 0 
                and len(settingsDic["borderWidth"]) > 0 and len(settingsDic["roomImageBorder"]) > 0 and len(settingsDic["colorsDic"]) == 4):

                self.__error("One or more fields have not been filled in!")
                return         

            # Image border width is not allowed to be more then 5. checking if it isn't too big
            if (int(settingsDic["borderWidth"]) > 5):

                self.__error("Image border width can not be more then 5px!")
                return

            # Checking if the colorDic has 4 valid hex codes
            colorsDic = settingsDic["colorsDic"]
            for k, v in colorsDic.items():

                # Checking if the value (str)  doesnt start with #
                if not (v.find("#") == 0):
                        
                    self.__error("Something went wrong with the color selections! please re enter choices and try again!")
                    return

            # sending the settings dic to the createWidgets class so it can be used
            self.__CW.generate("CP", settingsDic)

            # Clearing the fileContent list so we can use it again
            self.__fileContent = []
            textVar0.set("Selected: No ")
            textVar1.set("Selected: No ")
            textVar2.set("Selected: No ")
            textVar3.set("Selected: No ")
            textVar4.set("Selected: No ")

            # Indicating that a page has been created so we dont get more then one page
            self.__pageHasBeenCreated = True
            # Saving the pageHasBeenCreated var to a file, if user restarts we load this so we can check if they made a page before exiting the cms
            __savePageHasBeenMade()

            # Going back to the main menu + Sending confirmation message
            tk.messagebox.showinfo("Page created!", "A new page has been created. You can now add content to it!")
            self.__showFrame("MCFrame")

        def __pickColor(frame, tag):
            """Will pick a color and assign the hex to dictionary under the right tag"""
            
            # Getting the rgb and hex in a tuple from the colorpicker
            colorString = askcolor(parent=frame, title="Pick a color")
            # Getting the second element from the tuple (hex code)
            colorString = colorString[1]
            # Saving the hex code under the given tag in the dic
            self.__colors.update({tag : colorString})
            # Changing the textvariable in the right label so the user knows he has set te file / color
            if (tag == "bgColor"):
                textVar1.set("Selected: Yes")
            elif(tag == "txtColor"):
                textVar2.set("Selected: Yes")
            elif(tag == "mainTitleColor"):
                textVar3.set("Selected: Yes")
            elif(tag == "otherTitleColor"):
                textVar4.set("Selected: Yes")

        # Setting main font
        frame.option_add("*Font", "Roboto 10")
        # Making the fonts we're going to use for certain titles
        mainTitleFont = Font(family="Georgia", size=20)
        otherTitleFont = Font(family="Georgia", size=16)

        ## Create page
        cpLabel = tk.Label(frame, text="Create page options")
        cpLabel.configure(font=mainTitleFont)
        # Select title (page and tab) (<h1> + <title>)
        selTitleLabel = tk.Label(frame, text="Insert title page/tab:")
        titleEntry = tk.Entry(frame)
        # Select leading text from file (<p>)
        selectTxtLab = tk.Label(frame, text="Select leading text file:")
        textVar0 = tk.StringVar()
        selectTxtFileBut = tk.Button(frame, text="Select file", command= lambda: self.__getFileContent(textVar0)) 
        fileChoice = tk.Label(frame, textvariable=textVar0)
        # Insert background hex color
        bgColorLabel = tk.Label(frame, text="Select background color hex code:")
        selColorBut1 = tk.Button(frame, text= "Select color", command= lambda: __pickColor(frame, "bgColor"))
        textVar1 = tk.StringVar()
        colorChoice1 = tk.Label(frame, textvariable=textVar1)       
        # Insert text hex color
        txtColorLabel = tk.Label(frame, text="Insert text color hex code:")
        selColorBut2 = tk.Button(frame, text="Select color", command= lambda: __pickColor(frame, "txtColor"))
        textVar2 = tk.StringVar()
        colorChoice2 = tk.Label(frame, textvariable=textVar2)
        # Select font type (3 options)
        selFontLabel = tk.Label(frame, text="Select font type:")
        fontChoice = ttk.Combobox(frame, values=["Times New Roman", "Roboto", "Courier New"])
        fontChoice.current(0)
        ## Main title options
        mainTitleOptLab = tk.Label(frame, text="Main title options")
        mainTitleOptLab.configure(font=otherTitleFont)
        # Select main title (header 1) text color hex code
        selMTitleColorLabel = tk.Label(frame, text="Insert main title color hex code:")
        selColorBut3 = tk.Button(frame, text="Select color", command= lambda: __pickColor(frame, "mainTitleColor"))
        textVar3 = tk.StringVar()
        colorChoice3 = tk.Label(frame, textvariable=textVar3)
        # Italic yes or no
        italicChoiceLabel = tk.Label(frame, text="Make title italic:")
        italicChoice = ttk.Combobox(frame, values=["No", "Yes"])
        italicChoice.current(0)
        # Convert title to all caps
        makeCapChoiceLabel = tk.Label(frame, text="Make title capital:")
        capitalChoice = ttk.Combobox(frame, values=["No", "Yes"])
        capitalChoice.current(0)
        ## Other titles / headers options
        titleOptionsLab = tk.Label(frame, text="Other titles options")
        titleOptionsLab.configure(font=otherTitleFont)
        # Select title text color hex code
        titleColorLab = tk.Label(frame, text="Insert title color hex code:")
        selColorBut4 = tk.Button(frame, text="Select color", command= lambda: __pickColor(frame, "otherTitleColor"))
        textVar4 = tk.StringVar()
        colorChoice4 = tk.Label(frame, textvariable=textVar4)
        # Titles underlined yes or no
        titleUnderlineChoiceLab = tk.Label(frame, text="Underline titles:")
        titleUnderlineChoice = ttk.Combobox(frame, values=["No", "Yes"])
        titleUnderlineChoice.current(0)
        # Select room between titles and text in px
        roomTitleTextLab = tk.Label(frame, text="Insert room between text and titles in px:")
        roomTitleTextEntry = tk.Entry(frame)
        roomTitleTextEntry.insert(0, "5")
        ## Image options
        imageOptionsLab = tk.Label(frame, text="Image options")
        imageOptionsLab.configure(font=otherTitleFont)
        # Select room between image and text
        roomImageTextLab = tk.Label(frame, text="Insert room between images and text in px:")
        roomImageTextEntry = tk.Entry(frame)
        roomImageTextEntry.insert(0, "5")       
        # Select border (none, Solid, Groove, Double)
        selBorderChoiceLab = tk.Label(frame, text="Select image border type:")
        selBorderChoice = ttk.Combobox(frame, values=["solid", "groove", "double"])
        selBorderChoice.current(0)
        # Rounded corners of 5px yes or no
        roundedCornersLab = tk.Label(frame, text="Rounded corners:")
        roundedCornersChoice = ttk.Combobox(frame, values=["No", "Yes"])
        roundedCornersChoice.current(0)
        # Width of border (max 5px)
        borderWidthLab = tk.Label(frame, text="Image border width in px (max 5): ")
        borderWidthEntry  = tk.Entry(frame)
        borderWidthEntry.insert(0, "2")
        # Room between image and border in px
        roomImageBorderLab = tk.Label(frame, text="Insert room between image and border in px:")
        roomImageBorderEntry = tk.Entry(frame)
        roomImageBorderEntry.insert(0, "0")
        # Save button which will also check the given input
        saveBut = tk.Button(frame, text="Save Settings", command= lambda: __save())
        # Return button which will return to the Main Choice frame
        retBut = tk.Button(frame, text="Return", command= lambda: self.__showFrame("MCFrame"))

        # Setting the text variables of our "input selected" labels to NO
        textVar0.set("Selected: No ")
        textVar1.set("Selected: No ")
        textVar2.set("Selected: No ")
        textVar3.set("Selected: No ")
        textVar4.set("Selected: No ")
        
        cpPadX = 2
        cpPadY = 2

        # Placing everything on the right place
        # GENERAL OPTIONS
        cpLabel.grid(column=1, row=0, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        selTitleLabel.grid(column=0, row=1, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        titleEntry.grid(column=1, row=1, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        selectTxtLab.grid(column=0, row=2, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        selectTxtFileBut.grid(column=1, row=2, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        fileChoice.grid(column=2, row=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        bgColorLabel.grid(column=0, row=3, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        selColorBut1.grid(column=1, row=3, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        colorChoice1.grid(column=2, row=3, sticky=tk.N+tk.S+tk.W, padx=cpPadX, pady=cpPadY)
        txtColorLabel.grid(column=0, row=4, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        selColorBut2.grid(column=1, row=4, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        colorChoice2.grid(column=2, row=4, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        selFontLabel.grid(column=0, row=5, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        fontChoice.grid(column=1, row=5, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        # MAIN TITLE OPTIONS
        mainTitleOptLab.grid(column=1, row=6,  sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        selMTitleColorLabel.grid(column=0, row=7, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        selColorBut3.grid(column=1, row=7, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        colorChoice3.grid(column=2, row=7, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        italicChoiceLabel.grid(column=0, row=8, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        italicChoice.grid(column=1, row=8, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        makeCapChoiceLabel.grid(column=0, row=9, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        capitalChoice.grid(column=1, row=9, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        # OTHER TITLES OPTION
        titleOptionsLab.grid(column=1, row=10, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        titleColorLab.grid(column=0, row=11, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        selColorBut4.grid(column=1, row=11, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        colorChoice4.grid(column=2, row=11, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        titleUnderlineChoiceLab.grid(column=0, row=12, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        titleUnderlineChoice.grid(column=1, row=12, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        roomTitleTextLab.grid(column=0, row=13, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        roomTitleTextEntry.grid(column=1, row=13, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        # IMAGE OPTIONS
        imageOptionsLab.grid(column=1, row=14,  sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        roomImageTextLab.grid(column=0, row=15, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        roomImageTextEntry.grid(column=1, row=15, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        selBorderChoiceLab.grid(column=0, row=16, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        selBorderChoice.grid(column=1, row=16, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        roundedCornersLab.grid(column=0, row=17, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        roundedCornersChoice.grid(column=1, row=17, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        borderWidthLab.grid(column=0, row=18, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        borderWidthEntry.grid(column=1, row=18, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        roomImageBorderLab.grid(column=0, row=19, columnspan=2, sticky=tk.N+tk.W+tk.S, padx=cpPadX, pady=cpPadY)
        roomImageBorderEntry.grid(column=1, row=19, sticky=tk.N+tk.W+tk.S+tk.E, padx=cpPadX, pady=cpPadY)
        saveBut.grid(column=2, row=20, sticky=tk.N+tk.S+tk.E, padx=20, pady=10)
        retBut.grid(column=0, row=20, sticky=tk.N+tk.S+tk.W, padx=20, pady=10)

    def startGUI(self):
        """Starts and runs the GUI part of the program"""
        
        def __pageWasCreated():
            """Will check what the state of pagehasbeencreated was before the cms got closed (if this is the case)"""
            
            # Checking if the file exist and opening in read mode if it does
            if (os.path.isfile("//ERIK-VIRTUALBOX/Web/pagehasbeenmade.txt")):
                with open("//ERIK-VIRTUALBOX/Web/pagehasbeenmade.txt", "r") as file:
                
                # Checking if the line == True, if this is not the case we dont return false, since the variable is False by default thanks to __init__
                    firstLine = file.readline()
                    if (firstLine == "True"):
                        return True
                    else: return False
            else: return False

        # Checking if the pagehasbeencreated file exist, if so we check what the state of the variable was before the cms got closed
        self.__pageHasBeenCreated = __pageWasCreated()

        # Creating the __root window
        self.__root = tk.Tk()
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)
        self.__root.title("Python Content Management System")

        # Defining the window size
        self.__wWidth = 850
        self.__wHeight = 850

        # Giving the start size + where to open it (how many pixels from x and y)
        self.__root.geometry("%dx%d+%d+%d" % (self.__wWidth + 40, self.__wHeight + 20, 300, 10))

        # Creating the frames and assigning them to our variables
        self.__MCFrame = self.__createMCFrame()
        self.__HTFrame = self.__createHTFrame()
        self.__HTIFrame = self.__createHTIFrame()
        self.__AddFrame = self.__createAddFrame()
        self.__CPFrame = self.__createCPFrame()

        # Creating all the widgets to all the frames
        self.__createWidgetsInMc(self.__MCFrame)
        self.__createWidgetsInHT(self.__HTFrame)
        self.__createWidgetsInHTI(self.__HTIFrame)
        self.__createWidgetsInAdd(self.__AddFrame)
        self.__createWidgetsInCP(self.__CPFrame)

        # Hiding all the frames in reversed order but leaving the main choice frame visible (unhidden)
        self.__CPFrame.grid_forget()
        self.__AddFrame.grid_forget()
        self.__HTIFrame.grid_forget()
        self.__HTFrame.grid_forget()
        self.__MCFrame.grid_forget()

        # Displaying the main choice frame
        self.__showFrame("MCFrame")

        # Starting the tkinter event loop
        self.__root.mainloop()