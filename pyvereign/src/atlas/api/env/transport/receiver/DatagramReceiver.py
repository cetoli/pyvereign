from atlas.api.env.transport.receiver.AbstractReceiver import AbstractReceiver
from atlas.api.env.transport.address.InetAddress import InetAddress
from atlas.api.env.networking.Protocol import Protocol
from atlas.api.exception.TransportError import TransportError
from atlas.api.exception.BindError import BindError
import socket

class DatagramReceiver(AbstractReceiver):
    
    def __init__(self, inetAddress, protocol):
        self.initialize()
        if not inetAddress:
            raise RuntimeError("inetAddress parameter is none.")
        if inetAddress.isBroadcastAddress():
            raise TransportError("Invalid address.")
        if not isinstance(inetAddress, InetAddress):
            raise TypeError("inetAddress parameter is not instance of InetAddress class.")
        self._inetAddress = inetAddress
        if not protocol:
            raise RuntimeError("protocol parameter is none.")
        if not isinstance(protocol, Protocol):
            raise TypeError("protocol parameter is not an instance of Protocol class.")
        self._protocol = protocol
    
    def open(self):
        try:
            self._socket = socket.socket(self._inetAddress.getFamily(), socket.SOCK_DGRAM)
            self._opened = True
            return self._opened
        except socket.error, e:
            raise TransportError(e)
        
    def bind(self):
        try:
            self._socket.bind(self._inetAddress.getTuple())
            return True
        except socket.error, e:
            raise BindError(e)
        
    def receive(self, bufferSize = 1024):
        try:
            stream, addr = self._socket.recvfrom(bufferSize)
            return stream
        except socket.error, e:
            raise TransportError(e)