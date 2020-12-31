import os, Extract
from tkinter import *
from tkinter import filedialog

def extract():
	Extract.Extract()

def GUI():
	root = Tk()

	# Sets the icon and name of the window
	root.title("Minecraft Asset Extractor")
	root.iconphoto(False, PhotoImage(file = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), "pack.png")))

	#root.filename = filedialog.askdirectory(initialdir=os.path.normpath("c://"), title="test")

	# Creating and placing labels.
	titleText = Label(root, text="Minecraft Asset Extractor").grid(row=0, column=0)

	outputLocationText = Label(root, text="Output Location:").grid(row=1, column=0)
	outputLocation = Entry(root, width=50)
	outputLocation.insert(0, os.path.normpath(os.path.expandvars(os.path.expanduser(r"~/Desktop/"))))
	outputLocation.grid(row=2, column=0)

	packNameText = Label(root, text="Resource Pack Name:").grid(row=3, column=0)
	packName = Entry(root, width=50)
	packName.grid(row=4, column=0)

	minecraftVersionText = Label(root, text="Minecraft Version (e.g. 1.16, 1.17):").grid(row=5, column=0)
	minecraftVersion = Entry(root, width=50)
	minecraftVersion.insert(0, "1.16")
	minecraftVersion.grid(row=6, column=0)

	minecraftVersionFullText = Label(root, text="Full Minecraft Version (e.g. 1.16.4, 20w51a):").grid(row=7, column=0)
	minecraftVersionFull = Entry(root, width=50)
	minecraftVersionFull.insert(0, "1.16.4")
	minecraftVersionFull.grid(row=8, column=0)

	sounds = Checkbutton(root).grid(row=9, column=0)
	soundsText = Label(root, text="Sound Files").grid(row=9, column=1)

	languages = Checkbutton(root).grid(row=9, column=2)
	languagesText = Label(root, text="Lang Files").grid(row=9, column=3)

	Extract = Button(root, text="Extract", command=extract).grid(row=10, column=0)

	root.mainloop()
