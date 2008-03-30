from org.pyvereign.core.environment.dao.hardware.NetworkAdapterDAO import NetworkAdapterDAO
from win32com import client
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactory import HardwareDTOFactory

class WindowsNetwworkAdapterDAO(NetworkAdapterDAO):
    """
    Defines the implementation of NetworkAdapterDAO interface for Windows SO. 
    
    @author: Fabricio
    @since: 30/03/2008 - 00:12:54
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def retrieveNetworkAdapters(self):
        """
        Retrieves network adapters installed in the user computer.
        @return: Returns network adapters installed in the user computer.
        @rtype: list
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkAdapterConfiguration where DNSHostName <> null")
        
        result = []
        
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        configurator = HardwareDTOFactoryConfigurator()
        configurator.setObjectRepository(repository)
        configurator.setFilename(Constants.HARDWARES_CONFIG_FILE)
        
        configurator.loadConfiguration()
        configurator.createObjects()
        factory = configurator.configureObject(HardwareDTOFactory())
        
        for item in colItems:
            adapters = objSWbemServices.ExecQuery("Select * from Win32_NetworkAdapter where Index = " + str(item.Index))             
            adapter = adapters[0]
            
            values = {}
            
            if adapter.Description:
                values["description"] = str(adapter.Description)
                
            if adapter.Name:
                values["product"] = str(adapter.Name)
                values["logicalName"] = str(adapter.Name)
            
            if adapter.Manufacturer:
                values["vendor"] = str(adapter.Manufacturer)
                
            if adapter.DeviceId:
                values["serial"] = str(adapter.DeviceId)
                values["hardwareId"] = str(adapter.DeviceId)
            
            if adapter.Speed:
                values["speed"] = int(adapter.Speed)
            
            if adapter.MACAddress:
                values["macAddress"] = str(adapter.MACAddress)
                
            if item.IPAddress[0]:
                values["ipAddress"] = str(item.IPAddress[0])
            
            networkAdapter = factory.createHardware(Constants.NETWORK_ADAPTER, values)
            result.append(networkAdapter)
        
        return result 
            
            