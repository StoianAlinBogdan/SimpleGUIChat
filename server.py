import socket
import threading

connections = []
usernames = []

def accept_connections(sock: socket.socket):
    while True:
        conn, addr = sock.accept()
        connections.append([conn, addr, 0])
        print(connections)

def communicate(conn, addr):
    try:
        while True:
            data = conn.recv(1024)
            if "USERNAME" in str(data):
                usernames.append(str(data).split(":")[1].split("\'")[0])
                print(usernames)
                for connection in connections:
                    connection[0].sendall(bytes(str("USERNAMES:") + str(usernames), encoding="ascii"))
                    continue
            for connection in connections:
                if connection[0] == conn:
                    user = str(usernames[connections.index(connection)])
            for connection in connections:
                connection[0].sendall(bytes(user + ": " + str(data), encoding="ascii"))
    except socket.error as e:
        print(e)
        for connection in connections:
            if connection[1] == addr:
                connections.pop(connections.index(connection))
                # TODO: remove the fucking user from userlist too lol


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost",5678))
    sock.listen()
    list_of_threads = []
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
        exit(1)
    

    