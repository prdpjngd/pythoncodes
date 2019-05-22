#!/usr/bin/pyhton3

import socket 

ip="0.0.0.0"
port=8181

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((ip,port)) # bind function only takes one input arg. i.e tupple here

while True:
    web=s.recvfrom(100)
    print(web)
    s.sendto("1".encode('ascii'),web[1])
