import pyautogui as pyu
import time, logging
import datetime
print(pyu.size())

points = 0
points += 4
print(f"Hash {points} : time {datetime.datetime.now()} ")

logging.basicConfig(filename='logs.txt', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

while True:

    #window 1
    #pyu.mouseInfo()
    pyu.moveTo(96,63, duration= 0.2)
    pyu.leftClick()
    pyu.leftClick()
    pyu.moveTo(318,230, duration=0.2)
    pyu.leftClick()
    pyu.moveTo(246,573, duration= 0.2)
    pyu.leftClick()

    #window 2
    #pyu.mouseInfo()
    pyu.moveTo(595,63, duration= 0.2)
    pyu.leftClick()
    pyu.leftClick()
    pyu.moveTo(830,230, duration=0.2)
    pyu.leftClick()
    pyu.moveTo(750,573, duration= 0.2)
    pyu.leftClick()

    #window 3
    #pyu.mouseInfo()
    pyu.moveTo(1095,63, duration= 0.2)
    pyu.leftClick()
    pyu.leftClick()
    pyu.moveTo(1315,230, duration=0.2)
    pyu.leftClick()
    pyu.moveTo(1251,573, duration= 0.2)
    pyu.leftClick()

    time.sleep(15)

    #window phase 2
    pyu.moveTo(246,512, duration=0.2)
    pyu.leftClick()
    #while True:
        #print(pyu.position())


    #window phase 2
    pyu.moveTo(750,512, duration=0.2)
    pyu.leftClick()


    #window phase 2
    pyu.moveTo(1251,512, duration=0.2)
    pyu.leftClick()


    time.sleep(60)

    points += 4
    print(f"Hash {points} : time {datetime.datetime.now()} ")

    logging.warning(f"Hash {points} : time {datetime.datetime.now()} ")