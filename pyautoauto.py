#bad boyssdafasfd
import pyautogui
import time
import sys
print("hello1")
pyautogui.position()

# Point(x=1581, y=276)
# Point(x=2241, y=834)
print(pyautogui.position())
# pyautogui.moveTo(2241,834,2)   #2초간 이동
# pyautogui.moveRel(0,300,2)     #시작 위치에서 이동
# pyautogui.moveRel(-100,0,2)     #시작 위치에서 이동


# pyautogui.moveTo(708,118,2)   #2초간 이동
# pyautogui.click(clicks=2, interval =2) #클릭 2번 / 더블클릭 pyautogui.click(clicks=2)

pyautogui.moveTo(241,1350,1)
pyautogui.doubleClick()
time.sleep(1)

pyautogui.typewrite(['enter'])
pyautogui.typewrite("hello ")
pyautogui.typewrite(['enter'])










print("hello2")