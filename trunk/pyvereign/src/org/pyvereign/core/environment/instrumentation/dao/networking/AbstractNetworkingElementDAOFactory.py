from org.pyvereign.core.environment.dao.networking.NetworkingElementDAOFactory import NetworkingElementDAOFactory
from org.pyvereign.core.environment.dao.networking.windows.WindowsNetworkingElementDAOFactory import WindowsNetworkingElementDAOFactory

class AbstractNetworkingElementDAOFactory(NetworkingElementDAOFactory):
    """
    Defines the abstract class for NetworkingElementDAOFactory interface.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    __factories = {"nt": WindowsNetworkingElementDAOFactory}
    
    def getNetworkingElementDAOFactory(self, type):
        """
        Gets an instance of NetworkingElementDAOFactory interface.
        @param type: the type of factory.
        @type type: str
        @return: Returns an instance of NetworkingElementDAOFactory interface.
        @rtype: L{NetworkingElementDAOFactory}
        """
        if not isinstance(type, str):
            raise TypeError("type parameter is not an instance of str class.")
        
        return AbstractNetworkingElementDAOFactory.__factories[type]() 
    
    getNetworkingElementDAOFactory = classmethod(getNetworkingElementDAOFactory)
    
       
    