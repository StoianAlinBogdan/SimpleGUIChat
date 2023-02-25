import socket
import threading

def send(sock: socket.socket):
    while True:
        data = input()
        sock.sendall(bytes(str(data), encoding="ascii"))
        if data == "!EXIT":
            sock.close()
            break
    exit(1)


def receive(sock: socket.socket):
    while True:
        data = sock.recv(1024)
        print(data)


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 5678))
    threading.Thread(target=send, args=(sock,)).start()
    threading.Thread(target=receive, args=(sock,)).start()
    