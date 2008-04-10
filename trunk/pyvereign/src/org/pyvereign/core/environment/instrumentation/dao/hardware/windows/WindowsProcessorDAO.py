from win32com import client
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.instrumentation.dao.hardware.ProcessorDAO import ProcessorDAO
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
from sets import ImmutableSet

class WindowsProcessorDAO(ProcessorDAO):
    """
    ProcessorDAO implementation for Windows SO 
    
    @author: Fabricio
    @since: 25/03/2008 - 15:25:46
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def retrieveProcessors(self):
        """
        Retrieves processor that are installed in user machine.
        @return: Returns processor that are installed in user machine.
        @rtype: ImmutableSet
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Processor")
        
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
            
            if item.Architecture:
                values["architecture"] = int(item.Architecture)
                
            if item.CPUStatus:
                values["cpuStatus"] = int(item.CPUStatus)
                
            if item.CurrentClockSpeed:
                values["currentClockSpeed"] = int(item.CurrentClockSpeed)
                
            if item.Description:
                values["description"] = str(item.Description)
                
            if item.DeviceId:
                values["hardwareId"] = str(item.DeviceId)
            
            if item.L2CacheSize:
                values["l2CacheSize"] = int(item.L2CacheSize)
                
            if item.L2CacheSpeed:
                values["l2CacheSpeed"] = int(item.L2CacheSpeed)
                
            if item.LoadPercentage:
                values["loadPercentage"] = int(item.LoadPercentage)
                
            if item.Name:
                values["logicalName"] = str(item.Name)
                values["product"] = str(item.Name)
            
            if item.MaxClockSpeed:
                values["maxClockSpeed"] = int(item.MaxClockSpeed)
                
            if item.ProcessorId:
                values["processorId"] = str(item.ProcessorId)
                
            if item.ProcessorType:
                values["processorType"] = int(item.ProcessorType)
            
            if item.UniqueId:
                values["serial"] = str(item.UniqueId)
            
            if item.Manufacturer:
                values["vendor"] = str(item.Manufacturer)
            
            processor = factory.createHardware(Constants.PROCESSOR, values)
            result.append(processor)
    
        return ImmutableSet(result)