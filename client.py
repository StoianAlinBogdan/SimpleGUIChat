import socket
import threading
from interface import _VARS, main_loop


def send(sock: socket.socket):
    while True:
        if _VARS["data_to_send"]:
            data = _VARS["data_to_send"].pop()
            if data is not None:
                print(data)
                sock.sendall(bytes(str(data), encoding="ascii"))
    exit(1)


def receive(sock: socket.socket):
    while True:
        data = sock.recv(1024)
        print(data)
        _VARS["data_to_display"].append(data)


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 5678))
    threading.Thread(target=send, args=(sock,), daemon=True).start()
    threading.Thread(target=receive, args=(sock,), daemon=True).start()
    threading.Thread(target=main_loop).start()