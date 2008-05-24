from org.pyvereign.core.environment.service.NetworkingService import NetworkingService
from org.pyvereign.core.platform.CoreService import CoreService
from org.pyvereign.util.Constants import Constants

class AbstractNetworkingService(NetworkingService, CoreService):
    """
    Defines the common implementation for NetworkingService objects.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self):
        CoreService.init(self)
        self._name = Constants.NETWORKING_SERVICE
    