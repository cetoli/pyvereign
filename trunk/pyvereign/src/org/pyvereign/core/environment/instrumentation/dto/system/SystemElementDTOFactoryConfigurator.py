from org.pyvereign.core.configuration.configurator.AbstractConfigurator import AbstractConfigurator
from org.pyvereign.util.ClassLoader import ClassLoader


class SystemElementDTOFactoryConfigurator(AbstractConfigurator):
    """
    Defines the configurator of a SystemElementDTOFactory object. 
    
    @author: Fabricio
    @since: 29/03/2008 - 14:23:08
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
    
    def createObjects(self):
        repositories = self._configuration.getProperty("system_elements")
        properties = repositories.getProperties()
        for p in properties:
            module = p.getProperty("module") 
            className = p.getProperty("classname")
            clazz = ClassLoader.loadClass(module.getValue(), className.getValue())
            self._repository.addObject(p.getName(), clazz)
    
    def configureObject(self, obj, configurationType = None):
        from org.pyvereign.core.environment.instrumentation.dto.system.SystemElementDTOFactory import SystemElementDTOFactory
        if not isinstance(obj, SystemElementDTOFactory):
            raise TypeError()
        obj._clearSystemElementClasses()
        for k, v in self._repository.getObjects():
            obj._registerSystemElementClass(k, v)
        return obj