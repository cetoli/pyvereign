from org.pyvereign.core.configuration.configurator.AbstractConfigurator import AbstractConfigurator
from org.pyvereign.util.ClassLoader import ClassLoader
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.communication.endpoint.service.ConcreteEndpointService import ConcreteEndpointService
from org.pyvereign.core.communication.topology.service.ConcreteTopologyControlService import ConcreteTopologyControlService


class CommunicationConfigurator(AbstractConfigurator):
    
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
        from org.pyvereign.core.communication.Communication import Communication
        if not isinstance(obj, Communication):
            raise TypeError()
        
        if not self._repository.hasObject(Constants.ENDPOINT_SERVICE):
            raise StandardError()
        
        serviceClass = self._repository.getObject(Constants.ENDPOINT_SERVICE)
        service = serviceClass()
        id = IDFactory().createCoreServiceID(obj, service.getName())
        obj.addModule(id, ConcreteEndpointService(service))
        
        if not self._repository.hasObject(Constants.TOPOLOGY_CONTROL_SERVICE):
            raise StandardError()
        
        serviceClass = self._repository.getObject(Constants.TOPOLOGY_CONTROL_SERVICE)
        service = serviceClass()
        id = IDFactory().createCoreServiceID(obj, Constants.TOPOLOGY_CONTROL_SERVICE)
        obj.addModule(id, ConcreteTopologyControlService(service))
        
        return obj
        
    
    