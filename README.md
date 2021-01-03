# Minecraft Asset Extractor
Rips all of the assets out of minecraft. This is a **heavly** modified version of [minecraft.gamepedia.com/Tutorials/Sound_directory](https://minecraft.gamepedia.com/Tutorials/Sound_directory).

## How To Use
### Downloading and Installing
1. Make sure you have python installed. Install it here: [www.python.org/downloads/](https://www.python.org/downloads/)
2. Download [latest version](https://github.com/RyanGar46/Minecraft-Asset-Extractor/releases).
3. Unzip the downloaded .zip file.

### Using the Program
1. Launch "Minecraft_Asset_Extractor.py"
2. Two windows should open: the command line, and the program. If you don't see one of these then make sure it is not minimized.
3. Fill in the following fields.
   - Output location: Where the final resource pack will be placed (Defaults to desktop).
   - Resource Pack Name: The name of the final resource pack.
   - Minecraft Version: number.number (e.g 1.16, 1.17).
   - Full Minecraft Version: number.number.number or snapshot (e.g. 1.16.4, 20w51a).
   - Custom Pack Icon: The image you will see in the resource pack selection screen (Optional).
   - Description: The text you will see in the resource pack selection screen.
   - Pack Format: The resource pack version (Automaticaly determined if "Auto Pack" is on).
   - Sound Files: Weather sound files are extracted or not.
   - Lang Files: Weather language files are extracted or not.
   - Compatibility Fixes: Adds edge cases for specific minecratf versions (Would suggest that you keep this on).
   - Is a Snapshot: Won't work until V0.3.0 - Alpha
   - Custom Pack Image: Enables and disables weather you want a custom image for you resource pack.
   - Auto Pack Format: Automaticaly determines the pack format. (If on, it disables "Pack Format")
   - Zip Files: Zips the resource pack after extracting.
   - Clear Command Line: Clears the command line at certian points in the extraction.
  4. Hit extract.
  5. You resource pack should have been created at the output location.

## Features That Need To Be Added
This is currently in aphal and still needs a lot of work to be done. Some of the things that I need to do before V1.0 are:
- ~~Tidy up the code.~~
  - ~~Add more comments to the code.~~
  - ~~Clean up varible names.~~
- Make sure that it is compatible with every MC version.
- OS compatibility
  - ~~Windows (Only OS I have access to)~~
  - Linux
  - Mac
- Make sure that it is user friendly.
  - ~~GUI~~
  - Intro Page
  - Tutorial Video
  - Saving last used settings.
- Pack into an .exe.
- Multithreading
- Settings
   - Default output location.
      - Desktop
      - Resource Pack Folder
      - Custom
   - Use last used settings.
   - Into page on start up.

## Extra Features
Extra things that I want to add at some point:
- Dark mode.
- Full screen compatibility.
