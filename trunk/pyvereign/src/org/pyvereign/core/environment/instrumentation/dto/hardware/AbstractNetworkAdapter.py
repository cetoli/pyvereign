from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractHardware import AbstractHardware
from org.pyvereign.core.environment.instrumentation.dto.hardware.NetworkAdapter import NetworkAdapter

class AbstractNetworkAdapter(AbstractHardware, NetworkAdapter):
    """
    Defines the common implementation  
    
    @author: Fabricio
    @since: 29/03/2008 - 18:24:40
    @version: 0.0.1
    """
    
    def init(self, values):
        self._speed = 0
        """
        @ivar: the speed of network adapter.
        @type: int  
        """
        self._macAddress = ""
        """
        @ivar: the MAC Address of network adapter.
        @type: str
        """
        self._ipAddress = ""
        """
        @ivar: the IP address of network adapter.
        @type: str  
        """
        AbstractHardware.init(self, values)
        
        if values.has_key("speed"):
            self._speed = values["speed"]
        
        if values.has_key("macAddress"):
            self._macAddress = values["macAddress"]
        
        if values.has_key("ipAddress"):
            self._ipAddress = values["ipAddress"]
            
    def getSpeed(self):
        """
        Gets the speed of network adapter.
        @return: Returns the speed of network adapter.
        @rtype: int
        """
        return self._speed
    
    def getMACAddress(self):
        """
        Gets the mac addresses of network adapter.
        @return: Returns the mac addresses of network adapter.
        @rtype: str
        """
        return self._macAddress
    
    def getIPAddress(self):
        """
        Gets the IP address of network adapter
        @return: Returns the IP address of network adapter
        @rtype: str
        """
        return self._ipAddress