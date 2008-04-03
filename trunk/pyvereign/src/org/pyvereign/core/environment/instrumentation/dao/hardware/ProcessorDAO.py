class ProcessorDAO(object):
    """
    Defines the interface of processor data access object. 
    
    @author: Fabricio
    @since: 25/03/2008 - 11:50:12
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveProcessors(self):
        """
        Retrieves processor that are installed in user machine.
        @return: Returns processor that are installed in user machine.
        @rtype: list
        """
        pass
    