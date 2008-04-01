from org.pyvereign.core.environment.dao.hardware.BatteryDAO import BatteryDAO
from win32com import client
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
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
        