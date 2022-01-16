# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import numpy as np

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def key_to_array():
    keys = key_check()
    out = np.zeros(2)
    if 'W' in keys:
        out[0] = 1
    elif 'S'in keys:
        out[0] = -1
    if 'A' in keys:
        out[1] = 1
    elif 'D'in keys:
        out[1] = -1
    
    return out