from org.pyvereign.core.environment.AbstractTransportService import AbstractTransportService
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.transport.address.InetAddress import InetAddress
from org.pyvereign.core.environment.transport.forwarder.ForwarderFactory import ForwarderFactory
from org.pyvereign.core.exception.TransportError import TransportError

class DefaultTransportService(AbstractTransportService):
    """
    Defines the default implementation of AbstractTransportService class.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
        self._name = Constants.TRANSPORT_SERVICE
    
    def sendStream(self, protocolName, inetAddress, stream, broadcasting = False, timeout = 0):
        """
        Sends a stream over transport protocol.
        @param protocolName: the transport protocol.
        @type protocolName: str
        @param inetAddress: an InetAddress object.
        @type inetAddress: L{InetAddress}
        @param stream: a stream to send
        @type stream: str
        @param broadcasting: indicates if stream will be sended in broadcasting mode.
        @param broadcasting: bool
        @param timeut: timeout value
        @type timeout: int
        @return: Returns a stream over transport protocol.
        @rtype: str
        """
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
        
        forwarder = ForwarderFactory().createForwarder(protocolName, inetAddress, self._protocols[protocolName])
        try:
            try:
                forwarder.open()
                if inetAddress.isBroadcastAddress() and broadcasting == True:
                    forwarder.supportBroadcasting(broadcasting)
                if not inetAddress.isBroadcastAddress() and broadcasting == True:
                    raise TransportError("Invalid configuration for the broadcasting of stream.")
                if timeout > 0:
                    forwarder.setTimeout(timeout)
                elif timeout < 0:
                    raise TransportError("Invalid timeout value.")
                return forwarder.send(stream)
            except:
                raise
        finally:
            forwarder.close()
    