from atlas.api.env.service.AbstractHardwareService import AbstractHardwareService
from atlas.api.env.service.NetworkControllerService import NetworkControllerService

class AbstractNetworkControllerService(AbstractHardwareService, NetworkControllerService):
    
    def initialize(self, *params):
        AbstractHardwareService.initialize(self)
        self._controllers = {}
        
    def start(self, *params):
        if not self._dataSource:
            raise RuntimeError("Data source is none.")
        ctrls = self._dataSource.retrieveNetworkControllers()
        for controller in ctrls:
            self._controllers[controller.getMACAddress()] = controller