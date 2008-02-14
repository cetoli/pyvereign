from atlas.api.env.hardware.service.AbstractHardwareService import AbstractHardwareService
from atlas.api.env.hardware.service.NetworkControllerService import NetworkControllerService
from sets import ImmutableSet

class AbstractNetworkControllerService(AbstractHardwareService, NetworkControllerService):
    
    def initialize(self, environment):
        AbstractHardwareService.initialize(self, environment)
        self._controllers = {}
        
    def start(self, *params):
        if not self._dataSource:
            raise RuntimeError("Data source is none.")
        ctrls = self._dataSource.retrieveNetworkControllers()
        for controller in ctrls:
            self._controllers[controller.getMACAddress()] = controller
    
    def getNetworkControllers(self):
        return ImmutableSet(self._controllers.itervalues())
    
    def getNetworkController(self, macAddress):
        return self._controllers[macAddress]
    
    def getMACAddresses(self):
        addresses = [addr.getMACAddress() for addr in self._controllers.values()]
        return addresses
    
    def getIPAddresses(self):
        addresses = [addr.getIPAddress() for addr in self._controllers.values()]
        return addresses
    
    def getName(self):
        return "network_controller"