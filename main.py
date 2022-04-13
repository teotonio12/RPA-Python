import red
import black
import white
import setup

setup.init()

aposta = input("Informe a Aposta: ")
print("Aposta Informada: ", aposta)

if(aposta  == "red"): 
    red.apostar()
    white.apostar()

if(aposta == "black"):
    black.apostar()
    white.apostar()

