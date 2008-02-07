from atlas.api.env.transport.forwarder.AbstractForwarder import AbstractForwader
from atlas.api.env.transport.address.InetAddress import InetAddress
from atlas.api.env.networking.Protocol import Protocol
from atlas.api.exception.TransportError import TransportError
import socket

class StreamForwarder(AbstractForwader):
    
    def __init__(self, inetAddress, protocol):
        self.initialize()
        if not inetAddress:
            raise RuntimeError("inetAddress parameter is none.")
        if not isinstance(inetAddress, InetAddress):
            raise TypeError("inetAddress parameter is not instance of InetAddress class.")
        if inetAddress.isBroadcastAddress():
            raise TransportError("Stream forwarder not support broadcasting.")
        self._inetAddress = inetAddress
        if not protocol:
            raise RuntimeError("protocol parameter is none.")
        if not isinstance(protocol, Protocol):
            raise TypeError("protocol parameter is not an instance of Protocol class.")
        self._protocol = protocol
    
    def open(self):
        try:
            self._socket = socket.socket(self._inetAddress.getFamily(), socket.SOCK_STREAM)
            self._opened = True
            return self._opened
        except socket.error, e:
            raise TransportError(e.message)
    
    def send(self, stream):
        AbstractForwader.send(self, stream)
        if not self._opened:
            raise TransportError("Stream forwarder is not opened.")
        try:
            self._socket.connect(self._inetAddress.getTuple())
            self._socket.send(stream)
            return stream
        except socket.error, e:
            raise TransportError(e.message)