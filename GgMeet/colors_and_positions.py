from time import sleep

import pyautogui as pt

while True:
    posXY = pt.position()
    print(posXY, pt.pixel(posXY[0], posXY[1]))
    sleep(1)
    #if posXY[0] == 0:
        #break
