from win32com import client
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.exception.DAOError import DAOError
from org.pyvereign.core.environment.instrumentation.dao.hardware.MachineDAO import MachineDAO
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactory import HardwareDTOFactory

class WindowsMachineDAO(MachineDAO):
    """
    Defines an implementation for windows SO. 
    
    @author: Fabricio
    @since: 25/03/2008 - 14:22:45
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def retrieveMachine(self):
        """
        Retrieves the machine information.
        @return: Returns the machine information.
        @rtype: L{Machine}
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_ComputerSystem")
        
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        configurator = HardwareDTOFactoryConfigurator()
        configurator.setObjectRepository(repository)
        configurator.setFilename(Constants.HARDWARES_CONFIG_FILE)
        
        configurator.loadConfiguration()
        configurator.createObjects()
        factory = configurator.configureObject(HardwareDTOFactory())
        
        if not colItems:
            raise DAOError("Machine not found.")
    
        values = {}
        
        item = colItems[0]
        
        if item.Description:
            values["description"] = str(item.Description)
        if item.Domain:
            values["domain"] = str(item.Domain)
        if item.Name:
            values["hardwareId"] = str(item.Name)
            values["logicalName"] = str(item.Name)
        if item.NumberOfProcessors:
            values["processors"] = item.NumberOfProcessors
        if item.Model:
            values["product"] = item.Model
        if item.TotalPhysicalMemory:
            values["totalMemory"] = item.TotalPhysicalMemory
        if item.Manufacturer:
            values["vendor"] = item.Manufacturer
        
        machine = factory.createHardware(Constants.MACHINE, values)
        
        return machine