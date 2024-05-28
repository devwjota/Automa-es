# Como simular "rolagem" do mouse
import pyautogui
from time import sleep

pyautogui.moveTo(x=...,y=...,duration=...)
for i in range(500):
    pyautogui.scroll(-1500)
    sleep(2)
