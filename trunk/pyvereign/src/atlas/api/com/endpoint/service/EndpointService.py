from atlas.api.com.CommunicationService import CommunicationService

class EndpointService(CommunicationService):
    
    def addEndpointListener(self, uri, listener):
        pass
    
    def removeEndpointListener(self, uri):
        pass
    
    def getEndpointListener(self, uri):
        pass
    
    def hasEndpointListener(self, uri):
        pass
    
    def createEndpointMessage(self, origin, destination, event = None):
        pass
    
    def createEndpointAddress(self, uri):
        pass
    
    def getMessageSender(self, endpointAddress, format):
        pass
    
    def getEndpointProtocolByName(self):
        pass
    
    def getEndpointProtocols(self):
        pass