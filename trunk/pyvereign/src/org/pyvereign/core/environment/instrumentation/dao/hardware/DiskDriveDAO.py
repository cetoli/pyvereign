class DiskDriveDAO(object):
    """
    Defines the interface of disk drive data access object. 
    
    @author: Fabricio
    @since: 25/03/2008 - 11:52:26
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def retrieveDiskDrives(self):
        """
        Retrieves disk drives which are installed in user machine.
        @return: Returns disk drives which are installed in user machine.
        @rtype: ImmutableSet
        """
        pass
    