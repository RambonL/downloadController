import os
import shutil
import time
import clipboard

path = "D:/Downloads/"


def getNewFile(filename):
    tmpArray = filename.split('.')
    i = len(tmpArray) - 1
    print(tmpArray[i])

    moveFile(filename, tmpArray[i])

def moveFile(filename, extention):
    if not os.path.isdir(path + extention):
        os.mkdir(path + extention)
        time.sleep(1)
        shutil.move(path + filename, path + extention)
        clipboard.startProgramm()
    else:
        shutil.move(path + filename, path + extention)
        clipboard.startProgramm()
