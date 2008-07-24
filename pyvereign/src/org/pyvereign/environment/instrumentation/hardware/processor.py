from org.pyvereign.environment.instrumentation.hardware.default_hardware import DefaultHardware
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.pre_condition import pre_condition
from org.pyvereign.error.illegal_argument_error import IllegalArgumentError
from org.pyvereign.util.decorators.require import require

class Processor(DefaultHardware):
    
    ARCH_X86 = "x86"
    ARCH_MIPS = "MIPS"
    ARCH_ALPHA = "Alpha"
    ARCH_POWER_PC = "Power PC"
    ARCH_IPF = "Intel Itanium Processor Family"
    ARCH_X64 = "x64"
    
    ST_UNKNOW = "Unknow"
    ST_CPU_ENABLE = "CPU Enabled"
    ST_CPU_DISABLE_BY_USER = "CPU Disabled by User via BIOS Setup"
    ST_CPU_DISABLE_BY_BIOS = "CPU Disabled by BIOS (POST Error)"
    ST_CPU_IDLE = "CPU Is Idle"
    ST_CPU_RESERVED = "Reserved"
    ST_OTHER = "Other"
    
    PROC_TYPE_OTHER = "Other"
    PROC_TYPE_UNKNOW = "Unknow"
    PROC_TYPE_CENTRAL_PROCESSOR = "Central Processor"
    PROC_TYPE_MATH_PROCESSOR = "Math Processor"
    PROC_TYPE_DSP_PROCESSOR = "DSP Processor"
    PROC_TYPE_VIDEO_PROCESSOR = "Video Processor"
    
    ARCH_VALUES = {0: ARCH_X86, 1: ARCH_MIPS, 2: ARCH_ALPHA, 
                   3: ARCH_POWER_PC, 6: ARCH_IPF, 9: ARCH_X64}
    
    ST_VALUES = {0: ST_UNKNOW, 1: ST_CPU_ENABLE, 2: ST_CPU_DISABLE_BY_USER,
                 3: ST_CPU_DISABLE_BY_BIOS, 4: ST_CPU_IDLE, 5: ST_CPU_RESERVED,
                 6: ST_CPU_RESERVED, 7: ST_OTHER}
    
    PROC_TYPE_VALUES = {1: PROC_TYPE_OTHER, 2: PROC_TYPE_UNKNOW, 
                        3: PROC_TYPE_CENTRAL_PROCESSOR, 
                        4: PROC_TYPE_MATH_PROCESSOR, 
                        5: PROC_TYPE_DSP_PROCESSOR, 
                        6: PROC_TYPE_VIDEO_PROCESSOR}
    
    def __init__(self):
        DefaultHardware.__init__(self)
        self.setArchitecture(0)
        self.setCPUStatus(0)
        self.setCurrentClockSpeed(0)
        self.setL2CacheSize(0)
        self.setL2CacheSpeed(0)
        self.setLoadPercentage(0)
        self.setProcessorId("")
        self.setMaxClockSpeed(0)
        self.setProcessorType(1)
    
    @public
    @return_type(str)    
    def getArchitecture(self):
        return self.ARCH_VALUES[self.__architecture]
    
    @public
    @return_type(str)
    def getCPUStatus(self):
        return self.ST_VALUES[self.__cpuStatus]
    
    @public
    @return_type(int)
    def getCurrentClockSpeed(self):
        return self.__currentClockSpeed
    
    @public
    @return_type(int)
    def getL2CacheSize(self):
        return self.__l2CacheSize
    
    @public
    @return_type(int)
    def getL2CacheSpeed(self):
        return self.__l2CacheSpeed
    
    @public
    @return_type(int)
    def getLoadPercentage(self):
        return self.__loadPercentage
    
    @public
    @return_type(int)
    def getMaxClockSpeed(self):
        return self.__maxClockSpeed
    
    @public
    @return_type(str)
    def getProcessorId(self):
        return self.__processorId
    
    @public
    @return_type(str)
    def getProcessorType(self):
        return self.PROC_TYPE_VALUES[self.__processorType]
    
    @public
    @return_type(str)
    @pre_condition("architecture", lambda arch: (arch >= 0 and arch <= 3) or (arch == 6) or (arch == 9), IllegalArgumentError)
    @require("architecture", int)
    def setArchitecture(self, architecture):
        if isinstance(architecture, bool):
            raise TypeError()
        self.__architecture = architecture
        return self.ARCH_VALUES[self.__architecture]
    
    @public
    @return_type(str)
    @pre_condition("cpuStatus", lambda status: status >= 0 and status <= 7, IllegalArgumentError)
    @require("cpuStatus", int)
    def setCPUStatus(self, cpuStatus):
        self.__cpuStatus = cpuStatus
        return self.ST_VALUES[self.__cpuStatus]
    
    @public
    @return_type(int)
    @pre_condition("speed", lambda speed: speed >= 0, IllegalArgumentError)
    @require("speed", int)
    def setCurrentClockSpeed(self, speed):
        if isinstance(speed, bool):
            raise TypeError()
        self.__currentClockSpeed = speed
        return self.__currentClockSpeed
    
    @public
    @return_type(int)
    @pre_condition("l2CacheSize", lambda speed: speed >= 0, IllegalArgumentError)
    @require("l2CacheSize", int)
    def setL2CacheSize(self, l2CacheSize):
        if isinstance(l2CacheSize, bool):
            raise TypeError()
        self.__l2CacheSize = l2CacheSize
        return self.__l2CacheSize
    
    @public
    @return_type(int)
    @pre_condition("l2CacheSpeed", lambda speed: speed >= 0, IllegalArgumentError)
    @require("l2CacheSpeed", int)
    def setL2CacheSpeed(self, l2CacheSpeed):
        if isinstance(l2CacheSpeed, bool):
            raise TypeError()
        self.__l2CacheSpeed = l2CacheSpeed
        return self.__l2CacheSpeed
    
    @public
    @return_type(int)
    @pre_condition("loadPercentage", lambda perc: perc >= 0 and perc <= 100, IllegalArgumentError)
    @require("loadPercentage", int)
    def setLoadPercentage(self, loadPercentage):
        if isinstance(loadPercentage, bool):
            raise TypeError()
        self.__loadPercentage = loadPercentage
        return self.__loadPercentage
    
    @public
    @return_type(int)
    @pre_condition("maxClockSpeed", lambda speed: speed >= 0, IllegalArgumentError)
    @require("maxClockSpeed", int)
    def setMaxClockSpeed(self, maxClockSpeed):
        if isinstance(maxClockSpeed, bool):
            raise TypeError()
        self.__maxClockSpeed = maxClockSpeed
        return self.__maxClockSpeed
    
    @public
    @return_type(str)
    @require("processorId", str)
    def setProcessorId(self, processorId):
        self.__processorId = processorId
        return self.__processorId
    
    @public
    @return_type(str)
    @pre_condition("processorType", lambda processorType: processorType >= 1 and processorType <= 6, IllegalArgumentError)
    @require("processorType", int)
    def setProcessorType(self, processorType):
        if isinstance(processorType, bool):
            raise TypeError()
        self.__processorType = processorType
        return self.PROC_TYPE_VALUES[self.__processorType]