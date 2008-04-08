from org.pyvereign.core.environment.TransportService import TransportService
from org.pyvereign.core.platform.CoreService import CoreService

class AbstractTransportService(TransportService, CoreService):
    """
    Defines the common interface of transport services.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self):
        CoreService.init(self)
        self._protocols = {}
        self._streamListeners = {}
    