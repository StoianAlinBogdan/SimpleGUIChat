import socket
import threading

connections = []

def accept_connections(sock: socket.socket):
    while True:
        conn, addr = sock.accept()
        connections.append([conn, addr, 0])

def communicate(conn, addr):
    while True:
        data = conn.recv(1024)
        for connection in connections:
            connection[0].sendall(bytes(str(data), encoding="ascii"))

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost",5678))
    sock.listen()
    try:
        threading.Thread(target=accept_connections, args=(sock,)).start()
        while True:
            if len(connections) == 0:
                continue
            else:
                for connection in connections:
                    if(connection[2] == 0):
                        threading.Thread(target=communicate, args=(connection[0], connection[1])).start()
                        connection[2] = 1
    except KeyboardInterrupt:
        for connection in connections:
            connection[0].close()

    

    