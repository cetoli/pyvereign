class HardwareDAOFactory(object):
    """
    Defines the factory interface for the creation of hardware DAOs.
    
    @author: Fabricio
    @since: 25/03/2008 - 12:01:15
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def createDiskDriveDAO(self):
        """
        Creates an instance of DiskDriveDAO interface.
        @return: Returns an instance of DiskDriveDAO interface.
        @rtype: L{DiskDriveDAO}
        """
        pass
    
    def createMachineDAO(self):
        """
        Creates an instance of MachineDAO interface.
        @return: Returns an instance of MachineDAO interface.
        @rtype: L{MachineDAO}
        """
        pass
    
    def createPhysicalMemoryDAO(self):
        """
        Creates an instance of PhysicalMemoryDAO interface.
        @return: Returns an instance of PhysicalMemoryDAO interface.
        @rtype: L{PhysicalMemoryDAO}
        """
        pass
    
    def createProcessorDAO(self):
        """
        Creates an instance of ProcessorDAO interface.
        @return: Returns an instance of ProcessorDAO interface.
        @rtype: L{ProcessorDAO}
        """
        pass
        """
        verb description
        @return: Returns description
        @rtype: type
        """
        
        
    