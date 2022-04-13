import pyautogui
import time

def init():
    
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("https://blaze.com/pt/games/double")
    pyautogui.press('enter')