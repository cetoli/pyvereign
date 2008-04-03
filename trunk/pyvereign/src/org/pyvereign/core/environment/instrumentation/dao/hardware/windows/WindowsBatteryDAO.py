from win32com import client
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.instrumentation.dao.hardware.BatteryDAO import BatteryDAO
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
from org.pyvereign.core.exception.DAOError import DAOError

class WindowsBatteryDAO(BatteryDAO):
    
    def __init__(self):
        return
    
    def retrieveBattery(self):
        """
        Retrieves the battery of user computer.
        @return: Returns the battery of user computer.
        @rtype: L{Battery}
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Battery")
        
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        configurator = HardwareDTOFactoryConfigurator()
        configurator.setObjectRepository(repository)
        configurator.setFilename(Constants.HARDWARES_CONFIG_FILE)
        
        configurator.loadConfiguration()
        configurator.createObjects()
        factory = configurator.configureObject(HardwareDTOFactory())
        
        if not colItems:
            raise DAOError("Battery not found.")
    
        values = {}
        
        item = colItems[0]
        
        if item.Caption:
            values["product"] = str(item.Caption)
            values["logicalName"] = str(item.Caption)
        
        if item.Description:
            values["description"] = str(item.Description)
            
        if item.DeviceId:
            values["hardwareId"] = str(item.DeviceId)
            values["serial"] = str(item.DeviceId)
        
        if item.EstimatedChargeRemaining:
            values["estimatedChargeRemaining"] = int(item.EstimatedChargeRemaining) 
            
        battery = factory.createHardware(Constants.BATTERY, values)
        
        return battery
            
            
        