class Receiver(object):
    """
    Defines the interface of stream receiver objects.
    
    @author: Fabricio
    @since: 
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def open(self):
        """
        Creates an communication api object.
        
        @return: Returns true if receiver was opened.
        @rtype: bool
        """
        pass
    
    def bind(self):
        """
        Binds the receiver object to a local address.
        
        @return: Returs true if its binded.
        @rtype: bool
        """
        pass
    
    def close(self):
        """
        Closes the receiver object.
        
        @return: Returns true if its closed.
        @rtype: bool
        """
        pass
    
    def receive(self, bufferSize):
        """
        Receives a stream from communication api object.
        
        @return: Returns a stream.
        @rtype: str
        """
        pass
    
    def reuseAddress(self, flag):
        """
        Configure the receiver of StreamListener to reuse the local address whether true.
        
        @return: Returns true if the receiver of StreamListener was configured.
        @rtype: bool
        """
        pass
    
    def isReusingAddress(self):
        """
        Verifies if receivers is reusing InetAddress.
        
        @return: Returns true if receivers is reusing InetAddress.
        @rtype: bool
        """
        pass
    
    def getInetAddress(self):
        """
        Gets the inet address of forwarder object.
        
        @return: Returns the inet address of forwarder object.
        @rtype: L{InetAddress}
        """
        pass
    
    def getProtocol(self):
        """
        Gets the network protocol used by forwarder.
        
        @return: Returns the network protocol used by forwarder.
        @rtype: L{NetworkProtocol}
        """
        pass