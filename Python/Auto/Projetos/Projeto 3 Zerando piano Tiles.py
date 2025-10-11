import pyautogui
import keyboard
from time import sleep
import win32api
import win32con

pyautogui.click(1120,500,duration=1) # Start 

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.06)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('1') == False:
        if pyautogui.pixelMatchesColor(997,405,(0, 0, 0)):
            click(997,405)
        if pyautogui.pixelMatchesColor(1089,407,(0, 0, 0)):
            click(1089,407)
        if pyautogui.pixelMatchesColor(1179,409,(0, 0, 0)):
            click(1179,409)
        if pyautogui.pixelMatchesColor(1269,409,(0, 0, 0)):
            click(1269,409)
