#!/usr/bin/python3

import socket

s_ip="13.234.242.197"
s_port=8181

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 2>1:
	msg=input("plz input here  : ")
	sms=msg.encode('ascii')
	s.sendto(sms,(s_ip,s_port))
	
