import socket
import threading
#import time
import struct
def function(newsock, address):
    FILEINFO_SIZE = struct.calcsize('128sI')
    while 1:
        try:
            fhead = newsock.recv(FILEINFO_SIZE)
            filename, filesize = struct.unpack('128sI', fhead)
            #filesize = os.path.getsize()
            print "address is: ",address
            print filename, len(filename),type(filename)
            print filesize
            filename = 'new_'+filename.strip('\00')
            fp = open(filename,'wb')
            restsize = filesize
            print "recving..."
            while 1:
                if restsize > 1024:
                    filedata = newsock.recv(1024)
                else:
                    filedata = newsock.recv(restsize)
                    fp.write(filedata)
                    break
                if not filedata:
                    break
                fp.write(filedata)
                restsize = restsize - len(filedata)
                if restsize <= 0:
                    break
            fp.close()
            print "recv succeeded !!File named:",filename
        except:
            print "he socket partner maybe closed"
            newsock.close()
            break
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8887))
sock.listen(5)
while True:
    newsock, address = sock.accept()
    print "accept another connection"
    tmpThread = threading.Thread(target=function,args=(newsock,address))
    tmpThread.start()
print 'end'
