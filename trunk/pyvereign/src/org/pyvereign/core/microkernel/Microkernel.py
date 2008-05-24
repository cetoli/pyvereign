from org.pyvereign.core.platform.CompositeModule import CompositeModule
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.id.InternalServerID import InternalServerID
from org.pyvereign.core.microkernel.InternalServer import InternalServer
from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.communication.Communication import Communication

class Microkernel(CompositeModule):
    """
    Defines the microkernel.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
        
      
    def init(self):
        CompositeModule.init(self)
        self._internalServers = {}
        """
        @ivar: Internal servers of microkernel.
        @type: dict  
        """
        
    def initialize(self, owner = None, id = None, context = None):
        environmentID = IDFactory().createInternalServerID(Constants.ENVIRONMENT)
        self._internalServers[environmentID.getFormatedID()] = Environment()
        self._internalServers[environmentID.getFormatedID()].initialize(self, environmentID, None)
        
        communicationID = IDFactory().createInternalServerID(Constants.COMMUNICATION)
        self._internalServers[communicationID.getFormatedID()] = Communication()
        self._internalServers[communicationID.getFormatedID()].initialize(self, communicationID, None)
        
        self._status = self.INITIALIZED
        
    def start(self, params):
        for server in self._internalServers.values():
            server.start(params)
    
    
    def executeMecanism(self, internalServerName, serviceRequest, serviceResponse):
        """
        Executes description
        @return: Returns description
        @rtype: rtype
        """
        try:
            environmentID = IDFactory().createInternalServerID(internalServerName)
            server = self._internalServers[environmentID.getFormatedID()]
            server.executeService(serviceRequest, serviceResponse)
        except:
            raise
        
    def addModule(self, id, module):
        if not isinstance(id, InternalServerID):
            raise TypeError("id parameter is not an instance of InternalServerID class.")
        if not isinstance(module, InternalServer):
            raise TypeError("module parameter is not an instance of InternalServer class.")
        self._internalServers[id.getFormatedID()] = module
        return self._internalServers[id.getFormatedID()]
        
    def removeModule(self, id):
        if not isinstance(id, InternalServerID):
            raise TypeError("id parameter is not an instance of InternalServerID class.")
        coreService = self._internalServers[id.getFormatedID()]
        del self._internalServers[id.getFormatedID()]
        return coreService
    
    def countModules(self):
        return len(self._internalServers)
    
    def clearModules(self):
        self._internalServers.clear()
    
    def getModule(self, id):
        if not isinstance(id, InternalServerID):
            raise TypeError("id parameter is not an instance of InternalServerID class.")
        return self._internalServers[id.getFormatedID()]
    
    def hasModule(self, id):
        if not isinstance(id, InternalServerID):
            raise TypeError("id parameter is not an instance of InternalServerID class.")
        return self._internalServers.has_key(id.getFormatedID())
        