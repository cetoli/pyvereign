from atlas.api.microkernel.Microkernel import Microkernel

class HardwareFactory(object):
    
    MACHINE = "machine"
    NETWORK_CONTROLLER = "network_controller"
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance._family = "default"
            cls.instance.initialize()
        
        return cls.instance
    
    def setFamily(self, family):
        self._family = family
        self.initialize()
        return self._family
    
    def registerHardwareClass(self, name, classObject):
        self._hardwareClasses[name] = classObject
        return self._hardwareClasses[name]
    
    def unregisterHardwareClass(self, name):
        clazz = self._hardwareClasses[name]
        del self._hardwareClasses[name]
        return clazz
    
    def clearHardwareClasses(self):
        self._hardwareClasses.clear()
        
    def createHardware(self, type):
        return self._hardwareClasses[type]()
    
    def initialize(self):
        self._hardwareClasses = {}
        try:
            if Microkernel().getStatus() == Microkernel.NON_UNITIALIZED:
                Microkernel().initialize()
            if Microkernel().getStatus() == Microkernel.INITIALIZED:
                Microkernel().start()
                
            Microkernel().executeMecanism("InternalConfiguration", "configurator", "configureHardwareFactory", self, self._family)
        except:
            raise 
    