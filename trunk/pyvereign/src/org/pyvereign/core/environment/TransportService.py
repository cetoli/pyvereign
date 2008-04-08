class TransportService(object):
    """
    Defines the interface of transport services.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
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
        pass
    
    def addTransportListener(self, protocolName, uri, listener):
        pass
    
    def removeTransportListener(self, protocolName, uri):
        pass
    
    def getTransportListener(self, protocolName, uri):
        pass
    
    def getNumberOfTransportListeners(self):
        pass
    
    