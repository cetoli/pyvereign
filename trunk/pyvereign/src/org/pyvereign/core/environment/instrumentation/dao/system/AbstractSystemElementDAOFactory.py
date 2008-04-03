from org.pyvereign.core.environment.instrumentation.dao.system.SystemElementDAOFactory import SystemElementDAOFactory
from org.pyvereign.core.environment.instrumentation.dao.system.windows.WindowsSystemElementDAOFactory import WindowsSystemElementDAOFactory

class AbstractSystemElementDAOFactory(SystemElementDAOFactory):
    """
    Defines the common implementation for SystemElementDAOFactory interface.
    
    @author: Fabricio
    @since: 29/03/2008 - 17:05:46
    @version: 0.0.1
    """
    
    __factories = {"nt": WindowsSystemElementDAOFactory}
    
    def getSystemElementDAOFactory(self, type):
        """
        Creates an instance of SystemElementDAOFactory interface.
        @param type: the type of system element dao factory.
        @type type: L{str}
        @return: Returns an instance of SystemElementDAOFactory interface.
        @rtype: L{SystemElementDAOFactory}
        """
        return AbstractSystemElementDAOFactory.__factories[type]()
    
    getSystemElementDAOFactory = classmethod(getSystemElementDAOFactory)
    