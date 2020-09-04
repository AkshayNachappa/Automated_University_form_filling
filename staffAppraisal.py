import pyautogui as pag
x_cord = 1750
y_cord = 630
pag.moveTo(x_cord,y_cord)
pag.leftClick(x_cord,y_cord)

def StaffAppraisal():
    for i in range(4):
        pag.typewrite('9')
        pag.press('tab')
    for i in range(10):
        pag.typewrite('4')
        pag.press('tab')
    pag.typewrite('9')
    pag.press('tab')
    pag.press('tab')
    pag.press('enter')

StaffAppraisal()
