from atlas.api.conf.configurator.EnvironmentConfigurator import EnvironmentConfigurator
from atlas.api.conf.configurator.HardwareFactoryConfigurator import HardwareFactoryConfigurator

class ConfiguratorFactory(object):
    
    HARDWARE = "HARDWARE"
    ENVIRONMENT = "ENVIRONMENT"
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
            
        return cls.instance
    
    def initialize(self):
        self._configurators = {}
        self._configurators[ConfiguratorFactory.HARDWARE] = HardwareFactoryConfigurator
        self._configurators[ConfiguratorFactory.ENVIRONMENT] = EnvironmentConfigurator
    
    def createConfigurator(self, type):
        return self._configurators[type]()