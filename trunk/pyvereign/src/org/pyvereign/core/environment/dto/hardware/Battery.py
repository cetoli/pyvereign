from org.pyvereign.core.environment.dto.hardware.Hardware import Hardware

class Battery(Hardware):
    """
    Defines the interface for Battery objects. 
    
    @author: Fabricio
    @since: 28/03/2008 - 16:56:07
    @version: 0.0.1
    """
    
    def getEstimatedChargeRemaining(self):
        """
        Gets the estimated charge remaining of battery.
        @return: Returns the estimated charge remaining of battery.
        @rtype: int
        """
        pass
    