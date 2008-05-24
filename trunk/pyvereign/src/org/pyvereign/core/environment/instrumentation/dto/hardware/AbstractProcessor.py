from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractHardware import AbstractHardware
from org.pyvereign.core.environment.instrumentation.dto.hardware.Processor import Processor

class AbstractProcessor(AbstractHardware, Processor):
    """
    Define the common implementation for Processor objects.
    
    @author: Fabricio
    @since: 22/03/2008 - 18:19:42
    @version: 0.0.1
    """
    
    ARCH_VALUES = {0: Processor.ARCH_X86, 1: Processor.ARCH_MIPS, 2: Processor.ARCH_ALPHA, 
                   3: Processor.ARCH_POWER_PC, 6: Processor.ARCH_IPF, 9: Processor.ARCH_X64}
    
    ST_VALUES = {0: Processor.ST_UNKNOW, 1: Processor.ST_CPU_ENABLE, 2: Processor.ST_CPU_DISABLE_BY_USER,
                 3: Processor.ST_CPU_DISABLE_BY_BIOS, 4: Processor.ST_CPU_IDLE, 5: Processor.ST_CPU_RESERVED,
                 6: Processor.ST_CPU_RESERVED, 5: Processor.ST_OTHER}
    
    PROC_TYPE_VALUES = {1: Processor.PROC_TYPE_OTHER, 2: Processor.PROC_TYPE_UNKNOW, 
                        3: Processor.PROC_TYPE_CENTRAL_PROCESSOR, 
                        4: Processor.PROC_TYPE_MATH_PROCESSOR, 
                        5: Processor.PROC_TYPE_DSP_PROCESSOR, 
                        6: Processor.PROC_TYPE_VIDEO_PROCESSOR}
    
    def init(self, values = {}):
        self._architecture = 0
        """
        @ivar: the archtecture of processor.
        @type : int 
        """
        self._cpuStatus = 0
        """
        @ivar: the status of processor cpu.
        @type : int 
        """
        self._currentClockSpeed = 0
        """
        @ivar: the current clock of processor.
        @type : int 
        """
        self._l2CacheSize = 0
        """
        @ivar: the L2 cache size of processor.
        @type : int 
        """
        self._l2CacheSpeed = 0
        """
        @ivar: the L2 cache speed of processor.
        @type : int 
        """
        self._loadPercentage = 0
        """
        @ivar: the load percentage of processor.
        @type : int 
        """
        self._maxClockSpeed = 0
        """
        @ivar: the max clock speed of processor.
        @type : int 
        """
        self._processorId = ""
        """
        @ivar: the id of processor.
        @type : str 
        """
        self._processorType = 0
        """
        @ivar: the type of processor.
        @type : int 
        """
        AbstractHardware.init(self, values)
        
        if values.has_key("architecture"):
            self._architecture = values["architecture"]
        
        if values.has_key("cpuStatus"):
            self._cpuStatus = values["cpuStatus"]
            
        if values.has_key("currentClockSpeed"):
            self._currentClockSpeed = values["currentClockSpeed"]
        
        if values.has_key("l2CacheSize"):
            self._l2CacheSize = values["l2CacheSize"]
        
        if values.has_key("l2CacheSpeed"):
            self._l2CacheSpeed = values["l2CacheSpeed"]
        
        if values.has_key("loadPercentage"):
            self._loadPercentage = values["loadPercentage"]
        
        if values.has_key("maxClockSpeed"):
            self._maxClockSpeed = values["maxClockSpeed"]
        
        if values.has_key("processorId"):
            self._processorId = values["processorId"]
        
        if values.has_key("processorType"):
            self._processorType = values["processorType"]
        
    def getArchitecture(self):
        """
        Gets the architecture of processor.
        
        @return: Returns the architecture of processor.
        @rtype: L{str}
        """
        return AbstractProcessor.ARCH_VALUES[self._architecture]
    
    def getCPUStatus(self):
        """
        Gets the status of CPU.
        
        @return: Returns the status of CPU.
        @rtype: L{str}
        """
        return AbstractProcessor.ST_VALUES[self._cpuStatus] 
    
    def getCurrentClockSpeed(self):
        """
        Gets the current clock of processor.
        
        @return: Returns the current clock of processor.
        @rtype: L{int}
        """
        return self._currentClockSpeed
    
    def getL2CacheSize(self):
        """
        Gets the L2 cache size of processor.
        
        @return: Returns the L2 cache size of processor.
        @rtype: L{int}
        """
        return self._l2CacheSize
    
    def getL2CacheSpeed(self):
        """
        Gets the L2 cache speed of processor.
        
        @return: Returns the L2 cache speed of processor.
        @rtype: L{int}
        """
        return self._l2CacheSpeed
    
    def getLoadPercentage(self):
        """
        Gets the load percentage of processor.
        
        @return: Returns the load percentage of processor.
        @rtype: L{int}
        """
        return self._loadPercentage
    
    def getMaxClockSpeed(self):
        """
        Gets the max clock speed of processor.
        
        @return: Returns the max clock speed of processor.
        @rtype: L{int}
        """
        return self._maxClockSpeed
    
    def getProcessorId(self):
        """
        Gets the processor id.
        
        @return: Returns the processor id.
        @rtype: L{str}
        """
        return self._processorId
    
    def getProcessorType(self):
        """
        Gets the processor type.
        
        @return: Returns the processor type.
        @rtype: L{str}
        """
        return AbstractProcessor.PROC_TYPE_VALUES[self._processorType]