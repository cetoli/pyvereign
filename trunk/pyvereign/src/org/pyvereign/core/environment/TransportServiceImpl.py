from org.pyvereign.core.environment.AbstractTransportService import AbstractTransportService

class TransportServiceImpl(AbstractTransportService):
    """
    Defines a concrete implementation of AbstractTranportService class.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, implementation):
        """
        Initializes the transport service implementation.
        
        @param implementation: the implementation of service.
        @type implementation: L{TransportService}
        """
        self._implementation = implementation
    
    def sendStream(self, protocolName, inetAddress, stream, broadcasting, timeout):
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
        return self._implementation.sendStream(protocolName, inetAddress, stream, broadcasting, timeout)
    
    def getInterface(self, type = None):
        return self._implementation