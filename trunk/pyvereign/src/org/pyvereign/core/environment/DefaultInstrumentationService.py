from org.pyvereign.core.environment.AbstractInstrumentationService import AbstractInstrumentationService
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.instrumentation.dao.networking.AbstractNetworkingElementDAOFactory import AbstractNetworkingElementDAOFactory
import os

class DefaultInstrumentationService(AbstractInstrumentationService):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def __init__(self):
        self.init()
        self._name = Constants.INSTRUMENTATION_SERVICE
        
    def getNetworkProtocols(self):
        factory = AbstractNetworkingElementDAOFactory.getNetworkingElementDAOFactory(os.name)
        
        dao = factory.createNetworkProtocolDAO()
        return dao.retrieveNetworkProtocols()