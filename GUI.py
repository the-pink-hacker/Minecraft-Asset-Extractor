import os, webbrowser
from Extract import *
from tkinter import *
from tkinter import filedialog

def extract():
	Extract(
	os.path.normpath(outputLocation.get()), # Output Location
	packName.get(), # Pack Name
	minecraftVersion.get(), # Minecraft Version
	minecraftVersionFull.get(), # Full Minecraft Version
	packPNGSelect.get(), # pack.png
	description.get(), # Description
	formatChoices.get(), # Pack Format
	bool(autoPackBool.get()), # Auto Pack Format
	bool(soundsBool.get()), # Sounds
	bool(languagesBool.get()), # LANG
	bool(zipBool.get()), # Zip
	bool(compatibilityBool.get())) # Compatibility

def openFolder():
	folder = filedialog.askdirectory(initialdir=os.path.normpath("C://"), title="Select Output Location")
	
	if folder != "":
		outputLocation.delete(0, END)
		outputLocation.insert(0, folder)

def openFile():
	folder = filedialog.askopenfilename(initialdir=os.path.normpath("C://"), title="Select File", filetypes =(("PNG", "*.png"),("All Files","*.*")))

	if folder != "":
		packPNGSelect.delete(0, END)
		packPNGSelect.insert(0, folder)

def packFormatButton():
	if autoPackBool.get() == False:
		packFormat.configure(state="active")
	elif autoPackBool.get() == True:
		packFormat.configure(state="disabled")

def packPNGButton():
	if packPNGBool.get() == True:
		packPNGSelect.configure(state="normal")
		packPNGSelectButton.configure(state="normal")
	elif packPNGBool.get() == False:
		packPNGSelect.configure(state="disabled")
		packPNGSelectButton.configure(state="disabled")

def callback(url):
    webbrowser.open_new(url)

def closeCredit(credit):
	credit.destroy()

def creditUI():
	credit = Tk()

	credit.title("Credit")
	credit.geometry("400x300")
	credit.resizable(False, False)

	creditTitleText = Label(credit, text="Minecraft Asset Extractor\nBy: Ryan Garrett")
	creditTitleText.grid(row=0, column=1)

	creditText = Label(credit, text="Ryan Garret (RyanGar46):")
	creditText.grid(row=1, column=0, sticky="W")

	github = Label(credit, text="GitHub", fg="blue", cursor="hand2", font=('Arial',9,'underline'))
	github.grid(row=2, column=0, sticky="W")
	github.bind("<Button-1>", lambda e: callback("https://github.com/RyanGar46"))

	githubProject = Label(credit, text="Minecraft Asset Extractor", fg="blue", cursor="hand2", font=('Arial',9,'underline'))
	githubProject.grid(row=3, column=0, sticky="W")
	githubProject.bind("<Button-1>", lambda e: callback("https://github.com/RyanGar46/Minecraft-Asset-Extractor"))

	twitter = Label(credit, text="Twitter", fg="blue", cursor="hand2", font=('Arial',9,'underline'))
	twitter.grid(row=4, column=0, sticky="W")
	twitter.bind("<Button-1>", lambda e: callback("https://twitter.com/RyanGar46"))

	youtube = Label(credit, text="YouTube", fg="blue", cursor="hand2", font=('Arial',9,'underline'))
	youtube.grid(row=5, column=0, sticky="W")
	youtube.bind("<Button-1>", lambda e: callback("https://www.youtube.com/channel/UCa5CoSRScfDUtoEAenjbnZg"))

	curseforge = Label(credit, text="CurseForge", fg="blue", cursor="hand2", font=('Arial',9,'underline'))
	curseforge.grid(row=6, column=0, sticky="W")
	curseforge.bind("<Button-1>", lambda e: callback("https://www.curseforge.com/members/ryangar46/projects"))

	planetMC = Label(credit, text="Planet Minecraft", fg="blue", cursor="hand2", font=('Arial',9,'underline'))
	planetMC.grid(row=7, column=0, sticky="W")
	planetMC.bind("<Button-1>", lambda e: callback("https://www.planetminecraft.com/member/ryangar46"))

	version = Label(credit, text="V0.2.1.1 - Alpha")
	version.place(relx=0.0, rely=1.0, anchor="sw")

	closeButton = Button(credit, text="Close", command=lambda:closeCredit(credit))
	closeButton.place(relx=1.0, rely=1.0, anchor="se")

	credit.mainloop()

# Creates the available choices in the pack format drop down.
packFormats = [
"1",
"2",
"3",
"4",
"5",
"6",
"7"
]

root = Tk()

autoPackBool = IntVar()
packPNGBool = IntVar()
soundsBool = IntVar()
languagesBool = IntVar()
compatibilityBool = IntVar()
zipBool = IntVar()

# Sets defualt value.
formatChoices = StringVar(root)
formatChoices.set(packFormats[5])

# Sets the info about the window.
root.title("Minecraft Asset Extractor")
root.iconphoto(False, PhotoImage(file = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), "pack.png")))
root.resizable(False, False)

# Creating and placing labels.
titleText = Label(root, text="Minecraft Asset Extractor\nBy: Ryan Garrett")
titleText.place(relx=0.5, rely=0.0, anchor="n")

creditButton = Button(root, text="Credits", command=creditUI)
creditButton.grid(row=0, column=0, sticky="NW")

outputLocationText = Label(root, text="Output Location:").grid(row=1, column=0, sticky="W")
outputLocation = Entry(root, width=50)
outputLocation.insert(0, os.path.normpath(os.path.expandvars(os.path.expanduser(r"~/Desktop/"))))
outputLocation.grid(row=2, column=0, sticky="W")
outputLocationButton = Button(root, text="Select Folder", command=openFolder)
outputLocationButton.grid(row=2, column=1)

packNameText = Label(root, text="Resource Pack Name:").grid(row=3, column=0, sticky="W")
packName = Entry(root, width=50)
packName.grid(row=4, column=0, sticky="W")

minecraftVersionText = Label(root, text="Minecraft Version (e.g. 1.16, 1.17):").grid(row=5, column=0, sticky="W")
minecraftVersion = Entry(root, width=50)
minecraftVersion.insert(0, "1.16")
minecraftVersion.grid(row=6, column=0, sticky="W")

minecraftVersionFullText = Label(root, text="Full Minecraft Version (e.g. 1.16.4, 20w51a):").grid(row=7, column=0, sticky="W")
minecraftVersionFull = Entry(root, width=50)
minecraftVersionFull.insert(0, "1.16.4")
minecraftVersionFull.grid(row=8, column=0, sticky="W")

packPNGSelectText = Label(root, text="Custom Pack Icon:").grid(row=9, column=0, sticky="W")
packPNGSelect = Entry(root, width=50, state="disabled")
packPNGSelect.grid(row=10, column=0, sticky="W")
packPNGSelectButton = Button(root, text="Select File", command=openFile, state="disabled")
packPNGSelectButton.grid(row=10, column=1)

descriptionText = Label(root, text="Description:").grid(row=11, column=0, sticky="W")
description = Entry(root, width=50)
description.grid(row=12, column=0, sticky="W")

packFormatText = Label(root, text="Pack Format:").grid(row=13, column=0, sticky="W")
packFormat = OptionMenu(root, formatChoices, *packFormats)
packFormat.configure(state="disabled")
packFormat.grid(row=14, column=0, sticky="W")

### Options
sounds = Checkbutton(root, variable=soundsBool).grid(row=3, column=2, sticky="E")
soundsText = Label(root, text="Sound Files").grid(row=3, column=3, sticky="W")

languages = Checkbutton(root, variable=languagesBool).grid(row=4, column=2, sticky="E")
languagesText = Label(root, text="Lang Files").grid(row=4, column=3, sticky="W")

compatibilityFixes = Checkbutton(root, variable=compatibilityBool)
compatibilityFixes.grid(row=5, column=2, sticky="E")
compatibilityFixes.select()
compatibilityFixesText = Label(root, text="Compatibility Fixes").grid(row=5, column=3, sticky="W")

packPNG = Checkbutton(root, command=packPNGButton, variable=packPNGBool)
packPNG.grid(row=6, column=2, sticky="E")
packPNGText = Label(root, text="Custom Pack Image").grid(row=6, column=3, sticky="W")

autoPack = Checkbutton(root, command=packFormatButton, variable=autoPackBool)
autoPack.grid(row=7, column=2, sticky="E")
autoPack.select()
autoPackText = Label(root, text="Auto Pack Format").grid(row=7, column=3, sticky="W")

zip = Checkbutton(root, variable=zipBool)
zip.grid(row=8, column=2, sticky="E")
zipText = Label(root, text="Zip Files").grid(row=8, column=3, sticky="W")

### Bottom
extractButton = Button(root, text="Extract", command=lambda:extract()).place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()
