from atlas.api.com.endpoint.address.EndpointAddress import EndpointAddress

class EndpointMessage(object):
    
    def __init__(self, origin, destination):
        if not origin:
            raise RuntimeError("origin parameter is none.")
        if not destination:
            raise RuntimeError("destination parameter is none.")
        if not isinstance(origin, EndpointAddress):
            raise TypeError("The origin parameter is not an instance of EndpointAddress class.")
        if not isinstance(destination, EndpointAddress):
            raise TypeError("The destination parameter is not an instance of EndpointAddress class.")
        
        self._origin = origin
        self._destination = destination
        self._data = {}
        
    def getOrigin(self):
        return self._origin