from org.pyvereign.core.id.ID import ID
import sha

class InternalServerID(ID):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def __init__(self, internalServerName):
        self._id = sha.new(internalServerName).hexdigest()
    
    def getIDFormated(self):
        """
        Gets the formated identifier.
        
        @return: The formated identifier.
        @rtype: L{str}
        """
        return "urn:pyvereign:core:internalserver:"+self._id