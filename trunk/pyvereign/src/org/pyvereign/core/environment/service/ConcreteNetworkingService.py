from org.pyvereign.core.environment.service.AbstractNetworkingService import AbstractNetworkingService

class ConcreteNetworkingService(AbstractNetworkingService):
    """
    Defines the concrete implementation of AbstractNetworkingService class.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, implementation):
        """
        Initializes the ConcreteNetworkingService objects.

        @param implementation: implementation of service
        @type implementation: L{NetworkingService}
        @rtype: None
        """
        self._implementation = implementation
    
    def initialize(self, owner, id, context):
        self._implementation.initialize(owner, id, context)
    
    def start(self, *params):
        self._implementation.start(*params)
    
    def stop(self):
        self._implementation.stop()
    
    def getStatus(self):
        return self._implementation.getStatus()
    
    def getID(self):
        return self._implementation.getID()
    
    def getOwner(self):
        return self._implementation.getOwner()
    
    def addModule(self, id, module):
        return self._implementation.addModule(id, module)
        
    def removeModule(self, id):
        return self._implementation.removeModule(id)
    
    def countModules(self):
        return self._implementation.countModules()
    
    def clearModules(self):
        self._implementation.clearModules()
    
    def isComposite(self):
        return self._implementation.isComposite()
    
    def getName(self):
        return self._implementation.getName()
   
    def getContext(self):
        return self._implementation.getContext()   
    
    def getNetworkProtocols(self):
        return self._implementation.getNetworkProtocols()
    