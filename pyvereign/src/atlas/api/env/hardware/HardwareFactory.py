from atlas.api.microkernel.Microkernel import Microkernel

class HardwareFactory(object):
    
    MACHINE = "machine"
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance._hardwareClasses = {}
        
        return cls.instance
    
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
        try:
            Microkernel()
        except:
            raise
    