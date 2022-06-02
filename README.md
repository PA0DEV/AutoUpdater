# AutoUpdater
Library to automaticly update code from a github Repository

Takes the source code from a given GitHub Repository and 

## How to use:

### !! Important !!

Before uploading the Repository to GutHub execute the library once to fetch all existing files in files.json:

```json
{
    "libs": [],
    "main": [
        ".gitattributes",
        "autoUpdater.py",
        "files.json",
        "info.json",
        "LICENSE",
        "main.py",
        "README.md"
    ],
    "settings": []
}
```

### implement the updater in your code:

```py
import autoUpdater
```
Import the library.

```py
REPO_URL = "https://github.com/PA0DEV/WordClock"
```
define the URL of the GitHub repository for your project

```py
updater = autoUpdater.Updater(REPO_URL)
```
initiate the updater

```py
reqReboot = updater.downloadUpdate()

if reqReboot:
    # hard reset the board
    machine.reset()
else:
    # continue to main.py
    pass
```
check for updates and download the code if remote version is newer than the local one. After downloading reset the board to run the new version.

---

## Requirements

- Your project repository has to be public in GitHub
- Your file structure is as following:

```
/main
│   file1.md
│   main.py
|   files.json
|   ...  
│
└───/libs
│   │   libExample.py
│   │   otherLib.py
│   |   ...
│   
└───/settings
    │   settings.json
    │   ...
```
- You have to create the files.json file before uploading to GitHub


