from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.require import require
from org.pyvereign.util.decorators.pre_condition import pre_condition
from org.pyvereign.environment.instrumentation.hardware.default_hardware import DefaultHardware
from org.pyvereign.error.illegal_argument_error import IllegalArgumentError

class Battery(DefaultHardware):
    
    def __init__(self):
        DefaultHardware.__init__(self)
        self.setEstimatedChargeRemaining(0)
    
    @public
    @return_type(int)    
    def getEstimatedChargeRemaining(self):
        return self.__charge
    
    @public
    @return_type(int)
    @pre_condition("charge", lambda charge: (charge >= 0 and charge <= 100), IllegalArgumentError, "Invalid charge value for battery.")
    @require("charge", int)
    def setEstimatedChargeRemaining(self, charge):
        if isinstance(charge, bool):
            raise TypeError()
        self.__charge = charge
        return self.__charge