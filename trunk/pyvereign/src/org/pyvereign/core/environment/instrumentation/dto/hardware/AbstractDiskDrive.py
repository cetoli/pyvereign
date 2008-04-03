from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractHardware import AbstractHardware
from org.pyvereign.core.environment.instrumentation.dto.hardware.DiskDrive import DiskDrive

class AbstractDiskDrive(AbstractHardware, DiskDrive):
    """
    Defines the common implementation for disk drives.
    
    @author: Fabricio
    @since: 21/03/2008 - 23:22:24
    @version: 0.0.1
    """
    
    TYPE_VALUES = {0: DiskDrive.TYPE_UNKNOW, 1: DiskDrive.TYPE_NO_ROOT_DIRECTORY, 
                   2: DiskDrive.TYPE_REMOVABLE_DRIVE, 3: DiskDrive.TYPE_LOCAL_DISK, 
                   4: DiskDrive.TYPE_NETWORK_DRIVE, 5: DiskDrive.TYPE_COMPACT_DISK, 
                   6:DiskDrive.TYPE_RAM_DISK}
    
    def init(self, values):
        self._driveType = 0
        """
        @ivar: the drive type of disk drive.
        @type: int
        """
        self._fileSystem = ""
        """
        @ivar: the file system of disk drive.
        @type: str
        """
        self._freeSpace = 0
        """
        @ivar: the free space of disk drive.
        @type: int
        """
        self._size = 0
        """
        @ivar: the size of disk drive.
        @type: int
        """
        self._volumeName = ""
        """
        @ivar: the file system of disk drive.
        @type: str
        """
        AbstractHardware.init(self, values)
        
        if values.has_key("driveType"):
            self._driveType = values["driveType"]
        
        if values.has_key("fileSystem"):
            self._fileSystem = values["fileSystem"]
            
        if values.has_key("freeSpace"):
            self._freeSpace = values["freeSpace"]
        
        if values.has_key("size"):
            self._size = values["size"]
            
        if values.has_key("volumeName"):
            self._volumeName = values["volumeName"]
    
    def getDriveType(self):
        """
        Gets the type of disk drive.
        @return: Returns the type of disk drive.
        @rtype: str
        """
        return AbstractDiskDrive.TYPE_VALUES[self._driveType]
    
    def getFileSystem(self):
        """
        Gets the file system of disk drive.
        @return: Returns the file system of disk drive.
        @rtype: str
        """
        return self._fileSystem
    
    def getFreeSpace(self):
        """
        Gets the free space of disk drive.
        @return: Returns the free space of disk drive.
        @rtype: int
        """
        return self._freeSpace
    
    def getSize(self):
        """
        Gets the size of disk drive.
        @return: Returns the size of disk drive.
        @rtype: int
        """
        return self._size
    
    def getVolumeName(self):
        """
        Gets the free space of disk drive.
        @return: Returns the free space of disk drive.
        @rtype: str
        """
        return self._volumeName