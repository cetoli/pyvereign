
class Service(object):
    """
    Defines the common interface for platform services.
    
    @author: Fabricio
    @since: 18/03/2008 - 14:03:01
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getContext(self):
        """
        Gets the context information of service.
        
        @return: The context information of service.
        @rtype: L{Context}
        """
        pass
        
    