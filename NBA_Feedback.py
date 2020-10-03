import pyautogui as pag
import time 
# moves mouse pointer to the coordinates entered and L-clicks
def moveandclick(x_cord,y_cord):
    pag.moveTo(x_cord,y_cord)
    pag.leftClick(x_cord,y_cord)
# Selects 'B' or '2' 
# Add more 'pag.press('right') to go further right
# replace right with enter to select 'A' or '1'
def clickB():
    pag.press('tab')
    pag.press('right')
# func to click submit
def nextClick():
    pag.press('tab')
    pag.press('enter')
# func for page 1
def page_1():
    for i in range(11):
        clickB()
    nextClick()
# func for page 2
def page_2():
    for i in range(13):
        clickB()
    pag.press('tab')
    nextClick()
# func for page 3
def page_3():
    # edit no of iterations depending upon no of subjects and remember to change
    # coordinates accordingly, generally just the Y Coordinate
    
    for i in range(3):
        clickB()
    pag.press('tab')
    nextClick()

moveandclick(1670,800)
page_1()
time.sleep(45)
moveandclick(1670,860)
page_2()
time.sleep(45)
moveandclick(1720,835)
page_3()
