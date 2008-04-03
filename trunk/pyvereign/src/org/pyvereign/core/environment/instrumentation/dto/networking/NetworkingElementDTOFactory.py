class NetworkingElementDTOFactory(object):
    """
    Defines the factory to create instances of NetworkingElement.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            """
            @cvar: unique instance of class.
            @type: L{NetworkingElementDTOFactory}
            """
            cls.instance.init()
        return cls.instance
    
    def init(self):
        self._networkingElementClasses = {}
        """
        @ivar: the map of System Element classes.
        @type: dict  
        """
    
    def createNetworkingElement(self, type, values):
        """
        Creates instances of NetworkingElement interface.
        @param type: the type of Hardware.
        @type type: str
        @param values: the initialization values
        @type values: dict
        @return: Returns an intance of NetworkingElement.
        @rtype: L{SystemElement}
        """
        if not isinstance(type, str):
            raise TypeError("type parameter is not an instance of str class.")
        if not isinstance(values, dict):
            raise TypeError("values parameter is not an instance of dict class.")
        
        return self._networkingElementClasses[type](values)
    
    def _registerNetworkingElementClass(self, name, clazz):
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
        self._networkingElementClasses[name] = clazz
    
    def _unregisterNetworkingElementClass(self, name):
        """
        Removes a class object.
        @param name: the name of class.
        @param name: str
        @rtype: None
        """
        del self._networkingElementClasses[name]
    
    def _clearNetworkingElementClasses(self):
        """
        Clean the map of system element classes.
        @rtype: None
        """
        self._networkingElementClasses.clear()
    