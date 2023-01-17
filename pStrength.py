import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
init()
import keyboard

clear = lambda: os.system('cls')
clear()

while True:
    clear()
    print(Fore.GREEN + 'What would you like to do:')
    time.sleep(0.2)
    print(Fore.BLUE + '\n1) Check password strength')
    time.sleep(0.1)
    print('2) Return to main menu')
    
    while True:
        if keyboard.is_pressed('1'):
            break
        elif keyboard.is_pressed('2'):
            call(['python','password_Manager.py'])
            sys.exit()