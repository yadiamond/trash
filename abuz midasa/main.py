import pyautogui
import keyboard
import time

def search_mouse_position(q):
    if q == '9':
        pyautogui.moveTo(1691, 1051)
        time.sleep(0.1)
        pyautogui.click(1691, 1051)
        time.sleep(0.1)
        pyautogui.moveTo(1652, 68)
        time.sleep(0.1)
        pyautogui.click(1652, 68)
        time.sleep(0.1)
        pyautogui.moveTo(1546, 120)
        time.sleep(0.1)
        pyautogui.click(1546, 120, button = 'right')
        time.sleep(0.1)
        pyautogui.moveTo(1160, 963)
        time.sleep(0.1)
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.moveTo(1089, 626)
        time.sleep(0.1)
        pyautogui.mouseUp()
        time.sleep(0.1)
        pyautogui.moveTo(1692, 914)
        time.sleep(0.1)
        pyautogui.click(1692, 914, button = 'right')
        time.sleep(0.1)
        pyautogui.moveTo(1747, 929)
        time.sleep(0.1)
        pyautogui.click(1747, 929)
        time.sleep(0.1)
        pyautogui.moveTo(1091, 620)
        time.sleep(0.1)
        pyautogui.click(1091, 620, button = 'right')

def handle_key_press(key):
    if key.name == '9':
        search_mouse_position('9')
        
keyboard.on_press(handle_key_press)

keyboard.wait()
