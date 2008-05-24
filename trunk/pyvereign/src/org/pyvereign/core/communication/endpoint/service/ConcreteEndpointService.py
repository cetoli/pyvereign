from org.pyvereign.core.communication.endpoint.service.AbstractEndpointService import AbstractEndpointService

class ConcreteEndpointService(AbstractEndpointService):
    
    def __init__(self, implementation):
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
    
    def addEndpointListener(self, uri, listener):
        return self._implementation.addEndpointListener(uri, listener)
    
    def removeEndpointListener(self, uri):
        return self._implementation.removeEndpointListener(uri)
    
    def getEndpointListener(self, uri):
        return self._implementation.getEndpointListener(uri)
    
    def hasEndpointListener(self, uri):
        return self._implementation.hasEndpointListener(uri)
    
    def createEndpointMessage(self, origin, destination, event = None):
        return self._implementation.createEndpointMessage(origin, destination, event)
    
    def createEndpointAddress(self, uri):
        return self._implementation.createEndpointAddress(uri)
    
    def getMessageSender(self, endpointAddress):
        return self._implementation.getMessageSender(endpointAddress)
    
    def getEndpointProtocolByName(self, name):
        return self._implementation.getEndpointProtocolByName(name)
    
    def getEndpointProtocols(self):
        return self._implementation.getEndpointProtocols()