import socket
import select
from Queue import Queue
import sys

size=2048  # bytes of data to be trasferred in one go

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.setblocking(0)
server_sock.bind(("0.0.0.0",int(sys.argv[1])))
server_sock.listen(1)

inputs = [sys.stdin, server_sock]
outputs = [sys.stdout]
msg_recvd = Queue()
msg_to_send = Queue()


while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, []
        )
    for s in readable:
        if s is server_sock:
            client_sock,(ip,port) = server_sock.accept()
            client_sock.setblocking(0)
            sys.stdout.write("client connected: {}:{}".format(ip,port))
            inputs.append(client_sock)
            outputs.append(client_sock)
        elif s is sys.stdin:
            data = s.readline()
            msg_to_send.put(str(data))
        else:
            data = s.recv(size)
            msg_recvd.put(str(data))
    for s in writable:
        if s is sys.stdout:
            while not msg_recvd.empty():
                msg = msg_recvd.get()
                s.write("client: {}".format(msg))
                s.flush()
        else:
            while not msg_to_send.empty():
                msg = msg_to_send.get()
                s.send(msg)
                
