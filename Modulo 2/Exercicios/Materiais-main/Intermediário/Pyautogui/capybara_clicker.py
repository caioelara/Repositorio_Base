# https://www.crazygames.com.br/jogos/capybara-clicker

import pyautogui as pag
from time import sleep
import keyboard


#pag.moveTo(706, 560, duration=1)

keyboard.wait('s')
sleep(5)
while True:
    pag.doubleClick()
    if keyboard.is_pressed('q'):
        print('Parando o programa...')
        break



#pag.displayMousePosition()