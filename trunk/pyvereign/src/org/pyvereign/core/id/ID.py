class ID(object):
    """
    Defines the identifier interface of platform modules.
    
    @author: Fabricio
    @since: 18/03/2008 - 10:22:40
    @version: 0.0.1
    """
    
    def __init__(self):
        """
        This method is implemented to raise an L{NotImplementedError}, because the ID class denotes an
        interface.
        
        @return: returns an instance of L{NotImplementedError}
        @rtype: L{NotImplementedError}
        """
        raise NotImplementedError()
    
    def getFormatedID(self):
        """
        Gets the formated identifier.
        
        @return: The formated identifier.
        @rtype: L{str}
        """
        pass
    