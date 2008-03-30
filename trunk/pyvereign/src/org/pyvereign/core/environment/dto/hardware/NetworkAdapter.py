from org.pyvereign.core.environment.dto.hardware.Hardware import Hardware

class NetworkAdapter(Hardware):
    """
    Defines the common interface for NetworkAdapter objects. 
    
    @author: Fabricio
    @since: 29/03/2008 - 18:04:53
    @version: 0.0.1
    """
    
    def getSpeed(self):
        """
        Gets the speed of network adapter.
        @return: Returns the speed of network adapter.
        @rtype: int
        """
        pass
    
    def getMACAddress(self):
        """
        Gets the mac addresses of network adapter.
        @return: Returns the mac addresses of network adapter.
        @rtype: str
        """
        pass
    
    def getIPAddress(self):
        """
        Gets the IP address of network adapter
        @return: Returns the IP address of network adapter
        @rtype: str
        """
        pass
    