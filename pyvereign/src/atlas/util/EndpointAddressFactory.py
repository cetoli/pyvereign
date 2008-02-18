from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress

class EndpointAddressFactory(object):
    
    def createEndpointAddress(self, protocol, ipAddress, port, service = "", parameters = ""):
        return EndpointAddress(protocol, ipAddress, port, service, parameters)
    
    def createEndpointBroadcastAddress(self, port, service = "", parameters = ""):
        return EndpointAddress("UDP", "<broadcast>", port, service, parameters)