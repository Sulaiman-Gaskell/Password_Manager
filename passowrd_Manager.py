import time
import os
from colorama import Fore, Back, Style, init
import sys
init()

clear = lambda: os.system('cls')
clear()


introText = '''V1.0.0\n
Welcome to the Password Manager!
Here you can store and generate passwords while checking the strength.
Currently you can only check the strength of your password.'''

for c in introText:
    print(Fore.GREEN + c, end='')
    time.sleep(0.000001)


while True:    
    print(Fore.BLUE + '\nChoose an option:\n')
    print(Fore.YELLOW + '''1) Check password strength
    2) Managed saved passwords (Coming soon)
    3) Generate a new password (Coming soon)''')

    while True:
        try:
            choice = int(input('\n-'))
            if choice > 1 or choice < 1:
                choice = int('f')
            else:
                break
        
        except:
            print(Fore.RED + 'Oopsy that\'s not ready yet\n')

    clear()
