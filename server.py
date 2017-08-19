import socket
import sys
size=2048  # bytes of data to be trasferred in one go
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("0.0.0.0",int(sys.argv[1])))

sock.listen(2)

(client,(ip,port))=sock.accept()

print "client connected: {}:{}".format(ip,port)

print "client: {}".format(client.recv(size))

client.send("hello {}:{}!! Welcome to Chatonym. We will develope more".format(ip,port))

client.close()
