import socket
import thread

server_socket=socket.socket()

def main():
    server_socket.bind(("127.0.0.1",8888))

    f = open('pic.png','wb')
    server_socket.listen(5)
    while True:
        (client_socket, client_address) = server_socket.accept()
        l = client_socket.recv(1024)
        while (l):
            f.write(l)
            l = client_socket.recv(1024)
        f.close()


    print f

    try:
        new_thread = thread.start_new_thread(send(file,))
        new_thread = thread.start_new_thread(recv(file,))
    except:
        print "Error: unable to start thread"

    while True:
        pass
    client_socket.close()
    server_socket.close()


def recv(file):
    pass


def send(file):
    pass


if __name__=="__main__":
    main()


