from org.pyvereign.core.environment.dao.hardware.DiskDriveDAO import DiskDriveDAO
from win32com import client
from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator

class WindowsDiskDriveDAO(DiskDriveDAO):
    """
    Defines an implementation 
    
    @author: Fabricio
    @since: 25/03/2008 - 13:07:16
    @version: 0.0.1
    """
    def __init__(self):
        return 
    
    def retrieveDiskDrives(self):
        """
        Retrieves disk drives which are installed in user machine.
        @return: Returns disk drives which are installed in user machine.
        @rtype: list
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk where FreeSpace > 0")
        
        result = []
        
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        configurator = HardwareDTOFactoryConfigurator()
        configurator.setObjectRepository(repository)
        configurator.setFilename(Constants.HARDWARES_CONFIG_FILE)
        
        configurator.loadConfiguration()
        configurator.createObjects()
        factory = configurator.configureObject(HardwareDTOFactory())
        
        
        for item in colItems:
            values = {}
            if item.Description:
                values["description"] = str(item.Description)
            if item.DriveType:
                values["driveType"] = int(item.DriveType)
            if item.FileSystem:
                values["fileSystem"] = str(item.FileSystem)
            if item.FreeSpace:
                values["freeSpace"] = int(item.FreeSpace)
            if item.DeviceID:
                values["hardwareId"] = str(item.DeviceID)
            if item.Name:
                values["logicalName"] = str(item.Name)
            if item.Description:
                values["product"] = str(item.Description)
            if item.Size:
                values["size"] = int(item.Size)
            if item.VolumeName:
                values["volumeName"] = str(item.VolumeName)
            if item.VolumeSerialNumber:
                values["serial"] = str(item.VolumeSerialNumber)
            
            
            diskDrive = factory.createHardware(Constants.DISK_DRIVE, values)
            result.append(diskDrive)
        
        return result