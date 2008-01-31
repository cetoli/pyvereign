from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
from atlas.api.conf.configurator.ConfiguratorFactory import ConfiguratorFactory

class HardwareFactory(object):
    
    MACHINE = "machine"
    NETWORK_CONTROLLER = "network_controller"
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
        
        return cls.instance
    
    def initialize(self):
        self._family = "default"
        self._hardwareClasses = {}
        configurator = ConfiguratorFactory().createConfigurator(ConfiguratorFactory.HARDWARE)
        configurator.setFilename("hardwares.yaml")
        configurator.setObjectRepository(DefaultObjectRepository())
        configurator.loadConfiguration()
        configurator.createObjects()
        configurator.configureObject(self, self._family)
        
    def setFamily(self, family):
        self._family = family
        self.initialize()
        return self._family
    
    def registerHardwareClass(self, name, classObject):
        self._hardwareClasses[name] = classObject
        return self._hardwareClasses[name]
    
    def unregisterHardwareClass(self, name):
        clazz = self._hardwareClasses[name]
        del self._hardwareClasses[name]
        return clazz
    
    def clearHardwareClasses(self):
        self._hardwareClasses.clear()
        
    def createHardware(self, type):
        return self._hardwareClasses[type]()
    
    