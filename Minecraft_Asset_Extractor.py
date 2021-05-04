import os, webbrowser, json
from Extract import AutoPack
from time import sleep
from threading import Thread
from configparser import *
from Extract import *
from tkinter import *
from tkinter import filedialog
from datetime import datetime

# Parses data from config.json
configFile = open("config.json")
configVaribles = json.load(configFile)
configFile.close()

packFormats = configVaribles["pack_format"]
snapshotLetters = configVaribles["snapshot_letters"]

desktopDir = os.path.normpath(os.path.expandvars(os.path.expanduser(r"~/Desktop/")))

class Settings:
	"""A class that stores all settings."""

	# Fields
	output_location = ""
	name = ""
	version = ""
	snapshot_year = 0
	snapshot_week = 0
	snapshot_letter = snapshotLetters[0]
	pngDir = ""
	description = ""
	pack_format = 0

	# Check Boxes
	snapshot = False
	png = False
	auto_pack = False
	sounds = False
	shaders = False
	languages = False
	realm = False
	zip = False
	compatibility = False
	clear = False
	delete = False

	# Settings
	default_output_location = ""
	intro_screen = False
	tempDir = "temp"
	debugSettings = False
	saveTimer = 1

	def __str__(self):
		return f"""Fields
Output Location: {self.output_location}\nName: {self.name}\nVersion: {self.version}\nSnapshot: {f"{self.snapshot_year}w{self.snapshot_week}{self.snapshot_letter}"}
PNG Location: {self.pngDir}\nDescription: {self.description}\nPack Format {self.pack_format}

Check Boxes
Snapshot: {self.snapshot}\nPNG: {self.png}\nAuto Pack: {self.auto_pack}\nSounds: {self.sounds}\nShaders: {self.shaders}\nLanguages: {self.languages}\nRealm: {self.realm}\nZip: {self.zip}
Compatibility: {self.compatibility}\nClear: {self.clear}\nDelete: {self.delete}

Settings
Default Output Location: {self.default_output_location}\nIntro Screen: {self.intro_screen}\nTemp Dir: {self.tempDir}\nDebug Settings: {self.debugSettings}\nSave Timer: {self.saveTimer} Second(s)"""

	# Updates all of the settings
	def update(self):
		# Fields
		self.output_location = outputLocationVar.get()
		self.name = packNameVar.get()
		self.version = minecraftVersionVar.get()
		self.snapshot_year = snapshotYearVar.get()
		self.snapshot_week = snapshotWeekVar.get()
		self.snapshot_letter = snapshotLetterSelection.get()
		self.pngDir = packPNGSelectVar.get()
		self.description = descriptionVar.get()
		self.pack_format = int(formatChoices.get())

		# Check Boxes
		self.snapshot = bool(snapshotsBool)
		self.png = bool(packPNGBool.get())
		self.auto_pack = bool(autoPackBool.get())
		self.sounds = bool(soundsBool.get())
		self.shaders = bool(shadersBool.get())
		self.languages = bool(languagesBool.get())
		self.realm = bool(realmBool.get())
		self.zip = bool(zipBool.get())
		self.compatibility = bool(compatibilityBool.get())
		self.clear = bool(clearBool.get())
		self.delete = bool(deleteBool.get())

		self.save()

	def save(self):
		# Saves the last used settings
		write_config = ConfigParser()

		# The fields on the left
		write_config.add_section("Fields")
		if outputLocation.get() != self.default_output_location:
			write_config.set("Fields","output_location", self.output_location)
		else:
			write_config.set("Fields","output_location", "")
		write_config.set("Fields","name", self.name)
		write_config.set("Fields","version", self.version)
		write_config.set("Fields","png", self.pngDir)
		write_config.set("Fields","description", self.description)
		write_config.set("Fields","pack_format", str(self.pack_format))

		# The options on the right
		write_config.add_section("CheckBoxes")
		write_config.set("CheckBoxes","snapshot", str(self.snapshot))
		write_config.set("CheckBoxes","png", str(self.png))
		write_config.set("CheckBoxes","auto_pack", str(self.auto_pack))
		write_config.set("CheckBoxes","sounds", str(self.sounds))
		write_config.set("CheckBoxes","shaders", str(self.shaders))
		write_config.set("CheckBoxes","languages", str(self.languages))
		write_config.set("CheckBoxes","realm", str(self.realm))
		write_config.set("CheckBoxes","zip", str(self.zip))
		write_config.set("CheckBoxes","compatibility", str(self.compatibility))
		write_config.set("CheckBoxes","clear", str(self.clear))
		write_config.set("CheckBoxes","delete", str(self.delete))

		# Extra settings
		write_config.add_section("Settings")
		if self.default_output_location != desktopDir:
			write_config.set("Settings","default_output_location", self.default_output_location)
		else:
			write_config.set("Settings","default_output_location", "")
		#write_config.set("Settings","intro_screen", self.intro_screen)
		write_config.set("Settings","intro_screen", "False")
		write_config.set("Settings", "temp_dir", self.tempDir)

		cfgfile = open("settings.ini",'w')
		write_config.write(cfgfile)
		cfgfile.close()

	def load(self):
		read_config = ConfigParser()

		if os.path.exists("settings.ini"):
			read_config.read("settings.ini")
		else:
			read_config.read("default_settings.ini")

		# The options on the right
		if read_config.get("CheckBoxes", "snapshot") == "True":
			self.snapshot = True
			snapshots.select()
		else:
			self.snapshot = False
			snapshots.deselect()

		if read_config.get("CheckBoxes", "png") == "True":
			self.png = True
			packPNG.select()
		else:
			self.png = False
			packPNG.deselect()

		if read_config.get("CheckBoxes", "auto_pack") == "True":
			self.auto_pack = True
			autoPack.select()
		else:
			self.auto_pack = False
			autoPack.deselect()

		if read_config.get("CheckBoxes", "sounds") == "True":
			self.sounds = True
			sounds.select()
		else:
			self.sounds = False
			sounds.deselect()

		if read_config.get("CheckBoxes", "shaders") == "True":
			self.shaders = True
			shaders.select()
		else:
			self.shaders = False
			shaders.deselect()

		if read_config.get("CheckBoxes", "languages") == "True":
			self.languages = True
			languages.select()
		else:
			self.languages = False
			languages.deselect()

		if read_config.get("CheckBoxes", "realm") == "True":
			self.realm = True
			realm.select()
		else:
			self.realm = False
			realm.deselect()

		if read_config.get("CheckBoxes", "compatibility") == "True":
			self.compatibility = True
			compatibilityFixes.select()
		else:
			self.compatibility = False
			compatibilityFixes.deselect()

		if read_config.get("CheckBoxes", "clear") == "True":
			self.clear = True
			clear.select()
		else:
			self.clear = False
			delete.deselect()

		if read_config.get("CheckBoxes", "zip") == "True":
			self.zip = True
			zip.select()
		else:
			self.zip = False
			zip.deselect()

		if read_config.get("CheckBoxes", "delete") == "True":
			self.delete = True
			delete.select()
		else:
			self.delete = False
			delete.deselect()
		zipButton()

		# The fields on the left.
		outputLocation.delete(0, END)
		outputLocationField = read_config.get("Fields", "output_location")
		if outputLocationField.replace(" ", "") == "":
			outputLocation.insert(0, desktopDir)
			self.output_location = desktopDir
		else:
			outputLocation.insert(0, outputLocationField)
			self.output_location = outputLocationField
		packName.delete(0, END)
		packName.insert(0, read_config.get("Fields", "name"))
		self.name = read_config.get("Fields", "name")
		minecraftVersion.delete(0, END)
		minecraftVersion.insert(0, read_config.get("Fields", "version"))
		self.version = read_config.get("Fields", "version")
		snapshotButton()
		packPNGSelect.delete(0, END)
		packPNGSelect.insert(0, read_config.get("Fields", "png"))
		self.pngDir = read_config.get("Fields", "png")
		packPNGButton()
		description.delete(0, END)
		description.insert(0, read_config.get("Fields", "description"))
		self.description = read_config.get("Fields", "description")
		formatChoices.set(packFormats[packFormats.index(read_config.get("Fields", "pack_format"))])
		self.pack_format = int(read_config.get("Fields", "pack_format"))
		packFormatButton()

		# Settings
		if read_config.get("Settings", "default_output_location").replace(" ", "") == "":
			settingsDefaultOutputLocation = desktopDir
			self.default_output_location = desktopDir
		else:
			outputLocation.delete(0, END)
			outputLocation.insert(0, read_config.get("Settings", "default_output_location"))
			self.default_output_location = read_config.get("Settings", "default_output_location")

		if read_config.get("Settings", "intro_screen") == "True":
			self.intro_screen = read_config.get("Settings", "intro_screen")
			introUI()
		self.tempDir = read_config.get("Settings", "temp_dir")

options = Settings()

def getTime():
	time = str(datetime.now())
	time = time.replace("-", " ")
	time = time.replace(":", " ")
	time = time.replace(".", " ")
	time = time.split(" ")
	return time

def parseNestedArray(array):
	array = str(array)
	array = array.replace("{", "")
	array = array.replace("}", "")
	array = array.replace("'", "")
	array = array.replace(" ", "")
	array = array.split(",")

	for index in range(len(array)):
		array[index] = array[index].split(":")
	return array

programTitle = configVaribles["program_info"]["title"]
author = configVaribles["program_info"]["author"]
programVersion = configVaribles["program_info"]["version"]

class RowHandeler:
	"""Helps automate the placement of lables."""
	def __init__(self, startingRow):
		self.currentRow = startingRow - 1

	def GetRow(self, keepRow = False):
		if keepRow == False:
			self.currentRow += 1

		return self.currentRow

def convertToRGB(r, g, b):
	"""Translates rgb to a tkinter friendly color code."""
	return f"#{r:02x}{g:02x}{b:02x}"

# When mouse is hovering over button
def onEnter(e):
	if e.widget["state"] == NORMAL:
		e.widget["background"] = convertToRGB(220, 220, 220)

# When mouse leaves button
def onLeave(e):
    e.widget["background"] = "SystemButtonFace"

def extract():
	ExtractStart(
	os.path.normpath(outputLocation.get()), # Output Location
	packName.get(), # Pack Name
	minecraftVersion.get(), # Minecraft Version
	f"{snapshotYear.get()}w{snapshotWeek.get()}{snapshotLetterSelection.get()}", # Snapshot
	bool(snapshotsBool.get()), # Snapshot bool
	packPNGSelect.get(), # pack.png
	bool(packPNGBool.get()), # Custom pack.png
	description.get(), # Description
	formatChoices.get(), # Pack Format
	bool(autoPackBool.get()), # Auto Pack Format
	bool(soundsBool.get()), # Sounds
	bool(shadersBool.get()), # Shaders
	bool(languagesBool.get()), # LANG
	bool(realmBool.get()), # Realm Files
	bool(zipBool.get()), # Zip
	bool(compatibilityBool.get()), # Compatibility
	bool(clearBool.get()), # Clear command line
	bool(deleteBool.get())) # Delets folder after zipping

def openFolder(parent, entry, initialdir = "C://"):
	folder = filedialog.askdirectory(parent=parent,initialdir=os.path.abspath(os.path.normpath(initialdir)), title="Select Output Location")
	
	if folder != "":
		entry.delete(0, END)
		entry.insert(0, folder)

def openFile():
	folder = filedialog.askopenfilename(initialdir=os.path.normpath("C://"), title="Select File", filetypes =(("PNG", "*.png"),("All Files","*.*")))

	if folder != "":
		packPNGSelect.delete(0, END)
		packPNGSelect.insert(0, folder)

def zipButton():
	if zipBool.get():
		delete.configure(state="normal")
	if not zipBool.get():
		delete.configure(state="disabled")

def snapshotButton():
	if snapshotsBool.get():
		snapshotLetter.configure(state="normal")
		snapshotWeek.configure(state="normal")
		snapshotYear.configure(state="normal")
	elif not snapshotsBool.get():
		snapshotLetter.configure(state="disabled")
		snapshotWeek.configure(state="disabled")
		snapshotYear.configure(state="disabled")

def packFormatButton():
	if not autoPackBool.get():
		packFormat.configure(state="active")
	elif autoPackBool.get():
		packFormat.configure(state="disabled")

def packPNGButton():
	if packPNGBool.get():
		packPNGSelect.configure(state="normal")
		packPNGSelectButton.configure(state="normal")
	elif not packPNGBool.get():
		packPNGSelect.configure(state="disabled")
		packPNGSelectButton.configure(state="disabled")

def callback(url):
    webbrowser.open_new(url)

def closeWindow(window):
	window.destroy()
	root.focus_force()

def generateLink(window, link, text, GetRow):

	url = parseNestedArray(link)

	# Creates lable
	linkText = Label(window, text=text, fg="blue", cursor="hand2", font=('Arial',9,'underline'))
	linkText.bind("<Button-1>", lambda e: callback(url))

	return linkText

def introUI():
	intro = Toplevel(root)

	intro.focus_force()
	intro.title("Introduction Screen")
	intro.iconbitmap(windowIcon)
	intro.geometry("400x300")
	intro.resizable(False, False)

	settingsTitleText = Label(intro, text=f"{programTitle}\nBy: {author}")
	settingsTitleText.place(relx=0.5, rely=0.0, anchor="n")

	GetRow = RowHandeler(0).GetRow

	spacer = Label(intro, text="", pady=10).grid(row=GetRow(), column=0, sticky="NW")

	generateLink(intro, configVaribles["links"]["Source Code"], "Github Page", GetRow).place(relx=0.5, rely=0.5, anchor="center")

	introVersion = Label(intro, text=programVersion)
	introVersion.place(relx=0.0, rely=1.0, anchor="sw")

	closeButton = Button(intro, text="Close", command=lambda:closeWindow(intro), relief="flat")
	closeButton.place(relx=1.0, rely=1.0, anchor="se")
	closeButton.bind("<Enter>", onEnter)
	closeButton.bind("<Leave>", onLeave)

def closeSettings(window, settings, options):
	settings.default_output_location = options[0]
	settings.tempDir = options[1]
	closeWindow(window)

def settingsUI(settings):
	setting = Toplevel(root)

	setting.focus_force()
	setting.title("Settings")
	setting.iconbitmap(windowIcon)
	setting.geometry("400x300")
	setting.resizable(False, False)

	settingsTitleText = Label(setting, text=f"{programTitle}\nBy: {author}")
	settingsTitleText.place(relx=0.5, rely=0.0, anchor="n")

	GetRow = RowHandeler(0).GetRow

	spacer = Label(setting, text="", pady=10).grid(row=GetRow(), column=0, sticky="NW")

	outputLocationText = Label(setting, text="Default Output Location:").grid(row=GetRow(), column=0, sticky="W")
	defaultOutputLocation = Entry(setting, width=50)
	defaultOutputLocation.insert(0, settings.default_output_location)
	defaultOutputLocation.grid(row=GetRow(), column=0, sticky="W")
	outputLocationButton = Button(setting, text="Select Folder", command=lambda:openFolder(setting, defaultOutputLocation, settings.default_output_location), relief="flat")
	outputLocationButton.grid(row=GetRow(True), column=1)
	outputLocationButton.bind("<Enter>", onEnter)
	outputLocationButton.bind("<Leave>", onLeave)

	tempDirText = Label(setting, text="Temp Directory:").grid(row=GetRow(), column=0, sticky="W")
	tempDir = Entry(setting, width=50)
	tempDir.insert(0, os.path.abspath(settings.tempDir))
	tempDir.grid(row=GetRow(), column=0, sticky="W")
	tempDirButton = Button(setting, text="Select Folder", command=lambda:openFolder(setting, tempDir, settings.tempDir), relief="flat")
	tempDirButton.grid(row=GetRow(True), column=1)
	tempDirButton.bind("<Enter>", onEnter)
	tempDirButton.bind("<Leave>", onLeave)

	settingsVersion = Label(setting, text=programVersion)
	settingsVersion.place(relx=0.0, rely=1.0, anchor="sw")

	closeButton = Button(setting, text="Close", command=lambda:closeSettings(setting, settings, [defaultOutputLocation.get(), tempDir.get()]), relief="flat")
	closeButton.place(relx=1.0, rely=1.0, anchor="se")
	closeButton.bind("<Enter>", onEnter)
	closeButton.bind("<Leave>", onLeave)

def generateLinks(window, links, GetRow):
	'''Takes an array of links and converts them into lables
	'''
	links = parseNestedArray(links)

	for index in range(len(links)):
		name = links[index][0]
		url = links[index][1]

		# Creates lable
		linkText = Label(window, text=name, fg="blue", cursor="hand2", font=('Arial',9,'underline'))
		linkText.grid(row=GetRow(), column=0, sticky="W")
		linkText.bind("<Button-1>", lambda e: callback(url))

def aboutUI():
	about = Toplevel(root)

	about.focus_force()
	about.title("Credit")
	about.iconbitmap(windowIcon)
	about.geometry("400x300")
	about.resizable(False, False)

	aboutTitleText = Label(about, text=f"{programTitle}\nBy: {author}")
	aboutTitleText.place(relx=0.5, rely=0.0, anchor="n")

	GetRow = RowHandeler(0).GetRow

	spacer = Label(about, text="", pady=10).grid(row=GetRow(), column=0, sticky="N")

	aboutText = Label(about, text=f"{author} (RyanGar46):")
	aboutText.grid(row=GetRow(), column=0, sticky="W")

	generateLinks(about, configVaribles["links"], GetRow)

	version = Label(about, text=programVersion)
	version.place(relx=0.0, rely=1.0, anchor="sw")

	closeButton = Button(about, text="Close", command=lambda:closeWindow(about), relief="flat")
	closeButton.place(relx=1.0, rely=1.0, anchor="se")
	closeButton.bind("<Enter>", onEnter)
	closeButton.bind("<Leave>", onLeave)

	about.mainloop()

def on_closing(settings):
	options.save()
	root.destroy()

root = Tk()

# Sets up settings
# region
def versionCheck(var, indx, mode):
	if AutoPack(options.version) >= 5:
		shaders.configure(state="normal")
	else:
		shaders.configure(state="disabled")

minecraftVersionVar = StringVar()
minecraftVersionVar.trace_add("write", versionCheck)
outputLocationVar = StringVar()
packNameVar = StringVar()
snapshotYearVar = StringVar()
snapshotWeekVar = StringVar()
snapshotLetterSelection = StringVar(root)
snapshotLetterSelection.set(snapshotLetters[0])
packPNGSelectVar = StringVar()
descriptionVar = StringVar()
formatChoices = StringVar(root)
formatChoices.set(packFormats[5])

autoPackBool = IntVar()
packPNGBool = IntVar()
soundsBool = IntVar()
languagesBool = IntVar()
realmBool = IntVar()
snapshotsBool = IntVar()
compatibilityBool = IntVar()
zipBool = IntVar()
clearBool = IntVar()
deleteBool = IntVar()
shadersBool = IntVar()
#endregion

# Sets the info about the window
root.focus_force()
windowIcon = configVaribles["program_info"]["icon"]
root.title(programTitle)
root.iconbitmap(windowIcon)
root.minsize(550, 375)

### Feilds
# region
GetRow = RowHandeler(0).GetRow

titleText = Label(root, text=f"{programTitle}\nBy: {author}")
titleText.place(relx=0.5, rely=0.0, anchor="n")

settings = Button(root, text="Settings", command=lambda: settingsUI(options), relief="flat")
settings.grid(row=GetRow(), column=0, sticky=NW)
settings.bind("<Enter>", onEnter)
settings.bind("<Leave>", onLeave)

aboutButton = Button(root, text="About", command=aboutUI, relief="flat")
aboutButton.place(x=50, y=0, anchor=NW)
aboutButton.bind("<Enter>", onEnter)
aboutButton.bind("<Leave>", onLeave)

introButton = Button(root, text="Intro Screen", command=introUI, relief="flat")
introButton.place(x=91, y=0, anchor=NW)
introButton.bind("<Enter>", onEnter)
introButton.bind("<Leave>", onLeave)

outputLocationText = Label(root, text="Output Location:").grid(row=GetRow(), column=0, sticky="W")
outputLocation = Entry(root, width=50, textvariable=outputLocationVar)
outputLocation.insert(0, desktopDir)
outputLocation.grid(row=GetRow(), column=0, sticky="W")
outputLocationButton = Button(root, text="Select Folder", command=lambda:openFolder(root, outputLocation), relief="flat")
outputLocationButton.grid(row=GetRow(True), column=1)
outputLocationButton.bind("<Enter>", onEnter)
outputLocationButton.bind("<Leave>", onLeave)

packNameText = Label(root, text="Resource Pack Name:").grid(row=GetRow(), column=0, sticky="W")
packName = Entry(root, width=50, textvariable=packNameVar)
packName.grid(row=GetRow(), column=0, sticky="W")

minecraftVersionText = Label(root, text="Minecraft Version (e.g. 1.16.4, 1.17):").grid(row=GetRow(), column=0, sticky="W")
minecraftVersion = Entry(root, width=50, textvariable=minecraftVersionVar)
minecraftVersion.grid(row=GetRow(), column=0, sticky="W")

snapshotText = Label(root, text="Snapshot Version:").grid(row=GetRow(), column=0, sticky="W")

snapshotYearText = Label(root, text="Year:").place(x=0, y=205, anchor=W)
snapshotYear = Entry(root, width=2, textvariable=snapshotYearVar)
snapshotYear.insert(0, str(datetime.today().year)[-2:])
snapshotYear.place(x=40, y=205, anchor=W)

snapshotWeekText = Label(root, text="Week:").place(x=60, y=205, anchor=W)
snapshotWeek = Entry(root, width=2, textvariable=snapshotWeekVar)
snapshotWeek.insert(0, str(datetime.today().isocalendar()[1]))
snapshotWeek.place(x=105, y=205, anchor=W)

snapshotLetterText = Label(root, text="Letter:").place(x=125, y=205, anchor=W)
snapshotLetter = OptionMenu(root, snapshotLetterSelection, *snapshotLetters)
snapshotLetter.place(x=165, y=205, anchor=W)

GetRow()

packPNGSelectText = Label(root, text="Custom Pack Icon:").grid(row=GetRow(), column=0, sticky="W")
packPNGSelect = Entry(root, width=50, textvariable=packPNGSelectVar)
packPNGSelect.grid(row=GetRow(), column=0, sticky="W")
packPNGSelectButton = Button(root, text="Select File", command=openFile, state="disabled", relief="flat")
packPNGSelectButton.grid(row=GetRow(True), column=1)
packPNGSelectButton.bind("<Enter>", onEnter)
packPNGSelectButton.bind("<Leave>", onLeave)

descriptionText = Label(root, text="Description:").grid(row=GetRow(), column=0, sticky="W")
description = Entry(root, width=50, textvariable=descriptionVar)
description.grid(row=GetRow(), column=0, sticky="W")

packFormatText = Label(root, text="Pack Format:").grid(row=GetRow(), column=0, sticky="W")
packFormat = OptionMenu(root, formatChoices, *packFormats)
packFormat.grid(row=GetRow(), column=0, sticky="W")
# endregion

### Options
# region
GetRow = RowHandeler(2).GetRow

sounds = Checkbutton(root, variable=soundsBool, text="Sound Files")
sounds.grid(row=GetRow(), column=2, sticky="W")

shaders = Checkbutton(root, variable=shadersBool, text="Shader Files")
shaders.grid(row=GetRow(), column=2, sticky="W")

languages = Checkbutton(root, variable=languagesBool, text="Lang Files")
languages.grid(row=GetRow(), column=2, sticky="W")

realm = Checkbutton(root, variable=realmBool, text="Realm Files")
realm.grid(row=GetRow(), column=2, sticky="W")

compatibilityFixes = Checkbutton(root, variable=compatibilityBool, text="Compatibility Fixes")
compatibilityFixes.grid(row=GetRow(), column=2, sticky="W")

snapshots = Checkbutton(root, command=snapshotButton, variable=snapshotsBool, text="Is a Snapshot")
snapshots.grid(row=GetRow(), column=2, sticky="W")

packPNG = Checkbutton(root, command=packPNGButton, variable=packPNGBool, text="Custom Pack Image")
packPNG.grid(row=GetRow(), column=2, sticky="W")

autoPack = Checkbutton(root, command=packFormatButton, variable=autoPackBool, text="Auto Pack Format")
autoPack.grid(row=GetRow(), column=2, sticky="W")

zip = Checkbutton(root, command=zipButton, variable=zipBool, text="Zip Files")
zip.grid(row=GetRow(), column=2, sticky="W")

delete = Checkbutton(root, variable=deleteBool, text="Delete Folder After Zip")
delete.grid(row=GetRow(), column=2, sticky="W")

clear = Checkbutton(root, variable=clearBool, text="Clear Command Line")
clear.grid(row=GetRow(), column=2, sticky="W")
# endregion Options

### Bottom
# region
extractButton = Button(root, text="Extract", command=lambda:[extract(), saveSettings(options)], relief="flat")
extractButton.place(relx=1.0, rely=1.0, anchor="se")
extractButton.bind("<Enter>", onEnter)
extractButton.bind("<Leave>", onLeave)
# endregion

options.load()

root.protocol("WM_DELETE_WINDOW", lambda: on_closing(options))

def clock(args):
	while True:
		sleep(options.saveTimer)
		try:
			options.update()
			if options.debugSettings:
				os.system("cls")
				print(options)
		except:
			None

clockthread = Thread(target = clock, args = (1,))
clockthread.start()

root.mainloop()

sys.exit(0)
