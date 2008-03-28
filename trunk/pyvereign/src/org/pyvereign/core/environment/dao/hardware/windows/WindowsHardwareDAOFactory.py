from org.pyvereign.core.environment.dao.hardware.HardwareDAOFactory import HardwareDAOFactory
from org.pyvereign.core.environment.dao.hardware.windows.WindowsDiskDriveDAO import WindowsDiskDriveDAO
from org.pyvereign.core.environment.dao.hardware.windows.WindowsMachineDAO import WindowsMachineDAO
from org.pyvereign.core.environment.dao.hardware.windows.WindowsPhysicalMemoryDAO import WindowsPhysicalMemoryDAO
from org.pyvereign.core.environment.dao.hardware.windows.WindowsProcessorDAO import WindowsProcessorDAO

class WindowsHardwareDAOFactory(HardwareDAOFactory):
    """
    Define the implementation of HardwareDAOFactory for Windows SO. 
    
    @author: Fabricio
    @since: 28/03/2008 - 11:42:13
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def createDiskDriveDAO(self):
        """
        Creates an instance of DiskDriveDAO interface.
        @return: Returns an instance of DiskDriveDAO interface.
        @rtype: L{DiskDriveDAO}
        """
        return WindowsDiskDriveDAO()
    
    def createMachineDAO(self):
        """
        Creates an instance of MachineDAO interface.
        @return: Returns an instance of MachineDAO interface.
        @rtype: L{MachineDAO}
        """
        return WindowsMachineDAO() 
    
    def createPhysicalMemoryDAO(self):
        """
        Creates an instance of PhysicalMemoryDAO interface.
        @return: Returns an instance of PhysicalMemoryDAO interface.
        @rtype: L{PhysicalMemoryDAO}
        """
        return WindowsPhysicalMemoryDAO()
    
    def createProcessorDAO(self):
        """
        Creates an instance of ProcessorDAO interface.
        @return: Returns an instance of ProcessorDAO interface.
        @rtype: L{ProcessorDAO}
        """
        return WindowsProcessorDAO()
        