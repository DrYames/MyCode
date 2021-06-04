import tkinter as tk
from tkinter import ttk

FILENAME = "preferences.txt"
# could not figure this one out 
def readFile():
    try:
        FILENAME = open("preferences.txt", "r")
        preferences = {}
        with open (FILENAME, "r") as pfile:
            for line in pfile:
                (key, val) = line.split()
                preferences[int(key)] = val
                print(preferences)
            return preferences                
    except FileNotFoundError:
        print("Could not find file 'preferences.txt' in system.")

class PreferencesFrame(ttk.Frame):
    def __init__(self, parent):
        # parent class constructor
        ttk.Frame.__init__(self, parent, padding="30 30 30 30")
        self.parent = parent

        # define string variables for text entry data fields
        self.name = tk.StringVar()
        self.language = tk.StringVar()
        self.autosave = tk.StringVar()
        self.errorname = tk.StringVar()
        self.errorlang = tk.StringVar()
        self.errorsave = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        self.pack()

        nameLabel = ttk.Label(self, text = "Name:").grid(column=0, row=0, sticky=tk.E)
        nameEntry = ttk.Entry(self, textvariable = self.name, width=30).grid(column=1, row=0)
        scndLabel1 = ttk.Label(self, textvariable = self.errorname, state="readonly").grid(column=2, row=0, sticky=tk.E)
        self.name.set("Joel Murach")

        langLabel = ttk.Label(self, text = "Language:").grid(column=0, row=1, sticky=tk.E)
        langEntry = ttk.Entry(self, textvariable = self.language, width=30).grid(column=1, row=1)
        scndLabel2 = ttk.Label(self, textvariable = self.errorlang, state="readonly").grid(column=2, row=1, sticky=tk.E)
        self.language.set("English")

        saveLabel = ttk.Label(self, text = "Auto Save Every X Minutes:").grid(column=0, row=2, sticky=tk.E)
        saveEntry = ttk.Entry(self, textvariable = self.autosave, width=30).grid(column=1, row=2)
        scndLabel3 = ttk.Label(self, textvariable = self.errorsave, state="readonly").grid(column=2, row=3, sticky=tk.E)
        self.autosave.set("x")

        # method to create buttons
        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5,pady=5)

    def makeButtons(self):
        # create and display save and cancel buttons
        buttonFrame = ttk.Frame(self)

        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E)

        ttk.Button(buttonFrame, text="Save", command=self.saveFile).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Cancel", command=self.parent.destroy).grid(column=1, row=0)

    def saveFile(self):
        # check entries
        try:
            testName = self.name.get()
            testLang = self.language.get()
            testSave = self.autosave.get()
            if (testName==isinstance(testName, str)):
                scndLabel1 = "Required."
            elif (testLang==isinstance(testLang, str)):
                scndLabel2 = "Required."
            elif (testLang==isinstance(testSave, int)):
                scndLabel3 = "Must be valid integer."
            
        except ValueError:
            print("whoops")
