from org.pyvereign.core.configuration.configurator.AbstractConfigurator import AbstractConfigurator
from org.pyvereign.util.ClassLoader import ClassLoader

class HardwareDTOFactoryConfigurator(AbstractConfigurator):
    """
    Defines a configurator for a HadwareDTOFactory object. 
    
    @author: Fabricio
    @since: 25/03/2008 - 01:23:56
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
    
    def createObjects(self):
        repositories = self._configuration.getProperty("hardwares")
        properties = repositories.getProperties()
        for p in properties:
            module = p.getProperty("module") 
            className = p.getProperty("classname")
            clazz = ClassLoader.loadClass(module.getValue(), className.getValue())
            self._repository.addObject(p.getName(), clazz)
    
    def configureObject(self, obj, configurationType = None):
        for k, v in self._repository.getObjects():
            obj._registerHardwareClass(k, v)
        return obj
    