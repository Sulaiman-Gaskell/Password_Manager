import time
import os
from colorama import Fore, Back, Style, init
import sys
from subprocess import call
init()

introText = '''V1.0.0\n
Welcome to the Password Manager!
Here you can store and generate passwords while checking the strength.
Currently you can only check the strength of your password.\n\n'''

for c in introText:
    print(Fore.GREEN + c, end='')
    time.sleep(0.000001)