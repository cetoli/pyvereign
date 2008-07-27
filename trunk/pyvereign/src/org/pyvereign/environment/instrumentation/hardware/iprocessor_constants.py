from org.pyvereign.base.interface import Interface

class IProcessorConstants(object):
    
    __metaclass__ = Interface
    
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
    
    def __init__(self):
        raise NotImplementedError()