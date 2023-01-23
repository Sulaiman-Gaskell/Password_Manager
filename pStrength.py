import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
from tqdm import tqdm
init()
import keyboard
import pwinput

def flush_input(): #flushes input buffer
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()

clear = lambda: os.system('cls') #creates a function to clear the screen
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
    password = pwinput.pwinput(prompt = 'Enter the password to be checked: ', mask = '*') #gets password to be checked and masks it with '*'
    points = 0
    
    
    uppers = [u for u in password if u.isupper()] #gets list of upper case letters in password
    lowers = [l for l in password if l.islower()] #gets list of lower case letters in password
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
        
    if len(uppers) <= 5 or len(lowers) <= 5: #checks if password has less than 5 upper or lower case letters
        points -=3
        
    #lPassword = []
    #for l in password:
    #    lPassword.append(l) #converts password to list (NOT NEEDED AS A STRING CAN BE TREATED AS AN IMMUATABLE LIST)

    if len(password) <= 4:
        points -= 2
    elif len(password) > 4 and len(password) <= 6:
        points -= 1
    elif len(password) > 8:
        points += 1
    elif len(password) > 13:
        points += 2
        
    sChars = ['@', '%', '+', '/', '|', r'\', r''', '!', '#', '$', '^', '?', ':', ',', '(', ')',\
'{', '}', '[', ']', '~', '-', '.', '£', '"', '&', '_', '*'] #list of special characters
    
    nums = '1 2 3 4 5 6 7 8 9 0'.split() #list of numbers
        
    for l in password: #adds an extra point for each special character and number
        if l in sChars:
            points += 1
        if l in nums:
            points += 1
            
       
    with open('cPasswords.txt','r') as f: 
        cPL = f.readlines()
        
    for line in cPL: #check if password is in common password list
        if password == line.replace('\n',''):
            points -= 100
            

            

    print('----------------------------------------\n\n')
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

    print('\nPress enter to continue')
    keyboard.wait('enter')
    
             
        
    

        
    