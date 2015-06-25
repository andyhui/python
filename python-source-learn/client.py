#!/usr/bin/env python
# encoding: utf-8

import socket

HOST='192.168.111.128'
PORT=8888
ADDR=(HOST,PORT)

BUF_SIZE = 1024

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
client.send('client sey:hello')
data = client.recv(BUF_SIZE)
if data:
    print 'client recv ----',data
client.close()
