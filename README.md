# Minecraft Asset Extractor
Rips all of the assets out of minecraft. This is a **heavly** modified version of [minecraft.gamepedia.com/Tutorials/Sound_directory](https://minecraft.gamepedia.com/Tutorials/Sound_directory).

This only works on windows 10. You can compile it for your OS. [How to Compile](#how-to-compile-the-program).

# How To Use
## Step 1
Unzip the file. (Right click the file -> Extract )
## Step 2
Open Minecraft_Asset_Extractor.exe
## Step 3
Select what type of version in the text box. (ex. 1.8.9)
## Step 4
Click Extract and wait! It may say that it will not respond because the command prompt is currently extracting the files.
## Step 5
Close the window, and enjoy your fully extracted resource pack!

(Note. This is a document. I will make a tutorial video soon.)
  
# How To Compile the Program
1. Make sure you have python installed. Install it here: [www.python.org/downloads/](https://www.python.org/downloads/)
2. Install pyinstaller through powershell:
```powershell
pip install pyinstaller
```
3. Right click on "Compile.ps1" in "Minecraft-Asset-Extractor/" and click on run with PowerShell
4. If asked to type y/n, type y.
5. If everything worked correctly then you should be able to launch "Minecraft-Asset-Extractor\dist\Minecraft_Asset_Extractor\Minecraft_Asset_Extractor.exe"

# Features That Need To Be Added
This is currently in aphal and still needs a lot of work to be done. Some of the things that I need to do before V1.0 are:
- ~~Tidy up the code.~~
  - ~~Add more comments to the code.~~
  - ~~Clean up varible names.~~
- Make sure that it is compatible with every MC version.
- Make sure that it is user friendly.
  - ~~GUI~~
  - ~~Intro Page~~
  - Tutorial Video
  - ~~Saving last used settings.~~
- ~~Pack into an .exe.~~
- Multithreading
- Settings
   - ~~Default output location.~~
   - Use last used settings.
   - Into page on start up.

# Extra Features
Extra things that I might want to add at some point:
- Dark mode.
- Full screen compatibility.
