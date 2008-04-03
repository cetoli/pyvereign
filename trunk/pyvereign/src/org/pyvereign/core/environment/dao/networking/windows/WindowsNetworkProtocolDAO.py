from org.pyvereign.core.environment.dao.networking.NetworkProtocolDAO import NetworkProtocolDAO
from win32com import client
from org.pyvereign.core.environment.dto.networking.NetworkingElementDTOFactory import NetworkingElementDTOFactory
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.dto.networking.NetworkingElementDTOFactoryConfigurator import NetworkingElementDTOFactoryConfigurator

class WindowsNetworkProtocolDAO(NetworkProtocolDAO):
    """
    Defines the implementation for data access objects of network protocol.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def retrieveNetworkProtocols(self):
        """
        Retrieves the network protocols that installed on user computer.
        @return: Returns the network protocols that installed on user computer.
        @rtype: list
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkProtocol where Name like '%/IP%'")
        
        result = []
        
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        configurator = NetworkingElementDTOFactoryConfigurator()
        configurator.setObjectRepository(repository)
        configurator.setFilename(Constants.NETWORKING_ELEMENTS_CONFIG_FILE)
        
        configurator.loadConfiguration()
        configurator.createObjects()
        factory = configurator.configureObject(NetworkingElementDTOFactory())


        for item in colItems:
            values = {}
            if item.Name:
                values["name"] = str(item.Name)
            
            if item.SupportsBroadcasting:
                values["supportsBroadcasting"] = bool(item.SupportsBroadcasting)
            
            if item.GuaranteesDelivery:
                values["guaranteesDelivery"] = bool(item.GuaranteesDelivery)
                
            if item.SupportsMulticasting:
                values["supportsMulticasting"] = bool(item.SupportsMulticasting)
            
            result.append(factory.createNetworkingElement(Constants.NETWORK_PROTOCOL, values))
        return result
    