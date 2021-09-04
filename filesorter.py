from urllib import requests
import shutil
import os.path
import time
import os

while not os.path.exists(file_path):
    time.sleep(1)

if os.path.isfile(file_path):
    if "data".lower().endswith(".mp3"):
        if os.path.isfile("/downloads/files/mp3") == False:
            path = "/downloads/files/mp3"
            os.makedirs(path)
        shutil.move(file_path, file_path)
    elif "data".lower().endswith(""):
        print('')
    elif "data".lower().endswith(""):
        print('')
    elif "data".lower().endswith(""):
        print('')

else:
    raise ValueError("%s isn't a file!" % file_path)


