from org.pyvereign.core.environment.dao.system.SystemElementDAOFactory import SystemElementDAOFactory
from org.pyvereign.core.environment.dao.system.windows.WindowsProcessDAO import WindowsProcessDAO

class WindowsSystemElementDAOFactory(SystemElementDAOFactory):
    """
    Defines the implementation for the data access object creation of system element . 
    
    @author: Fabricio
    @since: 29/03/2008 - 16:58:16
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def createProcessDAO(self):
        """
        Creates an instance of ProcessDAO
        @return: Returns an instance of ProcessDAO
        @rtype: L{ProcessDAO}
        """
        return WindowsProcessDAO()
    