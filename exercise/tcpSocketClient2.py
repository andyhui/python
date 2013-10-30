import socket  
import time  
import struct  
import os  
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
sock.settimeout(1)  
#e=  
try:  
    e=sock.connect(('127.0.0.1',8887))  
    print 'connect...'  
except socket.timeout,e:  
    print 'timeout',e  
except socket.error,e:  
    print 'error',e  
except e:  
    print 'any',e  
if not e:  
    while (1):  
        filename = raw_input('input your filename------->')  
        FILEINFO_SIZE = struct.calcsize('128sI') 
        fhead = struct.pack('128sI',filename,os.stat(filename).st_size)
        sock.send(fhead) 
        fp = open(filename,'rb')  
        while 1:         
            filedata = fp.read(1024)  
            if not filedata:  
                break  
            sock.send(filedata)  
        print "sending over..."  
        fp.close()  
