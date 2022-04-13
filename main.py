from turtle import delay
import pyautogui
import time

xred = "2535"
yred = "417"

xblack = "2719"
yblack = "421"

xwhite = "0"
ywhite = "0"


aposta = input("Informe a Aposta: ")
print("Aposta Informada: ", aposta)

if(aposta  == "red"): 
    xposicion = xred
    yposicion = yred

if(aposta == "black"):
    xposicion = xblack
    yposicion = yblack


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://blaze.com/pt/games/double")
pyautogui.press('enter')

pyautogui.click(xposicion,yposicion) 