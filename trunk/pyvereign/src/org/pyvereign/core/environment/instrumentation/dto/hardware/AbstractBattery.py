from org.pyvereign.core.environment.instrumentation.dto.hardware.Battery import Battery
from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractHardware import AbstractHardware

class AbstractBattery(Battery, AbstractHardware):
    """
    Defines the common implementation for Battery objects. 
    
    @author: Fabricio
    @since: 28/03/2008 - 17:08:10
    @version: 0.0.1
    """
    
    def init(self, values):
        self._estimatedChargeRemaining = 0
        """
        @ivar: the estimated charge remaining of battery.
        @type: int
        """
        AbstractHardware.init(self, values)
        
        if values.has_key("estimatedChargeRemaining"):
            self._estimatedChargeRemaining = values["estimatedChargeRemaining"]
    
    def getEstimatedChargeRemaining(self):
        """
        Gets the estimated charge remaining of battery.
        @return: Returns the estimated charge remaining of battery.
        @rtype: int
        """
        return self._estimatedChargeRemaining