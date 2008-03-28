from org.pyvereign.core.platform.CoreService import CoreService

class DefaultCoreService(CoreService):
    """
    Defines the default implementation for CoreService abstract class.
    
    @author: Fabricio
    @since: 18/03/2008 - 15:20:54
    @version: 0.0.1
    """
    
    def __init__(self):
        """
        Initializes DefaulfCoreService objects.
        
        @return: a instance of DefaultCoreService
        @rtype: L{DefaultCoreService}
        """
        self.init()
        
    def start(self, args = []):
        CoreService.start(self, args)
        
    def getInterface(self, type = None):
        return CoreService.getInterface(self, type)
    
    