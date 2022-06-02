# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# PA0DEV                                                  #
# Automatic code updater                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import autoUpdater
# import machine

# define repository URL
REPO_URL = "https://github.com/PA0DEV/WordClock"

# initiate updater
updater = autoUpdater.Updater(REPO_URL)
# download update if possible
reqReboot = updater.downloadUpdate()

if reqReboot:
    # hard reset the board
    machine.reset()
else:
    # continue to main.py
    pass