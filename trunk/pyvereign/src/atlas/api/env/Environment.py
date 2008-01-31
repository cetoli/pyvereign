from atlas.api.microkernel.AbstractInternalServer import AbstractInternalServer
from atlas.api.conf.configurator.EnvironmentConfigurator import EnvironmentConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
import os

class Environment(AbstractInternalServer):
    
    def __init__(self):
        print ""
        
    def initialize(self, *params):
        AbstractInternalServer.initialize(self, *params)
        
        configurator = EnvironmentConfigurator()
        try:
            configurator.setFilename("environment.yaml")
            configurator.setObjectRepository(DefaultObjectRepository())
            configurator.loadConfiguration()
            configurator.createObjects()
            configurator.configureObject(self, os.name)
        except:
            raise
        
#        machine = DefaultMachineService()
#        self._services[machine.getName()] = machine
#        machine.initialize()
#        machine.setDataSource(WindowsMachineDataSource())
#        
#        networkController = DefaultNetworkControllerService()
#        self._services[networkController.getName()] = networkController
#        networkController.initialize()
#        networkController.setDataSource(WindowsNetworkControllerDataSource())
#        
#        protocol = DefaultProtocolService()
#        self._services[protocol.getName()] = protocol
#        protocol.initialize()
#        protocol.setDataSource(WindowsProtocolDataSource())
        
    
    def start(self, *params):
        for service in self._services.values():
            service.start()
    
    

