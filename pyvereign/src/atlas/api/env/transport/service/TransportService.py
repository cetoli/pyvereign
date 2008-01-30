from atlas.api.env.EnvironmentService import EnvironmentService

class TransportService(EnvironmentService):
    
    def __init__(self):
        raise NotImplementedError()
    
    def sendStream(self, stream, protocolName, inetAddress):
        pass
    
    def receiveStream(self, protocolName, inetAddress):
        pass
    
