from atlas.api.conf.configurator.AbstractConfigurator import AbstractConfigurator
from atlas.api.conf.repository.DefaultObjectRepository import DefaultObjectRepository
from atlas.util.ClassLoader import ClassLoader

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
        obj.clearServices()
        
        hardware = self._repository.getObject("hardware")
        
        for k, v in hardware.getObjects():
            service = v.getObject("service")
            datasource = v.getObject("datasource")
            serviceClass = ClassLoader.loadClass(service.getObject("module"), service.getObject("classname"))
            conf = datasource.getObject(configurationType)
            datasourceClass = ClassLoader.loadClass(conf.getObject("module"), conf.getObject("classname"))
            
            serviceObj = serviceClass()
            serviceObj.setDataSource(datasourceClass())
            
            obj.registerService(service.getObject("name"), serviceObj)
            
        networking = self._repository.getObject("networking")
        
        for k, v in networking.getObjects():
            service = v.getObject("service")
            datasource = v.getObject("datasource")
            serviceClass = ClassLoader.loadClass(service.getObject("module"), service.getObject("classname"))
            conf = datasource.getObject(configurationType)
            datasourceClass = ClassLoader.loadClass(conf.getObject("module"), conf.getObject("classname"))
            
            serviceObj = serviceClass()
            serviceObj.setDataSource(datasourceClass())
            
            obj.registerService(service.getObject("name"), serviceObj)
            
        return obj
    