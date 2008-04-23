class MessageFormatFactory(object):
    """
    Defines the factory of MessageFormat object.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __new__(cls):
        if not 'instance' in cls.__dict__:
            cls.instance = object.__new__(cls)
            cls.instance.init()
        
        return cls.instance
    
    def init(self):
        self._formats = {}
    
    def createMessageFormat(self, type):
        """
        Creates an instance of MessageFormat.
        @param type: the type of MessageFormat.
        @type type: str
        @return: Returns an instance of MessageFormat.
        @rtype: L{MessageFormat}
        """
        if not isinstance(type, str):
            raise TypeError()
        return self._formats[type]()
    
    def _registerMessageFormatClass(self, name, clazz):
        if not isinstance(name, str):
            raise TypeError("name is not an instance of str class.")
        
        self._formats[name] = clazz
    
    def _unregisterMessageFormat(self, name):
        del self._formats[name]
    
    def _clearMessageFormatClasses(self):
        self._formats.clear()
        