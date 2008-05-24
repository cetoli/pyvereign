class PhysicalMemoryDAO(object):
    """
    Defines the interface for retrieving physical memory information. 
    
    @author: Fabricio
    @since: 25/03/2008 - 11:55:27
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrievePhysicalMemories(self):
        """
        Retrieves physical memories which are installed in user machine.
        @return: Returns physical memories which are installed in user machine.
        @rtype: ImmutableSet
        """
        pass
    