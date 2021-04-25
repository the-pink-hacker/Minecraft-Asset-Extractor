pyinstaller --icon=icon.ico Minecraft_Asset_Extractor.py, Extract.py
Copy-Item config.json -Destination dist\Minecraft_Asset_Extractor\config.json
Copy-Item icon.ico -Destination dist\Minecraft_Asset_Extractor\icon.ico
Copy-Item default_settings.ini -Destination dist\Minecraft_Asset_Extractor\default_settings.ini
Copy-Item LICENSE -Destination dist\Minecraft_Asset_Extractor\LICENSE.txt
Copy-Item README.md -Destination dist\Minecraft_Asset_Extractor\README.md
Invoke-Item dist\Minecraft_Asset_Extractor\
