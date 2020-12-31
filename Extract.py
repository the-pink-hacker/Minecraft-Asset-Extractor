import json, os, platform, shutil, sys
from zipfile import ZipFile
from pathlib import Path
import array as arr

# This is a heavly modified version of https://minecraft.gamepedia.com/Tutorials/Sound_directory.

# Change this if you want to put the sound files somewhere else
OUTPUT_PATH = os.path.normpath(os.path.expandvars(os.path.expanduser(r"~/Desktop/")))

def Extract():
	# 1.16 or 1.17
	MC_VERSION = input("Minecraft Version: ")
	# 1.16.4 or 20w51a
	MC_VERSION_FULL = input("Full Minecraft Version: ")
	# file-name RESOURCE_PACK_VERSION.zip this will be removed soon becuase it was for Vanilla Template creation.
	RESOURCE_PACK_VERSION = input("Resource Pack Version: ")
	# 6 = 1.16.4, 7 = 1.17
	MC_PACK = input("Pack Format: ")
	# Weather sounds will be extracted.
	SOUND = input("Sounds? ")
	# Weather sounds will be extracted.
	SOUND_BOOL = "False"

	if SOUND.lower() == "yes":
		SOUND = "s";
		SOUND_BOOL = "True"
	elif SOUND.lower() == "no":
		SOUND = "null";
		SOUND_BOOL = "False"
	else:
		SOUND = "null"
		SOUND_BOOL = "False"

	# Some of this code works on other operating systems, but I don't think of of it does.
	os.system("cls")
	if platform.system() == "Windows":
		MC_ASSETS = os.path.expandvars("%APPDATA%\\.minecraft\\assets")
		MC_VERSION_JAR = os.path.expandvars("%APPDATA%\\.minecraft\\versions\\" + MC_VERSION_FULL + "\\" + MC_VERSION_FULL + ".jar")
	else:
		MC_ASSETS = os.path.expanduser("~\\.minecraft\\assets")
		MC_VERSION_JAR = os.path.expanduser("~\\.minecraft\\versions\\" + MC_VERSION_FULL + "\\" + MC_VERSION_FULL + ".jar")

	print(f"OS: {platform.system()} \nMinecraft Version: {MC_VERSION} \nFull Minecraft Version: {MC_VERSION_FULL} \nPack Format: {MC_PACK} \nSounds: {SOUND_BOOL} \nMinecraft Version Location: {MC_VERSION_JAR}")

	CORRECT = input("Is the infomation correct? ")

	if CORRECT.lower() == "no":
		os.system("cls")
		Extract()

	# Compatibility fixes
	if int(MC_VERSION.split(".")[1]) == 13:
		MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/1.13.1.json"
	elif int(MC_VERSION.split(".")[1]) >= 8:
		MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_VERSION}.json"
	elif int(MC_VERSION.split(".")[1]) == 7:
		MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_VERSION_FULL}.json"
	else:
		MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/legacy.json"

	# Where the unextracted asset files are.
	MC_OBJECTS_PATH = f"{MC_ASSETS}/objects"
	# How it finds out weather it is an asset or somthing else.
	MC_SOUNDS = r"minecraft/"

	if SOUND_BOOL == "True":
		MC_VERSION_FULL = f"resource pack template {MC_VERSION_FULL} v{RESOURCE_PACK_VERSION} (sounds)"
	elif SOUND_BOOL == "False":
		MC_VERSION_FULL = f"resource pack template {MC_VERSION_FULL} v{RESOURCE_PACK_VERSION}"

	os.system("cls")

	# Opens the .jar
	with ZipFile(MC_VERSION_JAR, 'r') as zip:
		# Get a list of all archived file names from the zip
		listOfFileNames = zip.namelist()
	
		length = 0
		current = 0

		print("Extracting .rar")

		for fileName in listOfFileNames:
			if fileName.startswith("assets"):
				length += 1

		# Iterate over the file names
		for fileName in listOfFileNames:
			if fileName.startswith("assets"):
				current += 1
				print("Extracting .rar Progress: " + str(format(round(100 * (current / length), 2), '.2f')) + "%")
				zip.extract(fileName, OUTPUT_PATH + "\\" + MC_VERSION_FULL)

	if os.path.exists(os.path.normpath(f"{OUTPUT_PATH}/{MC_VERSION_FULL}\\assets\\.mcassetsroot")):
		os.remove(os.path.normpath(f"{OUTPUT_PATH}/{MC_VERSION_FULL}\\assets\\.mcassetsroot"))

	os.system("cls")

	# Handles files that are not in .jar
	with open(MC_OBJECT_INDEX, "r") as read_file:
		# Parse the JSON file into a dictionary
		data = json.load(read_file)

		# Find each line with MC_SOUNDS prefix, remove the prefix and keep the rest of the path and the hash
		sounds = {k[len(MC_SOUNDS):] : v["hash"] for (k,v) in data["objects"].items() if k.startswith(MC_SOUNDS)}

		length = 0
		current = 0

		if SOUND_BOOL == "True":
			print("Extracting Sounds And Languages")
		elif SOUND_BOOL == "False":
			print("Extracting Languages")

		for fpath, fhash in sounds.items():
			if fpath[0] == SOUND or fpath[0] == "t" or fpath[0] == "l":
				length += 1

		for fpath, fhash in sounds.items():
			if fpath[0] == SOUND or fpath[0] == "t" or fpath[0] == "l":
				current += 1
			
				if SOUND_BOOL == "True":
					print("Extracting Sounds And Languages Progress: " + str(format(round(100 * (current / length), 1), '.2f')) + "%")
				elif SOUND_BOOL == "False":
					print("Extracting Languages Progress: " + str(format(round(100 * (current / length), 1), '.2f')) + "%")

				# Ensure the paths are good to go for Windows with properly escaped backslashes in the string
				src_fpath = os.path.normpath(f"{MC_OBJECTS_PATH}/{fhash[:2]}/{fhash}")
				dest_fpath = os.path.normpath(f"{OUTPUT_PATH}/{MC_VERSION_FULL}/assets/minecraft/{fpath}")
				#print(fpath)
				# Make any directories needed to put the output file into as Python expects
				os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)

				# Copy the file
				shutil.copyfile(src_fpath, dest_fpath)

	PACK_PNG = os.path.join(os.path.abspath(os.path.join(__file__, os.pardir)), "pack.png")
	
	os.makedirs(os.path.dirname(f"{OUTPUT_PATH}\\{MC_VERSION_FULL}"), exist_ok=True)

	# Data to be written 
	dictionary ={
	"pack": {
		"pack_format": int(MC_PACK),
		"description": "put what ever you want here."
	}
}

	# Serializing json  
	json_object = json.dumps(dictionary, indent = 3)

	# Creates json file
	with open(f"{OUTPUT_PATH}\\{MC_VERSION_FULL}\\pack.mcmeta", "w") as outfile:
		outfile.write(json_object)

	shutil.copyfile(PACK_PNG, os.path.normpath(f"{OUTPUT_PATH}/{MC_VERSION_FULL}/pack.png"))

	input(f"Extracted All Assets To {OUTPUT_PATH}\\{MC_VERSION_FULL} ")

	# Adds The current pack to the array.
	resource_packs.append(os.path.normpath(f"{OUTPUT_PATH}\\{MC_VERSION_FULL}"))

	CONTINUE = input("Do you want extract another pack? ")

	if CONTINUE.lower() == "no":
		ZIP_FILES = input("Do you want to zip files? ")

		if ZIP_FILES.lower() == "no":
			input("Finished. ")
		else:
			os.system("cls")
			for pack in resource_packs:
					if pack != "":
						print(f"Ziping {pack}...")

						shutil.make_archive(os.path.normpath(f"{pack}"), 'zip', os.path.normpath(f"{pack}"))

						print("Zipped")

			DELETE = input("Do you want to delete files? ")
			os.system("cls")

			if DELETE.lower() == "yes":
				for pack in resource_packs:
					if pack != "":
						shutil.rmtree(pack)
						print(f"Deleted {pack}")
			input("Finished. ")
	else:
		os.system("cls")
		Extract()

# So it knows what packs you have extracted.
resource_packs = []

#Extract()
