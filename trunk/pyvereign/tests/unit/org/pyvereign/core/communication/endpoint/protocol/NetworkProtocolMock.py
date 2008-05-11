from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocol import NetworkProtocol
import pmock

class NetworkProtocolMock(NetworkProtocol, pmock.Mock):
    
    def __init__(self, name = ""):
        pmock.Mock.__init__(self, name)