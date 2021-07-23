pyinstaller --onefile --noupx --icon=icon.ico Minecraft_Asset_Extractor.py, Extract.py
Copy-Item config.json -Destination dist\config.json
Copy-Item icon.ico -Destination dist\icon.ico
Copy-Item default_settings.ini -Destination dist\default_settings.ini
Copy-Item LICENSE -Destination dist\LICENSE.txt
Copy-Item README.md -Destination dist\README.md
