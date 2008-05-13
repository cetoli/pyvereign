from org.pyvereign.core.environment.transport.address.InetAddressFactory import InetAddressFactory
class EndpointAddress(object):
    """
    Defines the address for endpoints in platform.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, protocol, ipAddress, port, service = "", action = "", parameter = ""):
        """
        Initializes the EndpointAddress object.
        
        @param protocol: the protocol of endpoint address.
        @type protocol: str
        @param ipAddress: the ipAddress of endpoint address.
        @type ipAddress: str
        @param port: port of endpoint address.
        @type port: int
        @param service: the service name of endpoint address.
        @type service: str
        @param action: the action name of endpoint address.
        @type action: str
        @param parameter: the parameter of endpoint address.
        @type parameter: str
        @rtype: None
        """
        if not isinstance(protocol, str):
            raise TypeError("The protocol parameter is not an instance of str class")
        if not isinstance(ipAddress, str):
            raise TypeError("The ipaddress parameter is not an instance of str class")
        if not isinstance(port, int):
            raise TypeError("The port parameter is not an instance of int class")
        if not isinstance(service, str):
            raise TypeError("The service parameter is not an instance of str class")
        if not isinstance(action, str):
            raise TypeError("The action parameter is not an instance of str class")
        if not isinstance(parameter, str):
            raise TypeError("The parameter of endpoint address is not an instance of str class")
        if port < 1:
            raise RuntimeError("Invalid port.")
        
        self._protocol = protocol
        """
        @ivar: the protocol of endpoint address.
        @type: str  
        """
        self._ipAddress = ipAddress
        """
        @ivar: the ip address of endpoint address.
        @type: str 
        """
        self._port = port
        """
        @ivar: the port of endpoint address.
        @type: int 
        """
        self._service = service
        """
        @ivar: the service name of endpoint address.
        @type: str  
        """
        self._action = action
        """
        @ivar: the action of endpoint address.
        @type: str  
        """
        self._parameter = parameter
        """
        @ivar: the paraemeter name
        @type: str  
        """
    
    def getProtocol(self):
        """
        Gets the protocol of endpoint address.
        @return: Returns the protocol of endpoint address.
        @rtype: str
        """
        return self._protocol
    
    def getIPAddress(self):
        """
        Gets the ip address of endpoint address.
        @return: Returns the ip address of endpoint address.
        @rtype: str
        """
        return self._ipAddress
    
    def getPort(self):
        """
        Gets the port of endpoint address.
        @return: Returns the port of endpoint address.
        @rtype: int
        """
        return self._port
    
    def getService(self):
        """
        Gets the service of endpoint address.
        @return: Returns the service of endpoint address.
        @rtype: str
        """
        return self._service
    
    def getAction(self):
        """
        Gets the action of endpoint address.
        @return: Returns the action of endpoint address.
        @rtype: str
        """
        return self._action
    
    def getParameter(self):
        """
        Gets the paramenter of endpoint address.
        @return: Returns the paramenter of endpoint address.
        @rtype: str
        """
        return self._parameter
    
    def toURI(self):
        """
        Gets an URI string.
        @return: Returns an URI string.
        @rtype: str
        """
        uri = self._protocol + "://"+self._ipAddress+":"+str(self._port)+"/"+self._service
        if self._action <> "" and self._action <> None:
            uri += "/" + self._action
        if self._parameter <> "" and self._parameter <> None:
            uri += "/" + self._parameter
        return uri
    
    def getEndpointAddress(self, uri):
        """
        Creates an EndpointAddress object by using uri parameter.
        @return: Returns an EndpointAddress object by using uri parameter.
        @rtype: L{EndpointAddress}
        """
        if not isinstance(uri, str):
            raise RuntimeError("the uri parameter is not an instance of str class.")
        
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
        elif len(v) == 6:
            address = EndpointAddress(protocol, ip, port, v[3], v[4], v[5])
        
        return address
    
    getEndpointAddress = classmethod(getEndpointAddress)
    
    def getInetAddress(self):
        if self._ipAddress == "<broadcast>":
            return InetAddressFactory.createBroadcastAddress(self._port)
        return InetAddressFactory.createInetAddress(self._ipAddress, self._port)
        