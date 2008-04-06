import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sckt.bind(("", 5050))
sckt.listen(1)

while True:
    s, addr = sckt.accept()
    stream = s.recv(2048)
    if stream:
        print stream