from atlas.api.conf.configurator.HardwareFactoryConfigurator import HardwareFactoryConfigurator

class ConfiguratorFactory(object):
    
    HARDWARE = "HARDWARE"
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.initialize()
            
        return cls.instance
    
    def initialize(self):
        self._configurators = {}
        self._configurators[ConfiguratorFactory.HARDWARE] = HardwareFactoryConfigurator
    
    def createConfigurator(self, type):
        return self._configurators[type]()