from org.pyvereign.core.configuration.configurator.AbstractConfigurator import AbstractConfigurator
from org.pyvereign.util.ClassLoader import ClassLoader

class MessageFormatFactoryConfigurator(AbstractConfigurator):
    """
    Defines the configurator of MessageFormatFactory.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
        
    def createObjects(self):
        properties = self._configuration.getProperty("formats")
        props = properties.getProperties()
        
        for p in props:
            module = p.getProperty("module") 
            className = p.getProperty("classname")
            clazz = ClassLoader.loadClass(module.getValue(), className.getValue())
            self._repository.addObject(p.getName(), clazz)
    
    def configureObject(self, obj, configurationType = None):
        for k, v in self._repository.getObjects():
            obj._registerMessageFormatClass(k, v)
        return obj
    