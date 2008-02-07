from atlas.api.env.transport.service.AbstractTransportService import AbstractTransportService
from atlas.api.microkernel.Microkernel import Microkernel
from atlas.api.env.transport.forwarder.ForwarderFactory import ForwarderFactory
from atlas.api.env.transport.address.InetAddress import InetAddress

class DefaultTransportService(AbstractTransportService):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self, *params):
        AbstractTransportService.initialize(self)
        
    def sendStream(self, protocolName, inetAddress, stream, broadcasting = False):
        if not protocolName:
            raise RuntimeError("protocolName parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("protocolName parameter is not an instance of str class.")
        if not inetAddress:
            raise RuntimeError("inetAddress parameter is none.")
        if not isinstance(inetAddress, InetAddress):
            raise TypeError("inetAddress parameter is not an instance of InetAddress class.")
        if not stream:
            raise RuntimeError("stream parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("stream parameter is not an instance of str class.")
        if broadcasting == None:
            raise RuntimeError("broadcasting parameter is none.")
        if not isinstance(protocolName, str):
            raise TypeError("broadcasting parameter is not an instance of bool class.")
        protocol = Microkernel().executeMecanism("Environment", "protocol", "getProtocol", protocolName)
        forwarder = ForwarderFactory().createForwarder(protocolName, inetAddress, protocol)
        try:
            try:
                forwarder.open()
                forwarder.supportBroadcasting(broadcasting)
                return forwarder.send(stream)
            except:
                raise
        finally:
            forwarder.close()