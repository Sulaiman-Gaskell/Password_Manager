import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
from tqdm import tqdm
init()
import keyboard
import pwinput

def flush_input():
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()

clear = lambda: os.system('cls')
clear()

print('1) Appearance')
time.sleep(0.1)
print('2) Password hider (coming soon)')
time.sleep(0.1)
print('3) Return to main menu')
print('\nWhat would you like to change?')

while True:
    if keyboard.is_pressed('1'):
        clear()
        s = open('appearance.txt','w')
        print('1) Light theme')
        time.sleep(0.1)
        print('2) Grey dark theme')
        time.sleep(0.1)
        print('3) Magenta dark theme')
        print('\nEnter a theme number: (More coming soon!)')
        while True:
            try:
                flush_input()
                choice = int(input())
                if choice > 3 or choice < 1:
                    choice = int('f')
                else:
                    s.write(str(choice))
                    clear()
                    s.close()
                    call(['python','firstLogOn.py'])
                    exit()
                    break
            except:
                print('\nOopsy that is invalid')
                
    elif keyboard.is_pressed('2'):
        pass
    
    elif keyboard.is_pressed('3'):
        clear()
        call(['python', 'password_Manager.py'])
        exit()
                
                  
                
        
        