from org.pyvereign.core.id.ID import ID
import sha

class CoreServiceID(ID):
    """
    Define the identifier of core services.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, serviceName):
        self._id = sha.new(serviceName).hexdigest()
        
    def getIDFormat(self):
        """
        Gets the formated identifier.
        
        @return: The formated identifier.
        @rtype: L{str}
        """
        return "urn:pyvereign:core:"+self._id
    