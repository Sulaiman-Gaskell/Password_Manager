import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
init()
os.system('color FFFF')
#exit()

with open('appearance.txt','r') as f:
    colour = f.read()

match colour:
    case '1':#Light
        os.system('color F0')
        
    case '2':#Grey dark
        os.system('color 08')
        print(Style.BRIGHT + '')
        
    case '3':#Magenta dark
        os.system('color 05')
        
    case '4':#Blue dark
        os.system('color 01')

    case '5': 
        os.system('color DF')
        
    case '6': #Classic
        os.system('color 00')
    
os.system('cls')
introText = '''V1.4.0\n
Welcome to the Password Manager!
Here you can store and generate passwords while checking the strength.\n\n'''

for c in introText:
    print(c, end='')
    time.sleep(0.000001)
    
    
call(['python', 'password_Manager.py'])
exit() 
