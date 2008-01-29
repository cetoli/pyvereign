from atlas.api.env.transport.communicationapi.AbstractCommunicationAPIAdapter import AbstractCommunicationAPIAdapter
import socket

class DatagramSocketAdapter(AbstractCommunicationAPIAdapter):
    
    def __init__(self, inetAddress):
        self.initialize()
        self._inetAddress = inetAddress
        self.__socket = socket.socket(inetAddress.getFamily(), socket.SOCK_DGRAM)
    
    def supportBroadcasting(self, value):
        if value:
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        else:
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)
        return value
    
    def isSupportingBroadcasting(self):
        return self.__socket.getsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST) == 1
    
    def reuseAddress(self, value):
        if value:
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        else:
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        return value
    
    def isReusingAddress(self):
        return self.__socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) == 1
    
    def close(self):
        if self.__socket:
            self.__socket.close()
        return True
    
    def send(self, stream):
        self.__socket.sendto(stream, self._inetAddress.getTuple())
        return stream
    
    def open(self):
        self.__socket.bind(self._inetAddress.getTuple())
        return True
    
    def receive(self, bufferSize):
        print self._inetAddress.getTuple()
        return self.__socket.recvfrom(bufferSize)