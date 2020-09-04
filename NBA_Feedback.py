import pyautogui as pag 
def moveandclick(x_cord,y_cord):
    pag.moveTo(x_cord,y_cord)
    pag.leftClick(x_cord,y_cord)
moveandclick(1670,800)

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

page_1()

page_2()
