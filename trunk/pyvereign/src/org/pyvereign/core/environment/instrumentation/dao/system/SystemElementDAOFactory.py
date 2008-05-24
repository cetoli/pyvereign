class SystemElementDAOFactory(object):
    """
    Defines the common interface for SystemElementDAOFactory objects. 
    
    @author: Fabricio
    @since: 29/03/2008 - 16:50:31
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def createProcessDAO(self):
        """
        Creates an instance of ProcessDAO
        @return: Returns an instance of ProcessDAO
        @rtype: L{ProcessDAO}
        """
        pass
    