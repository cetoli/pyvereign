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
            @type: L{HardwareDTOFactory}
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
        self._systemElementClasses[name] = clazz
    
    def _unregisterSystemElementClass(self, name):
        """
        Removes a class object.
        @param name: the name of class.
        @param name: str
        @rtype: None
        """
        del self._systemElementClasses[name]
    
    def _clearSystemElementClasses(self):
        """
        Clean the map of system element classes.
        @rtype: None
        """
        self._systemElementClasses.clear()
    