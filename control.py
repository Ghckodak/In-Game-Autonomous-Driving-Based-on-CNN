from keras.models import load_model
from getkeys import *
from sendkeys import *
import time
import numpy as np
import tensorflow as tf
from grabscreen import *

model_name = 'E:\ETS2AD\model_5.h5'
model = load_model(model_name)

paused = False
pasued_time = 0

def check_status():
    global paused
    global pasued_time
    keys = key_check()
    if not paused:
        key_control()

        if 'Q' in keys:
            paused = True
            ReleaseKey(A),ReleaseKey(S),ReleaseKey(W),ReleaseKey(D)
            print("Holding...")
            pasued_time = time.time()
            time.sleep(0.5)
    
    else:
        if 'Q' in keys:
            paused = False
            print("Starting...")
            time.sleep(0.5)
        


def key_control():
    global model
    class_list = np.asarray([[0,1],[0,-1],[0,0],[1,1],[1,-1],[1,0],[-1,1],[-1,-1],[-1,0]])

    

    screen = grab_screen(region=(500,500,1200,800))
    screen = cv2.resize(screen, (350, 150))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = np.asarray(screen)
  
    pred = model.predict(screen.reshape(-1,150,350))
    index = np.argmax(pred)
    confidence = np.max(pred)
    command = class_list[index]

    

    print(str(command)+str(confidence))
    if command[0]==1:
        PressKey(W)
    elif command[0]==-1:
        PressKey(S)
    if command[1]==1:
        PressKey(A)
    elif command[1]==-1:
        PressKey(D)

    time.sleep(0.08)

    ReleaseKey(A),ReleaseKey(S),ReleaseKey(W),ReleaseKey(D)

if __name__ == '__main__':

    print("Press Q to start control")
    while(True):
        
        check_status()
        #time.sleep(0.1)