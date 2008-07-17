from org.pyvereign.environment.instrumentation.hardware.default_hardware import DefaultHardware
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.require import require
from org.pyvereign.util.decorators.pre_condition import pre_condition
from org.pyvereign.error.IllegalArgumentError import IllegalArgumentError

class Machine(DefaultHardware):
    
    def __init__(self):
        DefaultHardware.__init__(self)
        self.setDomain("")
        self.setNumberOfProcessors(1)
        self.setTotalPhysicalMemory(0)
    
    @public
    @return_type(str)    
    def getDomain(self):
        return self.__domain
    
    @public
    @return_type(int)
    def getNumberOfProcessors(self):
        return self.__processors
    
    @public
    @return_type(int)
    def getTotalPhysicalMemory(self):
        return self.__memory
    
    @public
    @return_type(str)
    @require("domain", str)
    def setDomain(self, domain):
        self.__domain = domain
        return self.__domain
    
    @public
    @return_type(int)
    @pre_condition("processors", lambda procs: procs >= 1, IllegalArgumentError, "Invalid number of processors.")
    @require("processors", int)
    def setNumberOfProcessors(self, processors):
        if isinstance(processors, bool):
            raise TypeError()
        self.__processors = processors
        return self.__processors
    
    @public
    @return_type(int)
    @pre_condition("memory", lambda procs: procs >= 0, IllegalArgumentError, "Invalid total of memory.")
    @require("memory", int)
    def setTotalPhysicalMemory(self, memory):
        if isinstance(memory, bool):
            raise TypeError()
        self.__memory = memory
        return self.__memory