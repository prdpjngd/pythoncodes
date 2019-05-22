#!/usr/bin/python3

import socket 

target_ip="13.234.242.197"

target_port=8181

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg=inpur("plz type here  ")
    n=msg.encode("ascii")
    s.sendto(n,(target_ip,target_port))
    print(s.recvfrom(1000))
