from org.pyvereign.environment.instrumentation.hardware.default_hardware import DefaultHardware
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.pre_condition import pre_condition
from org.pyvereign.error.illegal_argument_error import IllegalArgumentError
from org.pyvereign.util.decorators.require import require

class PhysicalMemory(DefaultHardware):
    
    def __init__(self):
        DefaultHardware.__init__(self)
        self.setCapacity(0)
        self.setDataWidth(0)
        self.setSpeed(0)
       
    @public
    @return_type(int) 
    def getCapacity(self):
        return self.__capacity
    
    @public
    @return_type(int)
    def getDataWidth(self):
        return self.__dataWidth
    
    @public
    @return_type(int)
    def getSpeed(self):
        return self.__speed
    
    @public
    @return_type(int)
    @pre_condition("capacity", lambda capacity: capacity >= 0, IllegalArgumentError, "Invalid capacity for physical memory.")
    @require("capacity", int)
    def setCapacity(self, capacity):
        if isinstance(capacity, bool):
            raise TypeError()
        self.__capacity = capacity
        return self.__capacity
    
    @public
    @return_type(int)
    @pre_condition("dataWidth", lambda dataWidth: dataWidth >= 0, IllegalArgumentError, "Invalid data width for physical memory.")
    @require("dataWidth", int)
    def setDataWidth(self, dataWidth):
        if isinstance(dataWidth, bool):
            raise TypeError()
        self.__dataWidth = dataWidth
        return self.__dataWidth
    
    @public
    @return_type(int)
    @pre_condition("speed", lambda speed: speed >= 0, IllegalArgumentError, "Invalid speed for physical memory.")
    @require("speed", int)
    def setSpeed(self, speed):
        if isinstance(speed, bool):
            raise TypeError()
        self.__speed = speed
        return self.__speed