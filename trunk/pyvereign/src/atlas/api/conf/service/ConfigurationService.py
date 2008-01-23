from atlas.api.conf.service.HardwareFactoryConfigurator import HardwareFactoryConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository

class ConfigurationService(object):
    
    def initialize(self, *params):
        self._hardwareFactoryConfigurator = HardwareFactoryConfigurator()
        self._hardwareFactoryConfigurator.setFilename("hardwares.yaml")
        self._hardwareFactoryConfigurator.setObjectRepository(DefaultObjectRepository())
    
    def start(self, *params):
        self._hardwareFactoryConfigurator.loadConfiguration()
        self._hardwareFactoryConfigurator.createObjects()
    
    def stop(self):
        pass
    
    def configureHardwareFactory(self, hardwareFactory, family):
        return self._hardwareFactoryConfigurator.configureObject(hardwareFactory, family)
    
    def getName(self):
        return "configurator"