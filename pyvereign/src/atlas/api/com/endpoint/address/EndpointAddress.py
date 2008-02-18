from atlas.api.exception.EndpointAddressError import EndpointAddressError
from atlas.util.InetAddressFactory import InetAddressFactory

class EndpointAddress(object):
    
    def __init__(self, protocol, ipaddress, port, service = "", parameters = ""):
        
        if not protocol:
            raise RuntimeError("Invalid protocol.")
        if not ipaddress:
            raise RuntimeError("Invalid IP Address.")
        if not port:
            raise RuntimeError("Invalid port.")
        if service == None:
            raise RuntimeError("Invalid service.")
        if parameters == None:
            raise RuntimeError("Invalid parameters.")
        
        if not isinstance(protocol, str):
            raise TypeError("The protocol parameter is not an instance of str class")
        if not isinstance(ipaddress, str):
            raise TypeError("The ipaddress parameter is not an instance of str class")
        if not isinstance(port, int):
            raise TypeError("The port parameter is not an instance of int class")
        if not isinstance(service, str):
            raise TypeError("The service parameter is not an instance of str class")
        if not isinstance(parameters, str):
            raise TypeError("The parameters parameter is not an instance of str class")
        
        if port < 1:
            raise RuntimeError("Invalid port.")
        
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
    
    def getInetAddress(self):
        if self._ipaddress == "<broadcast>":
            print "OOLA"
            return InetAddressFactory.createBroadcastAddress(self._port)
        return InetAddressFactory.createInetAddress(self._ipaddress, self._port)