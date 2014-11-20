#!/usr/bin/env python
# encoding: utf-8

import socket

HOST='127.0.0.1'
PORT=8888
ADDR=(HOST,PORT)
BUF_SIZE=1024

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(1)

conn,addr = server.accept()
print 'server connneted by:',addr
while 1:
    data = conn.recv(BUF_SIZE)
    if not data:
        break
    print 'server recv:',data
    conn.send('server received success')
conn.close()
