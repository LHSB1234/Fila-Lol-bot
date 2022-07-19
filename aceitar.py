from time import sleep
import pyautogui

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    

def check_screen():
    button_pos = pyautogui.locateOnScreen('fila2.png', confidence=0.7)
            
    if button_pos != None:
        print(f'Found {button_pos}')
        click(button_pos.left, button_pos.top)
        return True
    
    return False

def main():
    while True:
        if check_screen():
            print("achou")
            sleep(6)
            #break

main()