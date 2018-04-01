import os

# Install Requirements

os.system("pip install requirements.txt")

import Tkinter as tk, tkFileDialog, tkSimpleDialog, webbrowser, shutil
from time import sleep

# Open Put.io in default browser

def OpenPutio():
    url = 'https://api.put.io/v2/oauth2/authenticate?client_id=28&response_type=oob'
    webbrowser.open(url, new=1, autoraise=True)

# Call Open Put.io Function

OpenPutio()

# Create Settings Class

class Settings:
    TorrentFolder = ""
    WatchFolder = ""
    Token =""
    
# Get Folder Location

def DialogPrompt(PromptTitle):
    root = tk.Tk()
    root.withdraw() #use to hide tkinter window
    currdir = os.getcwd()
    SelectedFolder = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title=PromptTitle) + "/"
    return SelectedFolder

# Create 1st Input Dialog Class

class MyDialog1(tkSimpleDialog.Dialog):
    
    def body(self, master):
        self.geometry("300x100")
        tk.Label(master, text="Enter your Put.io Token").grid(row=0)

        self.e1 = tk.Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus
    
    def apply(self):
        first = self.e1.get()
        self.result = first

# Get 1st Input Dialog

def InputDialog1():
    root = tk.Tk()
    root.withdraw()
    root.focus_force()
    dialog = MyDialog1(root, "Putio Sonarr")
    dialog.result
    return dialog.result

# Create 2nd Input Dialog Class

class MyDialog2(tkSimpleDialog.Dialog):
    def body(self, master):
        self.geometry("300x100")
        tk.Label(master, text="Enter your Put.io Folder ID #").grid(row=0)

        self.e1 = tk.Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus
    
    def apply(self):
        first = self.e1.get()
        self.result = first

# Get 2nd Input Dialog

def InputDialog2():
    root = tk.Tk()
    root.withdraw()
    root.focus_force()
    dialog = MyDialog2(root, "Putio Sonarr")
    dialog.result
    return dialog.result

# Save Settings to File

def CreateSettings(line1, line2, line3, line4):
    File = open(line1 + "Settings.txt", 'a')
    File.write(line1 + "\n")
    File.write(line2 + "\n")
    File.write(line3 + "\n")
    File.write(line4 + "\n")
    File.close()

# Copy files to Torrent Folder

def CopyFiles(path):
    CurrentDir = os.getcwd() + "/"
    shutil.copy(CurrentDir + "SonarrPutio.py", path + "SonarrPutio.py")
    shutil.copy(CurrentDir + "putio.py", path + "putio.py")


# Call Functions

Settings.TorrentFolder = DialogPrompt('Please select Torrent Folder')

Settings.WatchFolder =  DialogPrompt('Please select Watch Folder') 

Settings.Token = InputDialog1()

Settings.FolderID = InputDialog2()

CreateSettings(Settings.TorrentFolder, Settings.WatchFolder, Settings.Token, Settings.FolderID)

CopyFiles(Settings.TorrentFolder)
