import socket

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sckt.bind(("", 5050))

while True:
    stream, addr = sckt.recvfrom(2048)
    if stream:
        print stream