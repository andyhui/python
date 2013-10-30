#!/usr/bin/python
import socket
import sys

HOST,PORT = "localhost",9998
#data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	sock.connect((HOST,PORT))
	#f = open('test.tar','rb')
	f = open(sys.argv[1],'rb')
	while True:
		data = f.read(1024)
		if not data:
			break
		sock.send(data)
	f.close()
	#sock.sendall(data + "\n")
	receive = sock.recv(1024)
finally:
	sock.close()

print "Sent:	{}".format(data)
print "Received:{}".format(receive)
