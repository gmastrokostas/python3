import socket
import psutil
x = psutil.net_if_addrs().items()

for intface, ipaddy in x:
    print(intface, ipaddy[0][1])
    print(intface, ipaddy[0][2])
    print(intface, ipaddy[0][3])
    print(intface, ipaddy[0][4])
