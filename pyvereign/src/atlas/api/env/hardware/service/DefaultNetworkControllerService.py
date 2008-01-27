from atlas.api.env.hardware.service.AbstractNetworkControllerService import AbstractNetworkControllerService
from sets import ImmutableSet

class DefaultNetworkControllerService(AbstractNetworkControllerService):
    
    def __init__(self):
        self.initialize()
    
    def initialize(self, *params):
        AbstractNetworkControllerService.initialize(self)
        
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
        return "NetworkControllerService"