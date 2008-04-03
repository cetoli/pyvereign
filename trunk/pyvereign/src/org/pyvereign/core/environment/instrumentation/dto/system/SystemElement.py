class SystemElement(object):
    """
    Defines the common interface of sytem elements. 
    
    @author: Fabricio
    @since: 28/03/2008 - 14:26:13
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getName(self):
        """
        Gets the name of system element.
        @return: Returns the name of system element.
        @rtype: str
        """
        pass
    