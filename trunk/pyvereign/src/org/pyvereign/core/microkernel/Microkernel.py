from org.pyvereign.core.platform.CompositeModule import CompositeModule
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.id import IDFactory
from org.pyvereign.core.id.InternalServerID import InternalServerID
from org.pyvereign.core.microkernel.InternalServer import InternalServer

class Microkernel(CompositeModule):
    """
    Defines the microkernel.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
        self._internalServers = {}
        """
        @ivar: Internal servers of microkernel.
        @type: dict  
        """
        
    def initialize(self, owner = None, id = None, context = None):
        environment = self._internalServers[Constants.ENVIRONMENT]
        environmentID = IDFactory().createInternalServerID(Constants.ENVIRONMENT)
        
        
    def executeMecanism(self, internalServerName, serviceRequest, serviceResponse):
        """
        Executes description
        @return: Returns description
        @rtype: rtype
        """
        pass
    
    def addModule(self, id, module):
        if not isinstance(id, InternalServerID):
            raise TypeError("id parameter is not an instance of InternalServerID class.")
        if not isinstance(module, InternalServer):
            raise TypeError("module parameter is not an instance of InternalServer class.")
        self._internalServers[id.getIDFormated()] = module
        return self._internalServers[id.getIDFormated()]
        
    def removeModule(self, id):
        if not isinstance(id, InternalServerID):
            raise TypeError("id parameter is not an instance of InternalServerID class.")
        coreService = self._internalServers[id.getIDFormated()]
        del self._internalServers[id.getIDFormated()]
        return coreService
    
    def countModules(self):
        return len(self._internalServers)
    
    def clearModules(self):
        self._internalServers.clear()
    
    def getModule(self, id):
        if not isinstance(id, InternalServerID):
            raise TypeError("id parameter is not an instance of InternalServerID class.")
        return self._internalServers[id.getIDFormated()]
        