import time
import os
from colorama import Fore, Back, Style, init
import sys
init()
import keyboard

clear = lambda: os.system('cls')
clear()


introText = '''V1.0.0\n
Welcome to the Password Manager!
Here you can store and generate passwords while checking the strength.
Currently you can only check the strength of your password.\n\n'''

for c in introText:
    print(Fore.GREEN + c, end='')
    time.sleep(0.000001)


while True:    
    print(Fore.BLUE + 'Choose an option:\n')
    time.sleep(0.1)
    print(Fore.YELLOW + '''1) Check password strength
2) Managed saved passwords (Coming soon)
3) Generate a new password (Coming soon)''')

    while True:
        if keyboard.is_pressed('1'):
            choice = 1
            break
        
    clear()
