class Forwarder(object):
    """
    Defines the interface of objects which send streams over a computer network.
    
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def open(self):
        """
        Opens a connection with a destination of stream.
        
        @return: Returs true if the connection with a destination of system was successful.
        @rtype: bool
        """
        pass
    
    def close(self):
        """
        Closes a connection with a destination of stream.
        
        @return: Returns true if connection with a destination of stream was closed.
        @rtype: bool
        """
        pass
    
    def send(self, stream):
        """
        Sends a stream for its destination.
        
        @return: Returns the sended stream.
        @rtype: str
        """
        pass
    
    def supportBroadcasting(self, flag):
        """
        Configure the forwarder object for broadcast mode whether true.
        
        @return: Returns true if the forwarder object supports the broadcast mode.
        @rtype: bool
        """
        pass
    
    def isSupportingBroadcasting(self):
        """
        Verifies if forwarder object is in broadcast mode.
        
        @return: Returns true if the forwarder object is in broadcast mode.
        @rtype: bool
        """
        pass
    
    def hasSupportToBroadcasting(self):
        """
        Verifies if forwarder object supports the broadcast mode.
        
        @return: Returns true if the forwarder object supports the broadcast mode.
        @rtype: bool
        """
        pass
    
    def getProtocol(self):
        """
        Gets the network protocol used by forwarder.
        
        @return: Returns the network protocol used by forwarder.
        @rtype: L{NetworkProtocol}
        """
        pass
    
    def getInetAddress(self):
        """
        Gets the inet address of forwarder object.
        
        @return: Returns the inet address of forwarder object.
        @rtype: L{InetAddress}
        """
        pass
    
    def setTimeout(self, timeout):
        """
        Sets the timeout for forwarder object.
        
        @return: Returns the timeout for forwarder object.
        @rtype: int
        """
        pass
    
    def getTimeout(self):
        """
        Gets the timeout for forwarder object.
        
        @return: Returns the timeout for forwarder object.
        @rtype: int
        """
        pass