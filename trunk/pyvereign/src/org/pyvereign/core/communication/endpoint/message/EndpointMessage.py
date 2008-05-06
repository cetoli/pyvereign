from org.pyvereign.core.communication.format.FormatableObject import FormatableObject
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.core.exception.FormatableObjectError import FormatableObjectError

class EndpointMessage(FormatableObject):
    """
    Defines the implementation of endpoint message.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, origin = None, destination = None, event = None):
        """
        Initializes the EndpointMessage object.
        @param origin: the origin of message
        @type origin: L{EndpointAddress}
        @param destination: the destination of message
        @type destination: L{EndpointAddress}
        @param event: an event
        @type event: type
        """
        if origin and not isinstance(origin, EndpointAddress):
            raise TypeError("The origin parameter is not an instance of EndpointAddress class.")
        if destination and not isinstance(destination, EndpointAddress):
            raise TypeError("The destination parameter is not an instance of EndpointAddress class.")
        
        self._origin = origin
        """
        @param: the origin of message
        @type: L{EndpointAddress} 
        """
        self._destination = destination
        """
        @param: the destination of message
        @type: L{EndpointAddress} 
        """
        self._event = event
        """
        @param: the event of message
        @type: type
        """
    
    def getOrigin(self):
        """
        Gets the origin of message.
        @return: Returns the origin of message.
        @rtype: L{EndpointAddress}
        """
        return self._origin
    
    def getDestination(self):
        """
        Gets the destination of message.
        @return: Returns the origin of message.
        @rtype: L{EndpointAddress}
        """
        return self._destination
    
    def getEvent(self):
        """
        Gets the event of message.
        @return: Returns the event of message.
        @rtype: type
        """
        return self._event
    
    def getValues(self):
        values = {}
        if (not self._origin) or (not self._origin):
            raise FormatableObjectError()
        values["origin"] = self._origin.toURI()
        values["destination"] = self._destination.toURI()
        
        return values
    
    def setValues(self, values):
        if not isinstance(values, dict):
            raise TypeError()
        if not values.has_key("origin"):
            raise FormatableObjectError()
        if not values.has_key("destination"):
            raise FormatableObjectError() 
        self._origin = EndpointAddress.getEndpointAddress(values["origin"])
        self._destination = EndpointAddress.getEndpointAddress(values["destination"])
        
        return values
    
    