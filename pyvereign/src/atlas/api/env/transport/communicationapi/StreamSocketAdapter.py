from atlas.api.env.transport.communicationapi.AbstractCommunicationAPIAdapter import AbstractCommunicationAPIAdapter
import socket

class StreamSocketAdapter(AbstractCommunicationAPIAdapter):
    
    def __init__(self, inetAddress):
        self.initialize()
        self._inetAddress = inetAddress
        self.__socket = socket.socket(inetAddress.getFamily(), socket.SOCK_STREAM)
    
    def supportBroadcasting(self, value):
        raise RuntimeError("Invalid operation")
    
    def isSupportingBroadcasting(self):
        return False
    
    def reuseAddress(self, value):
        if value:
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        else:
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        return value
    
    def isReusingAddress(self):
        return self.__socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) == 1
    
    def open(self):
        self.__socket.bind(self._inetAddress.getTuple())
        self.__socket.listen(1)
        return True
    
    def close(self):
        if self.__socket:
            self.__socket.close()
        return True 
    
    def receive(self, bufferSize):
        conn, addr = self.__socket.accept()
        return conn.recv(bufferSize)
    
    def send(self, stream):
        self.__socket.connect(self._inetAddress.getTuple())
        self.__socket.send(stream)
        return stream
    
    def setTimeOut(self, timeOut):
        self.__socket.settimeout(timeOut)
        return self.__socket.gettimeout()
    
    def getTimeOut(self):
        return self.__socket.gettimeout()