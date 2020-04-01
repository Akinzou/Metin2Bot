import pydirectinput
import time
keys = ["w","a","s","d"]
was = int(time.time())
now = 0

def healAndUp():
    for i in range (0,3):
        #use health potion
        pydirectinput.press("1")
        #pick up item
        pydirectinput.press("`")


while 1:
    pydirectinput.keyDown("space")
    for i in range(len(keys)):
        pydirectinput.keyDown("space")
        #Turning
        pydirectinput.press(keys[i])
        healAndUp()
    healAndUp()

    #AntyBOT {
    pydirectinput.moveTo(1000, 1000)
    time.sleep(0.5)
    pydirectinput.moveTo(795, 597)
    pydirectinput.click()
    #}
    now = int(time.time())

    #Use hood every 30s
    if now - was >= 30:
        was = int(time.time())
        pydirectinput.press("2")
