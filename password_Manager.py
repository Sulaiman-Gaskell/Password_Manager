import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
init()
import keyboard

def flush_input():
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()

clear = lambda: os.system('cls')


while True:    
    print('Choose an option:\n')
    time.sleep(0.1)
    print('''1) Check password strength
2) Managed saved passwords (Coming soon)
3) Generate a new password (Coming soon)
4) Settings''')

    while True:
        if keyboard.is_pressed('1'):
            call(['python','pStrength.py'])
            exit()
            break
        
        if keyboard.is_pressed('4'):
            call(['python','settings.py'])
            exit()
        
    clear()

    