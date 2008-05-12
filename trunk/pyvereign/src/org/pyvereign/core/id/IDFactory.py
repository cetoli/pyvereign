from org.pyvereign.core.id.CoreServiceID import CoreServiceID
from org.pyvereign.core.id.InternalServerID import InternalServerID
class IDFactory(object):
    """
    Defines a factory for identifiers of platform.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
        return cls.instance
    
    def createCoreServiceID(self, internalServerName, serviceName):
        """
        Creates an instance of CoreServiceID interface.
        @return: Returns an instance of CoreServiceID interface.
        @rtype: L{CoreServiceID}
        """
        if not isinstance(serviceName, str):
            raise TypeError("service parameter is not an instance of str class.")
        if not isinstance(internalServerName, str):
            raise TypeError("internalServer is not an instance of str class.")
        return CoreServiceID(internalServerName, serviceName)

    def createInternalServerID(self, internalServerName):
        """
        Creates an instance of InternalServerID.
        @return: Returns an instance of InternalServerID.
        @rtype: L{InternalServerID}
        """
        return InternalServerID(internalServerName)
        