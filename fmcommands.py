"""
    fmcommands.py
    DGTavo88

    Contains the functions used by the "File" menu options.
"""

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tools
import traceback
import sys
import globals

#User decides to save file.
def EndProgramYes():
    SaveFileProcess() #Save file.
    globals.popup.destroy() #Destroy the pop-up.
    sys.exit(0) #End the program.

#User desides to not save file.
def EndProgramNo():
    globals.popup.destroy() #Destroy the pop-up.
    sys.exit(0) #End the program.

#User decides to not end the program.
def EndProgramCancel():
    globals.popup.destroy() #Destroy the pop-up.

def EndWorldProgram():
    dtext = globals.tobject.GetText()    #Get the text from the globals.tobject.
    if dtext != "" and dtext != " " and dtext != globals.tobject.loadedtext: #Check that the text isn't empty or just a space.
        globals.popup = Tk()    #Create pop-up.
        globals.popup.title(globals.data["newfile_saveprompt"]) #Change title of pop-up.
        prompt = Label(globals.popup, text = globals.data["newfile_saveprompt"], font = tools.GetFont("text"))  #Create label on pop-up.
        prompt.grid(row = 0, column = 0)    #Display label.
        style = ttk.Style() #Create style.
        style.map("TButton", background = [("pressed", "white"), ("active", "green")])  #Set new style.
        byes = ttk.Button(globals.popup, text = globals.data["option_yes"], command = EndProgramYes, style = "TButton")  #Create yes button.
        bno = ttk.Button(globals.popup, text = globals.data["option_no"], command = EndProgramNo) #Create "no" button.
        bcancel = ttk.Button(globals.popup, text = globals.data["option_cancel"], command = EndProgramCancel) #Create "cancel" button.
        #byes.pack()
        byes.grid(row = 2, column = 0, padx = (4, 32)) #Display "yes" button.
        #bno.pack()
        bno.grid(row = 2, column = 1, padx=(4, 32)) #Display "no" button.
        #bcancel.pack()
        bcancel.grid(row = 2, column = 2, padx=(4, 32)) #Display "cancel" button.
    else:
        sys.exit(0) #End the program.

#Update window title + some variables once the user has created a new file.
def NewFileYUpdate():
    globals.loadedFile = False
    globals.loadedDirectory = "-1"
    tools.UpdateTitle() #Update title.
    globals.newFile = False

#User decides to create new file.
def NewFileYes():
    globals.newFile = True
    SaveFileProcess() #Save file content.
    globals.popup.destroy() #Destroy pop-up.
    globals.tobject.DeleteText() #Delete the text from the globals.tobject.
    globals.loadedFile = False
    globals.loadedDirectory = "-1"
    tools.UpdateTitle()  #Update title.

def NewFileNo():
    globals.popup.destroy() #Destroy pop-up-
    globals.tobject.DeleteText() #Delete text from globals.tobject.
    globals.loadedFile = False
    globals.loadedDirectory = "-1"

def NewFileCancel():
    globals.popup.destroy() #Destroy pop-up.

def NewFileProcess():
    dtext = globals.tobject.GetText() #Get text from globals.tobject.
    if dtext != "" or dtext != " ": #Check that text isn't empty or just a space.
        globals.popup = Tk() #Create new tkinter window.
        globals.popup.title(globals.data["newfile_saveprompt"]) #Set pop-up title.
        prompt = Label(globals.popup, text = globals.data["newfile_saveprompt"], font = tools.GetFont("text")) #Create label on pop-up.
        prompt.grid(row = 0, column = 0) #Display label.
        style = ttk.Style() #Create new style.
        style.map("TButton", background = [("pressed", "white"), ("active", "green")]) #Set new style.
        byes = ttk.Button(globals.popup, text = globals.data["option_yes"], command = NewFileYes, style = "TButton") #Create "yes" button.
        bno = ttk.Button(globals.popup, text = globals.data["option_no"], command = NewFileNo) #Create "no" button.
        bcancel = ttk.Button(globals.popup, text = globals.data["option_cancel"], command = NewFileCancel) #Create "cancel" button.
        #byes.pack()
        byes.grid(row = 2, column = 0) #Display "yes" button.
        #bno.pack()
        bno.grid(row = 2, column = 1) #Display "no" button.
        #bcancel.pack()
        bcancel.grid(row = 2, column = 2) #Display "cancel" button.
    else:
        globals.tobject.DeleteText() #Delete text from globals.tobject.
        globals.loadedFile = False
        globals.loadedDirectory = "-1"

def SaveFileProcess():
    if globals.loadedFile == True and globals.loadedDirectory != "-1": #If file loaded and directory is not "-1".
        print("Saving file...")
        with open(globals.loadedDirectory, "w", encoding = "utf-8") as savefile:   #Open file for writing with "utf-8" encoding.
            print(globals.tobject.GetText())
            savefile.write(globals.tobject.GetText()) #Write globals.tobject text to file.
        globals.tobject.loadedtext = globals.tobject.GetText()
        globals.checked_text = False
        tools.UpdateTitle()  #Update window title.
        print("File saved successfully.")
        if globals.newFile == True:
            NewFileYUpdate() #Update window.
    else:
        SaveFileAsProcess() #Go to SaveFileAsProcess.

def SaveFileAsProcess():
    print("Saving file as...")
    try:
        globals.loadedDirectory = filedialog.asksaveasfilename(initialdir = "%desktop%", title = globals.data["savemenu_savetitle"], filetypes = ((globals.data["savemenu_texttype"], "*.txt"), (globals.data["savemenu_alltypes"], "*.*"))) #Ask user for file path.
        globals.loadedFile = True
        if globals.loadedDirectory != "":   #If we have a path.
            if not ".txt" in globals.loadedDirectory:
                globals.loadedDirectory += ".txt"
            with open(globals.loadedDirectory, "w", encoding = "utf-8") as savefile:    #Open file for writing with "utf-8" encoding.
                print(globals.tobject.GetText())
                savefile.write(globals.tobject.GetText())    #Write globals.tobject text to the file.
            print("File saved successfully.")
            globals.tobject.loadedtext = globals.tobject.GetText()
            globals.checked_text = False
            tools.UpdateTitle()  #Update window title.
            if globals.newFile == True:
                NewFileYUpdate() #Update window title.
        else:
            globals.loadedFile = False
            globals.loadedDirectory = "-1"
            print("File was not saved.")
    except:
        print("Failed to save file.")
        print(traceback.format_exc())

def LoadFileProcess():
    print("Loading file...")
    try:
        globals.loadedDirectory = filedialog.askopenfilename(initialdir = "%desktop%", title = globals.data["savemenu_savetitle"], filetypes = ((globals.data["savemenu_texttype"], "*.txt"), (globals.data["savemenu_alltypes"], "*.*"))) #Get file path.
        if globals.loadedDirectory != "":   #If we have a file path.
            globals.loadedFile = True
            with open(globals.loadedDirectory, "r", encoding = "utf-8") as savefile:    #Open file for reading with "utf-8" encoding.
                globals.tobject.ReplaceText(savefile.read()) #Read text from file and set it as the globals.tobject text.
            globals.tobject.loadedtext = globals.tobject.GetText()
            globals.checked_text = False
            tools.UpdateTitle()  #Update window title.
            print("File loaded successfully.")
        else:
            globals.loadedFile = False
            globals.loadedDirectory = "-1"
            print("File wasn't loaded.")
    except:
        print("Failed to load file.")
        print(traceback.format_exc())

def GetSaveDir():
    return globals.loadedDirectory

def CheckFileLoaded():
    return globals.loadedFile
