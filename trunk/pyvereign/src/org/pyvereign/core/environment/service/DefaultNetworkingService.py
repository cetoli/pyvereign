from org.pyvereign.core.environment.service.AbstractNetworkingService import AbstractNetworkingService
from org.pyvereign.core.environment.instrumentation.dao.networking.AbstractNetworkingElementDAOFactory import AbstractNetworkingElementDAOFactory
from org.pyvereign.core.exception.ModuleError import ModuleError
import os

class DefaultNetworkingService(AbstractNetworkingService):
    """
    Defines the default implementation of NetworkingService.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
    
    def initialize(self, owner, id, context):
        AbstractNetworkingService.initialize(self, owner, id, context)
        factory = AbstractNetworkingElementDAOFactory.getNetworkingElementDAOFactory(os.name)
        self._dao = factory.createNetworkProtocolDAO()
    
    def getNetworkProtocols(self):
        if not self._status == DefaultNetworkingService.STARTED:
            raise ModuleError("The service is not started.")
        
        try:
            return self._dao.retrieveNetworkProtocols()
        except:
            raise