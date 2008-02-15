from atlas.api.exception.EndpointAddressError import EndpointAddressError
class EndpointAddress(object):
    
    def __init__(self, protocol, ipaddress, port, service = "", parameters = ""):
        
        from atlas.api.microkernel.Microkernel import Microkernel
        
        if not Microkernel().executeMecanism("Environment", "protocol", "hasProtocol", protocol):
            raise EndpointAddressError("Protocol not found.")
        
        self._protocol = protocol
        self._ipaddress = ipaddress
        self._port = port
        self._service = service
        self._parameters = parameters
    
    def getProtocol(self):
        return self._protocol
    
    def getIPAddress(self):
        return self._ipaddress
    
    def getPort(self):
        return self._port
    
    def getService(self):
        return self._service
    
    def getParameters(self):
        return self._parameters
    
    def toURI(self):
        uri = self._protocol + "://" + self._ipaddress + ":" + str(self._port)
        
        if not self._service == "":
            uri += "/" + self._service 
            
        if not self._parameters == "":
            uri += "/" + self._parameters
        
        return uri
    
    def toEndpointAddress(self, uri):
        address = None
        
        v = uri.split("/")
        
        protocol = v[0].split(":")[0]
        ip = v[2].split(":")[0]
        port = int(v[2].split(":")[1])
        if len(v) == 3:
            address = EndpointAddress(protocol, ip, port)
        elif len(v) == 4:
            address = EndpointAddress(protocol, ip, port, v[3])
        elif len(v) == 5:
            address = EndpointAddress(protocol, ip, port, v[3], v[4])
        print v
        
        return address
    
    toEndpointAddress = classmethod(toEndpointAddress)