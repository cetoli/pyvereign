from org.pyvereign.environment.instrumentation.hardware.ihardware import IHardware
from org.pyvereign.base.interface import Interface

class IDiskDrive(IHardware):
    
    __metaclass__ = Interface
    
    def __init__(self):
        raise NotImplementedError()
    
    def getDriveType(self):
        raise NotImplementedError()
    
    def getFileSystem(self):
        raise NotImplementedError()
    
    def getFreeSpace(self):
        raise NotImplementedError()
    
    def getSize(self):
        raise NotImplementedError()
    
    def getVolumeName(self):
        raise NotImplementedError()
    
    def setDriveType(self, type):
        raise NotImplementedError()
    
    def setFileSystem(self, fileSystem):
        raise NotImplementedError()
    
    def setFreeSpace(self, freeSpace):
        raise NotImplementedError()
    
    def setSize(self, size):
        raise NotImplementedError()
    
    def setVolumeName(self, volumeName):
        raise NotImplementedError()