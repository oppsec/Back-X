#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Gr3n0xX
# Python backdoor generator 

try:
    import sys
    import os
    import time

    from payloads.pythonpayload import pyload
   
    from src.message import success, error
    from src.clear import clear_terminal
    from src.ascii import get_ascii

except KeyboardInterrupt:
    error("Exiting...")
    sys.exit()

if sys.version_info[0] < 3:
    error("Run this tool with Python 3 please.")
    sys.exit()

    
def banner():
    clear_terminal()
    get_ascii()

def main():
    clear_terminal()
    get_ascii()
    pyload()

if __name__ == "__main__":
    main()
