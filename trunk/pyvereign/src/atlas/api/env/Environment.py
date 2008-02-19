from atlas.api.microkernel.AbstractInternalServer import AbstractInternalServer
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
from atlas.api.conf.configurator.ConfiguratorFactory import ConfiguratorFactory
import os

class Environment(AbstractInternalServer):
    
    def __init__(self):
        self._name = "environment"
        
    def initialize(self, *params):
        AbstractInternalServer.initialize(self, *params)
        
        configurator = ConfiguratorFactory().createConfigurator(ConfiguratorFactory.ENVIRONMENT)
        try:
            configurator.setFilename("environment.yaml")
            configurator.setObjectRepository(DefaultObjectRepository())
            configurator.loadConfiguration()
            configurator.createObjects()
            configurator.configureObject(self, os.name)
            
            for service in self._services.values():
                service.initialize(self)
        except:
            raise        
    
    def start(self, *params):
        for service in self._services.values():
            service.start()
            
    def stop(self):
        for service in self._services.values():
            service.stop()
    
    

