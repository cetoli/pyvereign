from org.pyvereign.environment.instrumentation.hardware.default_hardware import DefaultHardware
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.require import require
from org.pyvereign.util.decorators.pre_condition import pre_condition
from org.pyvereign.error.IllegalArgumentError import IllegalArgumentError

class DiskDrive(DefaultHardware):
    
    TYPE_UNKNOW = "Unknow"
    TYPE_NO_ROOT_DIRECTORY = "No Root Directory"
    TYPE_REMOVABLE_DRIVE = "Removable Disk"
    TYPE_LOCAL_DISK = "Local Disk"
    TYPE_NETWORK_DRIVE = "Network Drive"
    TYPE_COMPACT_DISK = "Compact Disk"
    TYPE_RAM_DISK = "RAM Disk"
    
    TYPE_VALUES = {0: TYPE_UNKNOW, 1: TYPE_NO_ROOT_DIRECTORY, 
                   2: TYPE_REMOVABLE_DRIVE, 3: TYPE_LOCAL_DISK, 
                   4: TYPE_NETWORK_DRIVE, 5: TYPE_COMPACT_DISK, 
                   6: TYPE_RAM_DISK}
    
    def __init__(self):
        DefaultHardware.__init__(self)
        self.setDriveType(3)
        self.setFileSystem("")
        self.setFreeSpace(0)
        self.setVolumeName("")
        self.setSize(0)
    
    @public
    @return_type(str)    
    def getDriveType(self):
        return self.TYPE_VALUES[self.__driveType]
    
    @public
    @return_type(str)    
    def getFileSystem(self):
        return self.__fileSystem
    
    @public
    @return_type(int)
    def getFreeSpace(self):
        return self.__freeSpace
    
    @public
    @return_type(int)    
    def getSize(self):
        return self.__size
    
    @public
    @return_type(str)
    def getVolumeName(self):
        return self.__volumeName
    
    @public
    @return_type(str)
    @pre_condition("type", lambda type: type >= 0 and type <= 6, IllegalArgumentError, "Invalid type for disk drive.")
    @require("type", int)
    def setDriveType(self, type):
        if isinstance(type, bool):
            raise TypeError()
        self.__driveType = type
        return self.TYPE_VALUES[self.__driveType]
    
    @public
    @return_type(str)
    @require("fileSystem", str)
    def setFileSystem(self, fileSystem):
        self.__fileSystem = fileSystem
        return self.__fileSystem
    
    @public
    @return_type(int)
    @pre_condition("freeSpace", lambda type: type >= 0, IllegalArgumentError, "Invalid free space for disk drive.")
    @require("freeSpace", int)
    def setFreeSpace(self, freeSpace):
        if isinstance(freeSpace, bool):
            raise TypeError()
        self.__freeSpace = freeSpace
        return self.__freeSpace
    
    @public
    @return_type(int)
    @pre_condition("size", lambda size: size >= 0, IllegalArgumentError, "Invalid size for disk drive.")
    @require("size", int)
    def setSize(self, size):
        if isinstance(size, bool):
            raise TypeError()
        self.__size = size
        return self.__size
    
    @public
    @return_type(str)
    @require("volumeName", str)
    def setVolumeName(self, volumeName):
        self.__volumeName = volumeName
        return self.__volumeName