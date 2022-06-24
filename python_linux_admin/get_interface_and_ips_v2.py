import socket
import psutil
x = psutil.net_if_addrs().items()
#print("IFACE    IP         NETMSK------BROADCAST")
for intface, ipaddy in x:
    print(intface, ipaddy[0][1], ipaddy[0][2], ipaddy[0][3])
    #print(intface, ipaddy[0][4]) #Check if this actually checks PTP
