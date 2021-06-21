#!/usr/bin/python3
# This code write by Mr.nope
import socket
import sys
import os
import time
class color:
    green = '\033[92m'
    red = '\033[91m'
    End = '\033[0m'
ip = "\nEnter ip: "
opt = "\nIPz/> "
def title():
    os.system("printf '\033]2;IPz\a'")
def cls():
    os.system("clear")
def main():
    title()
    cls()
    print(color.green + """
        -[ IPz ]- (Version: 1.3.0) """ + color.red + """
      ---[ This code write by Mr.nope ]--- """ + color.End + """
      ---[ Github: https://github.com/mrprogrammer2938 ]---
      """)
    print("{1}-Start")
    print("{2}-Exit")
    choose = input(opt)
    if choose == '1':
        menu()
    elif choose == '2':
        ext()
    else:
        main()
def menu():
    cls()
    try:
        host = input(ip)
        time.sleep(1)
        attack = socket.gethostbyname(host)
        print("""
-------------------------------
web        |     IP           |
-------------------------------
""" + host + " | " + attack + """   |
-------------------------------""")
        try1()
    except EOFError:
        return False
def try1():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
        menu()
    elif try_again == 'n':
        ext()
    else:
        try1()
def ext():
    cls()
    print("Exiting...")
    sys.exit()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        sys.exit()