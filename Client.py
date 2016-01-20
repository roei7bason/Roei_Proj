import socket

client_socket=socket.socket()
client_socket.connect(("127.0.0.1",8888))

FileSend=raw_input("Enter File Name:")

f = open(FileSend,'rb')
l = f.read(1024)
while (l):
    client_socket.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"

file=client_socket.recv(1024)
print file

client_socket.close()


