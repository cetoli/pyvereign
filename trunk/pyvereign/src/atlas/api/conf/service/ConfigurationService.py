from atlas.api.conf.service.HardwareFactoryConfigurator import HardwareFactoryConfigurator

class ConfigurationService:
    
    def initialize(self, *params):
        self._hardwareFactoryConfigurator = HardwareFactoryConfigurator()
        self._hardwareFactoryConfigurator.setFilename("hardwares.yaml")
    
    def start(self, *params):
        self._hardwareFactoryConfigurator.loadConfiguration()
        self._hardwareFactoryConfigurator.createObjects()
    
    def stop(self):
        pass
    
    def configureHardwareFactory(self, hardwareFactory, family):
        return self._hardwareFactoryConfigurator.configureObject(hardwareFactory, family)
    
    def getName(self):
        return "configuration"