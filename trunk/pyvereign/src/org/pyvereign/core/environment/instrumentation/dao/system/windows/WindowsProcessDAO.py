from win32com import client
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.instrumentation.dao.system.ProcessDAO import ProcessDAO
from org.pyvereign.core.environment.instrumentation.dto.system.SystemElementDTOFactoryConfigurator import SystemElementDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.system.SystemElementDTOFactory import SystemElementDTOFactory
from sets import ImmutableSet

class WindowsProcessDAO(ProcessDAO):
    """
    Defines the implementation of ProcessDAO for windows SO. 
    
    @author: Fabricio
    @since: 29/03/2008 - 13:29:49
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def retrieveProcesses(self):
        """
        Retrieves processes which are running on the user computer.
        @return: Returns processes which are running on the user computer.
        @rtype: ImmutableSet
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Process")
        
        result = []
        
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        configurator = SystemElementDTOFactoryConfigurator()
        configurator.setObjectRepository(repository)
        configurator.setFilename(Constants.SYSTEM_ELEMENTS_CONFIG_FILE)
        
        configurator.loadConfiguration()
        configurator.createObjects()
        factory = configurator.configureObject(SystemElementDTOFactory())
        
        for item in colItems:
            values = {}
            
            if item.Name:
                values["name"] = str(item.Name)
                
            if item.ProcessId:
                values["processId"] = str(item.ProcessId)
                
            if item.MaximumWorkingSetSize:
                values["maximumWorkingSetSize"] = int(item.MaximumWorkingSetSize)
            
            if item.MinimumWorkingSetSize:
                values["minimumWorkingSetSize"] = int(item.MinimumWorkingSetSize)
                
            if item.VirtualSize:
                values["virtualSize"] = int(item.VirtualSize)
                
            process = factory.createSystemElement(Constants.PROCESS, values)
            result.append(process)
        
        return ImmutableSet(result)
    