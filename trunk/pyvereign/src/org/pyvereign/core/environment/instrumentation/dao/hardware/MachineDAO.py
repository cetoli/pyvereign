class MachineDAO(object):
    """
    Defines the interface of machine data access object. 
    
    @author: Fabricio
    @since: 25/03/2008 - 11:43:51
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveMachine(self):
        """
        Retrieves the machine information.
        @return: Returns the machine information.
        @rtype: L{Machine}
        """
        pass
    