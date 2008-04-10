from win32com import client
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
from sets import ImmutableSet
class WindowsPhysicalMemoryDAO(object):
    """
    Implmetation of PhysicalMemoryDAO for Windows SO 
    
    @author: Fabricio
    @since: 25/03/2008 - 17:32:25
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def retrievePhysicalMemories(self):
        """
        Retrieves physical memories which are installed in user machine.
        @return: Returns physical memories which are installed in user machine.
        @rtype: ImmutableSet
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_PhysicalMemory")
        
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
            
            if item.Capacity:
                values["capacity"] = int(item.Capacity)
            
            if item.DataWidth:
                values["dataWidth"] = int(item.DataWidth)
                
            if item.Description:
                values["description"] = str(item.Description)
                values["product"] = str(item.Description)
            
            if item.DeviceLocator:
                values["deviceLocator"] = str(item.DeviceLocator)
                
            if item.SerialNumber:
                values["hardwareId"] = str(item.SerialNumber)
                
            if item.Name:
                values["logicalName"] = str(item.Name)
            
                
                
            if item.SerialNumber:
                values["serial"] = str(item.SerialNumber)
                
            if item.Speed:
                values["speed"] = int(item.Speed)
                
            if item.Manufacturer:
                values["vendor"] = str(item.Manufacturer)
            
            memory = factory.createHardware(Constants.PHYSICAL_MEMORY, values)
            result.append(memory)
        
        return ImmutableSet(result)