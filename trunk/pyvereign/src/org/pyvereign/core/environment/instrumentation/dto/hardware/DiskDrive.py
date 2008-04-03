from org.pyvereign.core.environment.instrumentation.dto.hardware.Hardware import Hardware

class DiskDrive(Hardware):
    """
    Defines the common interface for disk drives.
    
    @author: Fabricio
    @since: 21/03/2008 - 23:22:24
    @version: 0.0.1
    """
    
    TYPE_UNKNOW = "Unknow"
    TYPE_NO_ROOT_DIRECTORY = "No Root Directory"
    TYPE_REMOVABLE_DRIVE = "Removable Disk"
    TYPE_LOCAL_DISK = "Local Disk"
    TYPE_NETWORK_DRIVE = "Network Drive"
    TYPE_COMPACT_DISK = "Compact Disk"
    TYPE_RAM_DISK = "RAM Disk"
    
    def getDriveType(self):
        """
        Gets the type of disk drive.
        @return: Returns the type of disk drive.
        @rtype: str
        """
        pass
    
    def getFileSystem(self):
        """
        Gets the file system of disk drive.
        @return: Returns the file system of disk drive.
        @rtype: str
        """
        pass
    
    def getFreeSpace(self):
        """
        Gets the free space of disk drive.
        @return: Returns the free space of disk drive.
        @rtype: int
        """
        pass
    
    def getSize(self):
        """
        Gets the size of disk drive.
        @return: Returns the size of disk drive.
        @rtype: int
        """
        pass
    
    def getVolumeName(self):
        """
        Gets the free space of disk drive.
        @return: Returns the free space of disk drive.
        @rtype: str
        """
        pass