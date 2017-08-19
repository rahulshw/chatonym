import socket
import sys

size = 2048  # bytes to receive at a time
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((sys.argv[1],int(sys.argv[2])))


message="Hey!!, I am the first client."

print("You: {}".format(message))
sock.send(message)
print("Server: {}".format(str(sock.recv(size))))
sock.close()



