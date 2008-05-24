from org.pyvereign.core.id.ID import ID
import sha

class CoreServiceID(ID):
    """
    Define the identifier of core services.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, layerName, serviceName):
        if not isinstance(layerName, str):
            raise TypeError("layerName parameter is not an instance of str class.")
        if not isinstance(serviceName, str):
            raise TypeError("serviceName parameter is not an instance of str class.")
        self._id = sha.new(serviceName + layerName).hexdigest()
        
    def getFormatedID(self):
        """
        Gets the formated identifier.
        
        @return: The formated identifier.
        @rtype: L{str}
        """
        return "urn:pyvereign:core:service:"+self._id
    