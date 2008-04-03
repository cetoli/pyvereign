from org.pyvereign.core.environment.dao.networking.windows.WindowsNetworkProtocolDAO import WindowsNetworkProtocolDAO
from org.pyvereign.core.environment.dao.networking.NetworkingElementDAOFactory import NetworkingElementDAOFactory

class WindowsNetworkingElementDAOFactory(NetworkingElementDAOFactory):
    """
    Defines the concrete factory for data access object of networking element dao for 
    Windows SO.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def createNetworkProtocolDAO(self):
        """
        Creates an instance of NetworkProtocolDAO.
        @return: Returns an instance of NetworkProtocolDAO.
        @rtype: L{NetworkProtocolDAO}
        """
        return WindowsNetworkProtocolDAO()
    