from org.pyvereign.base.object import Object
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from sets import ImmutableSet
from win32com import client
from org.pyvereign.environment.instrumentation.hardware.hardware_factory import HardwareFactory

class WindowsDiskDriveDAO(Object):
    
    @public
    @return_type(ImmutableSet)
    def retrieveDiskDrives(self):
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk where FreeSpace > 0")
        
        result = []
        
        if len(colItems) == 0:
            return ImmutableSet(result)
        
        for item in colItems:
            diskdrive = HardwareFactory.createDiskDrive()
            diskdrive.setDescription(str(item.Description))
            diskdrive.setDriveType(int(item.DriveType))
            diskdrive.setFileSystem(str(item.FileSystem))
            diskdrive.setFreeSpace(int(item.FreeSpace))
            diskdrive.setHardwareId(str(item.DeviceId))
            diskdrive.setLogicalName(str(item.Name))
            diskdrive.setProduct(str(item.Description))
            diskdrive.setSize(int(item.Size))
            diskdrive.setSerial(str(item.VolumeSerialNumber))
            diskdrive.setVolumeName(str(item.VolumeName))
            
            result.append(diskdrive)
        
        return ImmutableSet(result)
