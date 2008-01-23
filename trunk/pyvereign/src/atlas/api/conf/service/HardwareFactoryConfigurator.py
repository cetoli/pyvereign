from atlas.api.conf.AbstractConfigurator import AbstractConfigurator
from atlas.util.ClassLoader import ClassLoader
from atlas.api.conf.DefaultObjectRepository import DefaultObjectRepository

class HardwareFactoryConfigurator(AbstractConfigurator):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        AbstractConfigurator.initialize(self)
    
    def createObjects(self):
        try:
            for prop in self._configuration.getProperties():
                repository = DefaultObjectRepository()
                for p in prop.getProperties():
                    module = p.getProperty("module")
                    className = p.getProperty("classname")
                    
                    clazz = ClassLoader.loadClass(module.getValue(), className.getValue())
                    
                    repository.addObject(p.getName(), clazz)
                self._repository.addObject(prop.getName(), repository)
            return True
        except:
            raise
    
    def configureObject(self, obj, configurationType):
        obj.clearHardwareClasses()
        
        repository = self._repository.getObject(configurationType)
        
        for k, y in repository.getObjects():
            obj.registerHardwareClass(k, y)
        
        return obj
        