import socket
import sys
import os
import time
from time import *
from datetime import datetime
################################

print ("\033[31m")

os.system("figlet Hallo TO Moaz Mohamed Script ")
sleep(3)
os.system("clear")

print ("\033[1;34m")

os.system("figlet Port Scan Network ")

print ("\033[36m")

print ("BY:Moaz Mohamed")
print ("Github : https://github.com/MoazMohamed891")
print ("Linkedin : https://www.linkedin.com/in/moaz-mohamed-10b807318")

print ('\033[1;37m')
ip = input("Enter Your IP : ")
t1 =datetime.now()
print ("Scanning Start.. %s Please Wait.. "%ip)
sleep(1)
################################
try:
    for port in range(1,6553):
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if (s.connect_ex((ip,port))==0):
             try:
                  serv=socket.getservbyport(port)

             except socket.error:
                 serv="Unknown Service"
             print ("Port %s Open Service:%s "%(port,serv))
        t2=datetime.now()
        t3=t2-t1
    print ("Scanning Completed On %s"%t3)
except KeyboardInterrupt:
    print ("See You Soon....!") 
