import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 5050))
    while True:
        data, addr = sock.recvfrom(1024)
        if data:
            print data, addr
except socket.error, e:
    print e
    sock.close()