from org.pyvereign.core.platform.Service import Service

class TransportService(Service):
    """
    Defines the interface for tranport service. 
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def sendStream(self, protocolName, inetAddress, stream, broadcasting, timeout):
        """
        Sends a stream over a network protocol.
        
        @param protocolName: the name of network protocol.
        @type protocolName: str
        @param inetAddress: an InetAddress object.
        @type inetAddress: L{InetAddress}
        @param stream: a data stream
        @type stream: str
        @param broadcasting: a flag to configure the transmission mode.
        @type broadcasting: bool
        @param timeout: the timeout of transmission.
        @type timeout: int
        @return: Returns a stream has sended.
        @rtype: str
        """
        pass
    
    def addTransportListener(self, protocolName, uri, listener):
        """
        Adds a transport listener object in map of stream listeners.
        
        @param protocolName: the transport protocol of transport listener.
        @type protocolName: str
        @param uri: a uri to map stream listener.
        @type uri: str
        @param listener: a TransportListener object.
        @type listener: L{TransportListener}
        
        @return: Returns the TransportListener object mapped in the map of TransportListeners.
        @rtype: L{TransportListener}
        """
        pass
    
    def removeTransportListener(self, protocolName, uri):
        """
        Removes the listener has mapped by using uri.
        @param protocolName: the transport protocol of transport listener.
        @type protocolName: str
        @param uri: a uri to map stream listener.
        @type uri: str
        @return: Returns the TransportListener object mapped in the map of TransportListeners.
        @rtype: L{TransportListener}
        """
        pass
    
    def getTransportListener(self, protocolName, uri):
        """
        Gets the listener has mapped by using uri.
        @param protocolName: the transport protocol of transport listener.
        @type protocolName: str
        @param uri: a uri to map stream listener.
        @type uri: str
        @return: Returns the TransportListener object mapped in the map of TransportListeners.
        @rtype: L{TransportListener}
        """
        pass
    
    def getNumberOfTransportListeners(self):
        """
        Gets the number of transport listeners.
        
        @return: the number of transport listeners.
        @rtype: int
        """
        pass
        