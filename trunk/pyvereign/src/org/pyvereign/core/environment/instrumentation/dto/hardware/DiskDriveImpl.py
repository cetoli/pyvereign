from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractDiskDrive import AbstractDiskDrive

class DiskDriveImpl(AbstractDiskDrive):
    """
    Defines the default implementation for disk drives.
    
    @author: Fabricio
    @since: 21/03/2008 - 23:22:24
    @version: 0.0.1
    """
    
    def __init__(self, values):
        self.init(values)