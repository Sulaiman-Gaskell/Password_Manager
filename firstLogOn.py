import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
init()
os.system('color 00')

with open('appearance.txt','r') as f
    colour = f.read()

match colour:
    case '1':
        os.system('color 7F')
        print(Fore.BLACK + Back.WHITE + Style.BRIGHT + '')
    case '2':
        os.system('color 08')
        print(Fore.WHITE + '')
    case '3':
        os.system('color 00')
        print(Fore.MAGENTA + Back.BLACK + '')
    
os.system('cls')
introText = '''V1.2.2\n
Welcome to the Password Manager!
Here you can store and generate passwords while checking the strength.\n\n'''

for c in introText:
    print(c, end='')
    time.sleep(0.000001)
    
    
call(['python', 'password_Manager.py'])
exit() 
