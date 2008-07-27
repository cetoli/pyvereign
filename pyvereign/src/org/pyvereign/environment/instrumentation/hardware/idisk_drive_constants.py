from org.pyvereign.base.interface import Interface

class IDiskDriveConstants(object):
    
    __metaclass__ = Interface
    
    TYPE_UNKNOW = "Unknow"
    TYPE_NO_ROOT_DIRECTORY = "No Root Directory"
    TYPE_REMOVABLE_DRIVE = "Removable Disk"
    TYPE_LOCAL_DISK = "Local Disk"
    TYPE_NETWORK_DRIVE = "Network Drive"
    TYPE_COMPACT_DISK = "Compact Disk"
    TYPE_RAM_DISK = "RAM Disk"
    
    def __init__(self):
        raise NotImplementedError()