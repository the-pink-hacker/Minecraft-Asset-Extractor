import json, os, platform, shutil, sys
from zipfile import ZipFile
from pathlib import Path
import array as arr

# This is a heavly modified version of https://minecraft.gamepedia.com/Tutorials/Sound_directory.

def Extract(OUTPUT_PATH, PACK_NAME, MC_VERSION, MC_VERSION_FULL, PACK_PNG, MC_PACK, AUTO_PACK, SOUNDS, LANGBOOL, ZIP_FILES, COMPATIBILITY):
	if AUTO_PACK == True:
		print("Auto Pack")

	if SOUNDS == True:
		SOUND = "s";
	else:
		SOUND = "null"

	if LANGBOOL == True:
		LANG = "l";
	else:
		LANG = "null"

	# Some of this code works on other operating systems, but I don't think all of it does.
	os.system("cls")
	if platform.system() == "Windows":
		MC_ASSETS = os.path.expandvars("%APPDATA%\\.minecraft\\assets")
		MC_VERSION_JAR = os.path.expandvars("%APPDATA%\\.minecraft\\versions\\" + MC_VERSION_FULL + "\\" + MC_VERSION_FULL + ".jar")
	else:
		MC_ASSETS = os.path.expanduser("~\\.minecraft\\assets")
		MC_VERSION_JAR = os.path.expanduser("~\\.minecraft\\versions\\" + MC_VERSION_FULL + "\\" + MC_VERSION_FULL + ".jar")

	# Compatibility fixes
	if COMPATIBILITY == True:
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

	if SOUNDS == "True":
		MC_VERSION_FULL = f"resource pack template {MC_VERSION_FULL} (sounds)"
	elif SOUNDS == "False":
		MC_VERSION_FULL = f"resource pack template {MC_VERSION_FULL}"

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

		if SOUNDS == "True":
			print("Extracting Sounds And Languages")
		elif SOUNDS == "False":
			print("Extracting Languages")

		for fpath, fhash in sounds.items():
			if fpath[0] == SOUND or fpath[0] == "t" or fpath[0] == LANG:
				length += 1

		for fpath, fhash in sounds.items():
			if fpath[0] == SOUND or fpath[0] == "t" or fpath[0] == LANG:
				current += 1
			
				if SOUNDS == "True":
					print("Extracting Sounds And Languages Progress: " + str(format(round(100 * (current / length), 1), '.2f')) + "%")
				elif SOUNDS == "False":
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

	print(f"Extracted All Assets To {OUTPUT_PATH}\\{MC_VERSION_FULL} ")

	if ZIP_FILES == False:
		input("Finished. ")
	else:
		os.system("cls")

		print(f"Ziping {OUTPUT_PATH}\{MC_VERSION_FULL}...")

		shutil.make_archive(os.path.normpath(f"{OUTPUT_PATH}/{MC_VERSION_FULL}"), 'zip', os.path.normpath(f"{OUTPUT_PATH}/{MC_VERSION_FULL}"))

		print("Zipped {OUTPUT_PATH}\{MC_VERSION_FULL}.")

		os.system("cls")

		shutil.rmtree(os.path.normpath(f"{OUTPUT_PATH}/{MC_VERSION_FULL}"))

		input("Finished. ")
