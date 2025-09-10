import pyautogui as pag

# pag.displayMousePosition()

for i in range(20):
    pag.moveTo(300 + 20 * i, 300 + 10 * i, duration=0.2)
    pag.moveTo(400 + 20 * i, 300 + 10 * i, duration=0.2)
    pag.moveTo(400 + 20 * i, 400 + 10 * i, duration=0.2)
    pag.moveTo(300 + 20 * i, 400 + 10 * i, duration=0.2)

