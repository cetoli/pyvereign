from org.pyvereign.core.exception.FormatFactoryError import FormatFactoryError

class FormatFactory(object):
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
    
    def createFormat(self, type):
        """
        Creates an instance of MessageFormat.
        @param type: the type of MessageFormat.
        @type type: str
        @return: Returns an instance of MessageFormat.
        @rtype: L{MessageFormat}
        """
        if not isinstance(type, str):
            raise TypeError()
        if not self._formats.has_key(type):
            raise FormatFactoryError()
        return self._formats[type]()
    
    def _registerMessageFormatClass(self, name, clazz):
        if not isinstance(name, str):
            raise TypeError("name is not an instance of str class.")
        if not isinstance(clazz, type):
            raise TypeError()
        
        self._formats[name] = clazz
        return self._formats[name]
    
    def _unregisterMessageFormatClass(self, name):
        if not isinstance(name, str):
            raise TypeError("name is not an instance of str class.")
        if not self._formats.has_key(name):
            raise FormatFactoryError()
        clazz = self._formats[name]
        del self._formats[name]
        return clazz
        
    
    def _clearMessageFormatClasses(self):
        self._formats.clear()
        return len(self._formats)
        
    def _countMessageFormatClasses(self):
        return len(self._formats)
        