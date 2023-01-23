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
    print('''PLease note that this is in beta and therfore
results may be incorrect\n\n''')
    print('What would you like to do:')
    time.sleep(0.2)
    print('\n1) Check password strength')
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
    password = pwinput.pwinput(prompt = 'Enter the password to be checked: ', mask = '*')
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
        
    sChars = ['@', '%', '+', '/', '|', r'\', r''', '!', '#', '$', '^', '?', ':', ',', '(', ')',\
'{', '}', '[', ']', '~', '-', '.', '£', '"', '&', '_', '*']
    
    nums = '1 2 3 4 5 6 7 8 9 0'.split()
        
    for l in lPassword:
        if l in sChars:
            points += 1
        if l in nums:
            points += 1
            
       
    with open('cPasswords.txt','r') as f:
        cPL = f.readlines()
        
    for line in cPL: #check if password is in common password list
        if password == line.replace('\n',''):
            points -= 100
            

            
    
    for i in tqdm (range (100), desc='Checking password...'): #for loop for progress bar
        time.sleep(0.001)    
    clear()

    #consider using switch statement here
    match points:
        case _ if points < -2:
            print('Your password is extremely weak')        
        case -2 :
            print('Your password is very weak')
        case -1:
            print('Your password is weak')
        case 0:
            print('Your password is on the weaker side')
        case 1:
            print('Your password is neither strong or weak')
        case 2:
            print('Your password is strong')
        case 3:
            print('Your password is very strong')
        case _ if points > 3:
            print('Your password is extremely strong!')
        case _:
            print('\nThe password entered was identified as a common password')
    '''
    if points < -2:
        print('Your password is extremely weak')
    elif points == -2:
        print('Your password is very weak')
    elif points == -1:
        print('Your password is weak')
    elif points == 0:
        print('Your password is on the weaker side')
    elif points == 1:
        print('Your password is neither strong or weak')
    elif points == 2:
        print('Your password is strong')
    elif points == 3:
        print('Your password is very strong')
    elif points > 3:
        print('Your password is extremly strong!')
        
    if points < -50:
        print('\nThe password entered was identified as a common password')
    '''    
    print('\nPress enter to continue')
    keyboard.wait('enter')
    
             
        
    

        
    