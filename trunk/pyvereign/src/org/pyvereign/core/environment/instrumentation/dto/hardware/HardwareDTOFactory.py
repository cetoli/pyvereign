from org.pyvereign.core.exception.HardwareDTOFactoryError import HardwareDTOFactoryError
class HardwareDTOFactory(object):
    """
    Implements a factory for creating instances of Hardware interface. 
    
    @author: Fabricio
    @since: 25/03/2008 - 00:37:28
    @version: 0.0.1
    """
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            """
            @cvar: unique instance of class.
            @type: L{HardwareDTOFactory}
            """
            cls.instance.init()
        return cls.instance
    
    def init(self):
        self._hardwareClasses = {}
        """
        @ivar: the map of hardware classes.
        @type: dict
        """
        
    def createHardware(self, type, values):
        """
        Creates instances of Hardware interface.
        @param type: the type of Hardware.
        @type type: str
        @param values: the initialization values
        @type values: dict
        @return: Returns an intance of Hardware.
        @rtype: L{Hardware}
        """
        if not isinstance(type, str):
            raise TypeError("type parameter is not an instance of str class.")
        if not isinstance(values, dict):
            raise TypeError("values parameter is not an instance of dict class.")
        
        if not self._hardwareClasses.has_key(type):
            raise HardwareDTOFactoryError("Can't create HardwareDTO.")
        
        return self._hardwareClasses[type](values)
    
    def _registerHardwareClass(self, name, clazz):
        """
        Inserts a class object in map.
        @param name: the name of class.
        @type name: str
        @param clazz: the class object.
        @type clazz: object
        @rtype: None
        """
        if not isinstance(name, str):
            raise TypeError("the name parameter is not an instance of str class")
        if not isinstance(clazz, type):
            raise TypeError("clazz is not a class object.")
        self._hardwareClasses[name] = clazz
        return self._hardwareClasses[name]
    
    def _unregisterHardwareClass(self, name):
        """
        Removes a class object.
        @param name: the name of class.
        @param name: str
        @rtype: None
        """
        if not isinstance(name, str):
            raise TypeError("the name parameter is not an instance of str class")
        if not self._hardwareClasses.has_key(name):
            raise HardwareDTOFactoryError("Can't remove HardwareDTO.")
        clazz = self._hardwareClasses[name]
        del self._hardwareClasses[name]
        return clazz
    
    def _clearHardwareClasses(self):
        """
        Clean the map of hardware classes.
        @rtype: None
        """
        self._hardwareClasses.clear()
        return len(self._hardwareClasses)
    
    def _countHardwareClasses(self):
        """
        Counts the number of Hardware classes.
        @return: Returns the number of Hardware classes.
        @rtype: int
        """
        return len(self._hardwareClasses)