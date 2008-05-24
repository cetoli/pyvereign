class ProcessDAO(object):
    """
    Defines the common interface for data access object for SO processes. 
    
    @author: Fabricio
    @since: 28/03/2008 - 16:46:21
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveProcesses(self):
        """
        Retrieves processes which are running on the user computer.
        @return: Returns processes which are running on the user computer.
        @rtype: ImmutableSet
        """
        pass
        
    