from org.pyvereign.core.environment.AbstractInstrumentationService import AbstractInstrumentationService

class InstrumentationServiceImpl(AbstractInstrumentationService):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def __init__(self, implementation):
        self._implementation = implementation
        
    def getNetworkProtocols(self):
        """
        Gets a list of network protocols.
        @return: Returns a list of network protocols.
        @rtype: list
        """
        return self._implementation.getProtocols()

    def getInterface(self, type = None):
        return self._implementation