from atlas.api.env.transport.communicationapi.AbstractCommunicationAPI import AbstractCommunicationAPIAdapter
import socket

class DatagramSocketAdapter(AbstractCommunicationAPIAdapter):
    
    def __init__(self):
        self.initialize()
    
    def open(self, inetAddress):
        self.__socket = socket.socket(inetAddress.getFamily(), socket.SOCK_DGRAM)
        AbstractCommunicationAPIAdapter.open(self, inetAddress)
        return self._inetAddress
    
    def close(self):
        if self.__socket:
            self.__socket.close()
        return True