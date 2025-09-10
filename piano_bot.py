from pyautogui import *
import pyautogui as ag
import time
import keyboard
import win32api, win32con

# Click Function
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)

# Timeout to give time to start the web game
time.sleep(3)

y = 700
# Main while loop
while keyboard.is_pressed("q") == False:


    if ag.pixel(745, y)[0] == 0:  # Checking if the pixel is black or not and if it is it clicks
        click(745, y)

    if ag.pixel(898, y)[0] == 0:
        click(898, y)

    if ag.pixel(1048, y)[0] == 0:
        click(1048, y)

    if ag.pixel(1186, y)[0] == 0:
        click(1186, y)
