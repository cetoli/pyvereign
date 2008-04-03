class NetworkingElement(object):
    """
    Defines the common interface for networking elements.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getName(self):
        """
        Gets the name of networking element.
        @return: Returns the name of networking element.
        @rtype: str
        """
        pass
    