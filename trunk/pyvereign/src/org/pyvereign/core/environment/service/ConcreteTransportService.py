from org.pyvereign.core.environment.service.AbstractTransportService import AbstractTransportService

class ConcreteTransportService(AbstractTransportService):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def __init__(self, implementation):
        """
        Initializes the ConcreteTransportService objects.

        @param implementation: implementation of service
        @type implementation: L{TransportService}
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
    
    def sendStream(self, protocolName, inetAddress, stream, broadcasting = False, timeout = 0):
        return self._implementation.sendStream(protocolName, inetAddress, stream, broadcasting, timeout)
    
    def addTransportListener(self, protocolName, uri, listener):
        return self._implementation.addTransportListener(protocolName, uri, listener)
    
    def removeTransportListener(self, protocolName, uri):
        return self._implementation.removeTransportListener(protocolName, uri)
    
    def getTransportListener(self, protocolName, uri):
        return self._implementation.getTransportListener(protocolName, uri)
    
    def getNumberOfTransportListeners(self):
        return self._implementation.getNumberOfTransportListeners()