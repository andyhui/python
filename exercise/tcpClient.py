import socket
import os
import select
import sys

def prompt():
   sys.stdout.write('Client ')
   sys.stdout.flush()


try:
    newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    newSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except:
    print 'socket Error'
    sys.exit(1)


newSocket.connect(('127.0.0.1', 1245))

print 'Connected to remote host. Start sending messages'
prompt()

while 1:

    socket_list = [sys.stdin, newSocket]

    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        if sock == newSocket:
            data = sock.recv(4096)
            if not data:
                print '\nDisconnected from chat server'
                sys.exit()
            else:
                sys.stdout.write(data)
                prompt()
        else:
            msg = sys.stdin.readline()
            newSocket.send('\r<Client>: ' + msg)
            prompt()
