import socket
import os
import select
import sys

def prompt():
    sys.stdout.write('Server :  ')
    sys.stdout.flush()

try:
    newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    newSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except:
    print 'socket Error'
    sys.exit(1)

newSocket.bind(('127.0.0.1', 8000))
newSocket.listen(5)

input_list = [newSocket, sys.stdin]

print 'Chat Program'
prompt()

while True:

    inputready, outputready, exceptready = select.select(input_list,[],[])

    for sock in inputready:

        if sock == newSocket:
            (client, (ip, port)) = newSocket.accept()
            input_list.append(client)
            data = client.recv(2048)
            if data:
                sys.stdout.write(data)

        elif sock == sys.stdin:
            msg = sys.stdin.readline()
            newSocket.send('\r<Server>: ' + msg)
            prompt()

        else:
            data = sock.recv(2048)
            if data:
                sys.stdout.write(data)

newSocket.close()
