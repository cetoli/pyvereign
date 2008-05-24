from org.pyvereign.util.ClassLoader import ClassLoader
from org.pyvereign.util.Constants import Constants

class EndpointProtocolCreator:
    
    def __init__(self):
        raise NotImplementedError()
    
    def createEndpointProtocol(self, networkProtocol):
        clazz = ClassLoader.loadClass(Constants.ENDPOINT_PROTOCOL_MODULE, Constants.ENDPOINT_PROTOCOL_CLASS)
        return clazz(networkProtocol)
    
    createEndpointProtocol = classmethod(createEndpointProtocol)