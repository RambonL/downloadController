import keyboard
import win32clipboard as cb
import time
import re

regex = '(http)(.)*'

while True:
    if keyboard.is_pressed('strg+c'):
        time.sleep(1)
        cb.OpenClipboard()
        data = cb.GetClipboardData()
        cb.CloseClipboard()
        if(re.search(regex, data)):
            print(data)
            print('True')
        else:
            print(data)
            print('False')
        break
