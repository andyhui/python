import socket
import select
import sys

CONNECTION_LIST = []
RECV_BUFFER = 4096
PORT = 1245

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', PORT))
server_socket.listen(5)

CONNECTION_LIST.append(server_socket)
CONNECTION_LIST.append(sys.stdin)


print 'Chat server Started on port ' + str(PORT)


def broadcast_data(sock, message):

    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock and socket != sys.stdin:
            try:
                socket.send(message)
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)

def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()

prompt()

while True:
    read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], []) # NON_blocking I/O with 0

    for sock in read_sockets:
        if sock == server_socket:
            # new Connection
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
            print 'Clinet (%s, %s) connected ' % addr
            broadcast_data(sockfd, "[%s:%s] entered room" % addr)
        elif sock == sys.stdin:
            msg = sys.stdin.readline()
            broadcast_data(sock, 'Server > ' + msg)
            prompt()
        else:
            try:
                #In Windows, sometimes when a TCP program closes abruptly,
                # a "Connection reset by peer" exception will be thrown
                data = sock.recv(RECV_BUFFER)
                if data:
                    print "\r" + '<' + str(sock.getpeername()) + '>' + data
                    broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '>' + data)
            except:
                broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                print "Client (%s, %s) is offline" % addr
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue
