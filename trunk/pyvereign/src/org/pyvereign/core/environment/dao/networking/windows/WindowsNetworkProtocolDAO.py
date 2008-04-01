from org.pyvereign.core.environment.dao.networking.NetworkProtocolDAO import NetworkProtocolDAO
from win32com import client

class WindowsNetworkProtocolDAO(NetworkProtocolDAO):
    """
    Defines the implementation for data access objects of network protocol.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def retrieveNetworkProtocol(self):
        """
        Retrieves the network protocols that installed on user computer.
        @return: Returns the network protocols that installed on user computer.
        @rtype: list
        """
        strComputer = "."
        objWMIService = client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
        colItems = objSWbemServices.ExecQuery("Select * from Win32_NetworkProtocol")
        
        result = []
    