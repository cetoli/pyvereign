from org.pyvereign.core.platform.SimpleModule import SimpleModule

class AbstractService(SimpleModule):
    """
    Defines the abstract class for platform services.
    
    @author: Fabricio
    @since: 18/03/2008 - 14:13:00
    @version: 0.0.1
    """
    
    def getContext(self):
        return self._context