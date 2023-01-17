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



while True:
    clear()
    print(Fore.RED + '''PLease note that this is in beta and therfore
results may be incorrect\n\n''')
    print(Fore.GREEN + 'What would you like to do:')
    time.sleep(0.2)
    print(Fore.BLUE + '\n1) Check password strength')
    time.sleep(0.1)
    print('2) Return to main menu')
    
    while True:
        if keyboard.is_pressed('1'):
            break
        elif keyboard.is_pressed('2'):
            clear()
            call(['python','password_Manager.py'])
            sys.exit()
            
    clear()
    flush_input()
    password = pwinput.pwinput(prompt = Fore.YELLOW + 'Enter the password to be checked: ', mask = '*')
    points = 0
    
    
    uppers = [u for u in password if u.isupper()]
    lowers = [l for l in password if l.islower()]
    if len(uppers) > len(lowers):
        gap = len(uppers) - len(lowers)
    else:
        gap = len(lowers) - len(uppers)
    
    if gap > 5:
        points -= 1
    elif gap > 2 and gap <= 5:
        points += 1
    else:
        points += 2
        
    if len(uppers) <= 5 or len(lowers) <= 5:
        points -=3
        
    lPassword = []
    for l in password:
        lPassword.append(l)

    if len(lPassword) <= 4:
        points -= 2
    elif len(lPassword) > 4 and len(lPassword) <= 6:
        points -= 1
    elif len(password) > 8:
        points += 1
    elif len(password) > 13:
        points += 2
        
    sChars = ['@', '%', '+', '/', '\\', '\'', '!', '#', '$', '^', '?', ':', ',', '(', ')',\
'{', '}', '[', ']', '~', '-', '.', '£', '"', '&', '_', '*']
    
    nums = '1 2 3 4 5 6 7 8 9 0'.split()
        
    for l in lPassword:
        if l in sChars:
            points += 1
        if l in nums:
            points += 1
            
    
    for i in tqdm (range (100), desc=Fore.BLUE + 'Checking password...'):
        time.sleep(0.001)    
    clear()
    if points < -2:
        print(Fore.RED + 'Your password is extremly weak')
    elif points == -2:
        print(Fore.RED + 'Your password is very weak')
    elif points == -1:
        print(Fore.RED + 'Your password is weak')
    elif points == 0:
        print(Fore.YELLOW + 'Your password is on the weaker side')
    elif points == 1:
        print(Fore.YELLOW + 'Your password is neither strong or weak')
    elif points == 2:
        print(Fore.GREEN + 'Your password is strong')
    elif points == 3:
        print(Fore.GREEN + 'Your password is very strong')
    elif points > 3:
        print(Fore.GREEN + 'Your password is extremly strong!')
        
    print(Fore.BLUE + '\nPress enter to continue')
    keyboard.wait('enter')
    
             
        
    

        
    