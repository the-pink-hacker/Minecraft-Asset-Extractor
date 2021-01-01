import os, Extract
from tkinter import *
from tkinter import filedialog

def extract():
	Extract.Extract()

def GUI():

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

	# Sets defualt value
	formatChoices = StringVar(root)
	formatChoices.set(packFormats[5])

	# Sets the icon and name of the window
	root.title("Minecraft Asset Extractor")
	root.iconphoto(False, PhotoImage(file = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), "pack.png")))

	#root.filename = filedialog.askdirectory(initialdir=os.path.normpath("c://"), title="test")

	# Creating and placing labels.
	titleText = Label(root, text="Minecraft Asset Extractor").grid(row=0, column=0)

	outputLocationText = Label(root, text="Output Location:").grid(row=1, column=0, sticky="W")
	outputLocation = Entry(root, width=50)
	outputLocation.insert(0, os.path.normpath(os.path.expandvars(os.path.expanduser(r"~/Desktop/"))))
	outputLocation.grid(row=2, column=0, sticky="W")

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

	packFormatText = Label(root, text="Pack Format:").grid(row=9, column=0, sticky="W")
	packFormat = OptionMenu(root, formatChoices, *packFormats)
	packFormat.grid(row=10, column=0, sticky="W")

	sounds = Checkbutton(root).grid(row=1, column=1)
	soundsText = Label(root, text="Sound Files").grid(row=1, column=2)

	languages = Checkbutton(root).grid(row=2, column=1)
	languagesText = Label(root, text="Lang Files").grid(row=2, column=2)

	compatibilityFixes = Checkbutton(root)
	compatibilityFixes.grid(row=3, column=1)
	compatibilityFixes.select()
	compatibilityFixesText = Label(root, text="Compatibility Fixes").grid(row=3, column=2)

	zip = Checkbutton(root)
	zip.grid(row=4, column=1)
	zip.select()
	zipText = Label(root, text="Zip Files").grid(row=4, column=2)

	extractButton = Button(root, text="Extract", command=extract).grid(row=11, column=0)

	root.mainloop()
