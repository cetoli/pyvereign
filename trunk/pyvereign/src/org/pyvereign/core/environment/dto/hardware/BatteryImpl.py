from org.pyvereign.core.environment.dto.hardware.AbstractBattery import AbstractBattery

class BatteryImpl(AbstractBattery):
    """
    Defines the default implementation of AbstractBattery class. 
    
    @author: Fabricio
    @since: 29/03/2008 - 09:44:39
    @version: 0.0.1
    """
    
    def __init__(self, values):
        self.init(values)