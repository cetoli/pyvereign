from org.pyvereign.core.configuration.configurator.AbstractConfigurator import AbstractConfigurator
from org.pyvereign.util.ClassLoader import ClassLoader
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.service.ConcreteNetworkingService import ConcreteNetworkingService
from org.pyvereign.core.id.IDFactory import IDFactory

class EnvironmentConfigurator(AbstractConfigurator):
    """
    Defines the configurator of Environment internal server.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
        
    def createObjects(self):
        properties = self._configuration.getProperty("services")
        props = properties.getProperties()
        
        for p in props:
            module = p.getProperty("module") 
            className = p.getProperty("classname")
            clazz = ClassLoader.loadClass(module.getValue(), className.getValue())
            self._repository.addObject(p.getName(), clazz)
            
    def configureObject(self, obj, configurationType = None):
        if not self._repository.hasObject(Constants.NETWORKING_SERVICE):
            raise StandardError()
        serviceClass = self._repository.getObject(Constants.NETWORKING_SERVICE)
        service = serviceClass()
        id = IDFactory().createCoreServiceID(obj, service.getName())
        obj.addModule(id, service)
        
        if not self._repository.hasObject(Constants.TRANSPORT_SERVICE):
            raise StandardError()
        
        serviceClass = self._repository.getObject(Constants.TRANSPORT_SERVICE)
        service = serviceClass()
        id = IDFactory().createCoreServiceID(obj, service.getName())
        obj.addModule(id, service)
        
        return obj     
    