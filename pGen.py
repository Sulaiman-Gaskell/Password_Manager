import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
from tqdm import tqdm
init()
import keyboard
import pwinput
import string
import random
import pyperclip

def flush_input():
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()

clear = lambda: os.system('cls')
clear()



    
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

while True:

    print('''Please note that this in still in development!\n\n''')

    print('''Choose an option:

1) Generate a new password
2) Return to main menu\n''')

    while True:
        if keyboard.is_pressed('1'):
            break
        elif keyboard.is_pressed('2'):
            clear()
            call(['python', 'password_Manager.py'])
            sys.exit()
            

    clear()
    while True:
        try:
            flush_input()
            length = int(input('Enter how long you want your password to be (>=8 chars): '))
            if length < 8:
                length = int('f')
            else:  
                break
        except:
            print('\nThat is too short or invalid try again\n')
            time.sleep(0.1)
  
    while True:
            
        password = generate_password(length)
        clear()
        print(password + '\n-----------------------------------------------------------------------')
        print('This is your password')
        print('\nDon\'t like it? Press \'Enter\' to generate a new password\nOr press \'c\' \
to copy current password to clipboard\nOr press \'n\' to finish')
        while True:
            if keyboard.is_pressed('enter'):
                break
            elif keyboard.is_pressed('c'):
                pyperclip.copy(password)
                clear()
                print('Copied to clipboard!')
                time.sleep(1)
                clear()
                break
            elif keyboard.is_pressed('n'):
                call(['python','pGen.py'])
                sys.exit()
        



