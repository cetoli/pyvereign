from atlas.api.env.EnvironmentService import EnvironmentService

class TransportService(EnvironmentService):
    
    def __init__(self):
        raise NotImplementedError()
    
    def sendStream(self, protocolName, inetAddress, stream, broadcasting, timeout):
        pass
    
    def addTransportListener(self, protocolName, uri, listener):
        pass
    
    def removeTransportListener(self, protocolName, uri):
        pass
    
    def getTransportListener(self, protocolName, uri):
        pass
    
    def getNumberOfTransportListeners(self):
        pass
    
    def getProtocols(self):
        pass
    
    
    
    
