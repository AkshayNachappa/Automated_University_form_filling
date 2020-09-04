import pyautogui as pag
import time 
def moveandclick(x_cord,y_cord):
    pag.moveTo(x_cord,y_cord)
    pag.leftClick(x_cord,y_cord)

def clickB():
    pag.press('tab')
    pag.press('right')
def nextClick():
    pag.press('tab')
    pag.press('enter')

def page_1():
    for i in range(11):
        clickB()
    nextClick()
    
def page_2():
    for i in range(13):
        clickB()
    pag.press('tab')
    nextClick()
def page_3():
    # edit no of iterations depending upon no of subjects and remember to change
    # coordinates accordingly, generally just the Y Coordinate
    
    for i in range(4):
        clickB()
    pag.press('tab')
    nextClick()

moveandclick(1670,800)
page_1()
time.sleep(8)
moveandclick(1670,860)
page_2()
time.sleep(8)
moveandclick(1695,830)
page_3()