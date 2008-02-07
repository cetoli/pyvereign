import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 5050))
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        if data:
            print data, addr
except socket.error, e:
    print e
    sock.close()