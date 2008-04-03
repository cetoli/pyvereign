from org.pyvereign.core.environment.instrumentation.dto.hardware.Hardware import Hardware

class Processor(Hardware):
    """
    Defines the common interface for Processor objects.
    
    @author: Fabricio
    @since: 22/03/2008 - 17:25:34
    @version: 0.0.1
    """
    
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
    
    
    
    def getArchitecture(self):
        """
        Gets the architecture of processor.
        
        @return: Returns the architecture of processor.
        @rtype: L{str}
        """
        pass
    
    def getCPUStatus(self):
        """
        Gets the status of CPU.
        
        @return: Returns the status of CPU.
        @rtype: L{str}
        """
        pass 
    
    def getCurrentClockSpeed(self):
        """
        Gets the current clock of processor.
        
        @return: return
        @rtype: L{type}
        """
        pass
    
    def getL2CacheSize(self):
        """
        Gets the L2 cache size of processor.
        
        @return: Returns the L2 cache size of processor.
        @rtype: L{int}
        """
        pass
    
    def getL2CacheSpeed(self):
        """
        Gets the L2 cache speed of processor.
        
        @return: Returns the L2 cache speed of processor.
        @rtype: L{int}
        """
        pass
    
    def getLoadPercentage(self):
        """
        Gets the load percentage of processor.
        
        @return: Returns the load percentage of processor.
        @rtype: L{int}
        """
        pass
    
    def getMaxClockSpeed(self):
        """
        Gets the max clock speed of processor.
        
        @return: Returns the max clock speed of processor.
        @rtype: L{int}
        """
        pass
    
    def getProcessorId(self):
        """
        Gets the processor id.
        
        @return: Returns the processor id.
        @rtype: L{str}
        """
        pass
    
    def getProcessorType(self):
        """
        Gets the processor type.
        
        @return: Returns the processor type.
        @rtype: L{str}
        """
        pass
    
    