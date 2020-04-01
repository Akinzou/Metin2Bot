import pydirectinput
import time
keys = ["w","a","s","d"]
was = int(time.time())
now = 0

def healAndUp():
    for i in range (0,3):
        pydirectinput.press("1")
        pydirectinput.press("`")


while 1:
    pydirectinput.keyDown("space")
    for i in range(len(keys)):
        pydirectinput.keyDown("space")
        pydirectinput.press(keys[i])
        healAndUp()
    healAndUp()
    pydirectinput.moveTo(1000, 1000)
    time.sleep(0.5)
    pydirectinput.moveTo(795, 597)
    pydirectinput.click()
    now = int(time.time())

    if now - was >= 30:
        was = int(time.time())
        pydirectinput.press("2")
