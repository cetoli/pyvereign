from atlas.api.conf.configurator.AbstractConfigurator import AbstractConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
from atlas.util.ClassLoader import ClassLoader
from atlas.api.exception.ConfigurationError import ConfigurationError

class EnvironmentConfigurator(AbstractConfigurator):
    
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        AbstractConfigurator.initialize(self)
        
    def createObjects(self):
        try:
            properties = self._configuration.getProperties()
            for x in properties:
                repX = DefaultObjectRepository()
                for y in x.getProperties():
                    repY = DefaultObjectRepository()
                    for z in y.getProperties():
                        repZ = DefaultObjectRepository()
                        for i in z.getProperties():
                            if not i.isComposite():
                                repZ.addObject(i.getName(), i.getValue())
                            else:
                                repI = DefaultObjectRepository()
                                for j in i.getProperties():
                                    repI.addObject(j.getName(), j.getValue())
                                repZ.addObject(i.getName(), repI)
                            
                        repY.addObject(z.getName(), repZ)
                    repX.addObject(y.getName(), repY)
                
                self._repository.addObject(x.getName(), repX)
            return True
        except:
            raise
    
    def configureObject(self, obj, configurationType):
        if not obj:
            raise RuntimeError("Invalid parameter")
        if not configurationType:
            raise RuntimeError("Invalid parameter")
        
        obj.clearServices()
        
        if not self._repository.hasObject("hardware"):
            raise ConfigurationError("hardware property was not found.")
        
        hardware = self._repository.getObject("hardware")
        
        for k, v in hardware.getObjects():
            if not v.hasObject("service"):
                raise ConfigurationError("service property was not found.")
            service = v.getObject("service")
            if not v.hasObject("datasource"):
                raise ConfigurationError("datasource property was not found.")
            datasource = v.getObject("datasource")
            serviceClass = ClassLoader.loadClass(service.getObject("module"), service.getObject("classname"))
            conf = datasource.getObject(configurationType)
            datasourceClass = ClassLoader.loadClass(conf.getObject("module"), conf.getObject("classname"))
            
            serviceObj = serviceClass()
            serviceObj.setDataSource(datasourceClass())
            
            obj.registerService(service.getObject("name"), serviceObj)
            
        networking = self._repository.getObject("networking")
        
        for k, v in networking.getObjects():
            if not v.hasObject("service"):
                raise ConfigurationError("service property was not found.")
            service = v.getObject("service")
            if not v.hasObject("datasource"):
                raise ConfigurationError("datasource property was not found.")
            datasource = v.getObject("datasource")
            serviceClass = ClassLoader.loadClass(service.getObject("module"), service.getObject("classname"))
            conf = datasource.getObject(configurationType)
            datasourceClass = ClassLoader.loadClass(conf.getObject("module"), conf.getObject("classname"))
            
            serviceObj = serviceClass()
            serviceObj.setDataSource(datasourceClass())
            
            obj.registerService(service.getObject("name"), serviceObj)
            
        return obj
    