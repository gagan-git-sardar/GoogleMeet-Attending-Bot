import pyautogui as pt
from time import sleep
from PIL import Image
import pyperclip
import random

sleep(1)


def get_message():
    # global x, y

    # print("line 50")
    # position_window = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\WindowsLogo.png", confidence=.3)
    # t = position_window[0]
    # u = position_window[1]
    # print(t, u)
    t = 0
    u = 0
    pt.moveTo(t + 33, u + 16, duration=.4)
    pt.click()
    sleep(1)
    # position_whatsapp = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\WhatsappLOGO.png", confidence=.1)
    # g = position_whatsapp[0]
    # h = position_whatsapp[1]
    pt.moveTo(675, 131, duration=.5)

    pt.click()
    sleep(4)
    position_greendot = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\greendot2.png", confidence=.6)
    e = position_greendot[0]
    f = position_greendot[1]
    pt.moveTo(e, f, duration=.5)
    pt.click()
    position_new = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\Smiley2.png", confidence=.6)
    x = position_new[0]
    y = position_new[1]
    pt.moveTo(873, 959, duration=.5)
    #postion_link = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\link.png", confidence=.1)
    #j = postion_link[0]
    #h = postion_link[1]
    #pt.moveTo(j, h, duration=.4)
    # pt.tripleClick()
    # pt.rightClick()
    # pt.moveRel(12, 15)
    # pt.click()
    # whatsapp_message = pyperclip.paste()
    pt.click()
    sleep(8)
    #position_audio = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\Google Meet Mic.png", confidence=.01)
    #a = position_audio[0]
    #b = position_audio[1]
    pt.moveTo(657, 812, duration=.5)
    pt.click()
    #position_video = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\Google Meet Video.png", confidence=.01)
    #c = position_video[0]
    #d = position_audio[1]
    pt.moveTo(756, 804, duration=.5)
    pt.click()
    position_AskToJoin = pt.locateOnScreen(r"C:\Users\gagan\PycharmProjects\GoogleMeetBot\GgMeet\AskToJoin.png", confidence=.4)
    y = position_AskToJoin[0]
    z = position_AskToJoin[1]
    pt.moveTo(1376, 633, duration=.5)
    pt.click()

    sleep(10)
    pt.moveTo(996, 1012, duration=.6)
    sleep(10)
    pt.click()


get_message()
