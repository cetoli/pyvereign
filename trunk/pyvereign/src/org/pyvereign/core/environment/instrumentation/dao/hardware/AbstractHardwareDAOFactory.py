from org.pyvereign.core.environment.instrumentation.dao.hardware.HardwareDAOFactory import HardwareDAOFactory
from org.pyvereign.core.environment.instrumentation.dao.hardware.windows.WindowsHardwareDAOFactory import WindowsHardwareDAOFactory

class AbstractHardwareDAOFactory(HardwareDAOFactory):
    """
    Defines the abastract class for HardwareDAOFactory interface.
    
    @author: Fabricio
    @since: 28/03/2008 - 11:56:55
    @version: 0.0.1
    """
    
    factories = {"nt": WindowsHardwareDAOFactory}
    
    def getHardwareDAOFactory(self, type):
        """
        Creates an instance of HardwareDAOFactory.
        @param type: the type of HardwareDAOFactory
        @type type: L{str}
        @return: Returns an instance of HardwareDAOFactory.
        @rtype: HardwareDAOFactory
        """
        if not isinstance(type, str):
            raise TypeError("type parameter is not an instance of str class.")
        return AbstractHardwareDAOFactory.factories[type]()
    
    getHardwareDAOFactory = classmethod(getHardwareDAOFactory)
        
        