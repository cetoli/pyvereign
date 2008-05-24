from org.pyvereign.core.exception.SystemElementDTOFactoryError import SystemElementDTOFactoryError
class SystemElementDTOFactory(object):
    """
    Defines the factory for the creation of SystemElement object. 
    
    @author: Fabricio
    @since: 29/03/2008 - 14:17:08
    @version: 0.0.1
    """
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            """
            @cvar: unique instance of class.
            @type: L{SystemElementDTOFactory}
            """
            cls.instance.init()
        return cls.instance
    
    def init(self):
        self._systemElementClasses = {}
        """
        @ivar: the map of System Element classes.
        @type: dict  
        """
    
    def createSystemElement(self, type, values):
        """
        Creates instances of SystemElement interface.
        @param type: the type of Hardware.
        @type type: str
        @param values: the initialization values
        @type values: dict
        @return: Returns an intance of SystemElement.
        @rtype: L{SystemElement}
        """
        if not isinstance(type, str):
            raise TypeError("type parameter is not an instance of str class.")
        if not isinstance(values, dict):
            raise TypeError("values parameter is not an instance of dict class.")
        if not self._systemElementClasses.has_key(type):
            raise SystemElementDTOFactoryError()
        
        return self._systemElementClasses[type](values)
    
    def _registerSystemElementClass(self, name, clazz):
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
            raise TypeError()
        self._systemElementClasses[name] = clazz
        return self._systemElementClasses[name]
    
    def _unregisterSystemElementClass(self, name):
        """
        Removes a class object.
        @param name: the name of class.
        @param name: str
        @rtype: None
        """
        if not isinstance(name, str):
            raise TypeError("the name parameter is not an instance of str class")
        if not self._systemElementClasses.has_key(name):
            raise SystemElementDTOFactoryError()
        clazz = self._systemElementClasses[name]
        del self._systemElementClasses[name]
        return clazz
    
    def _clearSystemElementClasses(self):
        """
        Clean the map of system element classes.
        @rtype: None
        """
        self._systemElementClasses.clear()
        return len(self._systemElementClasses)
        
    def _countSystemElementClasses(self):
        return len(self._systemElementClasses)
    