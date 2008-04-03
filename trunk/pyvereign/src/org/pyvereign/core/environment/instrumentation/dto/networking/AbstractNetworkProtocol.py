from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocol import NetworkProtocol
from org.pyvereign.core.environment.instrumentation.dto.networking.AbstractNetworkingElement import AbstractNetworkingElement

class AbstractNetworkProtocol(NetworkProtocol, AbstractNetworkingElement):
    """
    Defines the common implementation for network protocol objects. 
    
    @author: Fabricio
    @since: 31/03/2008 - 01:22:33
    @version: 0.0.1
    """
    
    def init(self, values):
        self._supportsBroadcasting = False
        """
        @ivar: defines if protocol supports broadcasting.
        @type: bool
        """
        self._supportsMulticasting = False
        """
        @ivar: defines if protocol supports multcasting.
        @type: bool
        """
        self._guaranteesDelivery = False
        """
        @ivar: defines if protocol guarantees the delivery of packet.
        @type: bool
        """
        self._type = -1
        """
        @ivar: the type of protocol.
        @type: int  
        """
        AbstractNetworkingElement.init(self, values)
        
        
        if values.has_key("name"):
            self._name = values["name"]
        
        if values.has_key("supportsBroadcasting"):
            self._supportsBroadcasting = values["supportsBroadcasting"]
        
        if values.has_key("supportsMulticasting"):
            self._supportsMulticasting = values["supportsMulticasting"]
            
        if values.has_key("guaranteesDelivery"):
            self._guaranteesDelivery = values["guaranteesDelivery"]
    
    def supportsBroadcasting(self):
        """
        Gets if protocol supports broadcast operation.
        @return: Returns if protocol supports broadcast operation.
        @rtype: bool
        """
        return self._supportsBroadcasting
    
    def guaranteesDelivery(self):
        """
        Verifies if protocol offers guarantee of delivery.
        @return: Returns if protocol offers guarantee of delivery.
        @rtype: bool
        """
        return self._guaranteesDelivery
    
    def supportsMulticasting(self):
        """
        Gets if protocol supports multicast operation.
        @return: Returns if protocol supports broadcast operation.
        @rtype: bool
        """
        return self._supportsMulticasting