class ClassLoader:
    """
    Utility class for loading class objects.
    """
    
    def loadClass(self, module, className):
        """
        Loads class objects by using their module and class name.
        @param module: module of class
        @type module: str
        @param className: name of class
        @type className: str
        @return: Returns a class object.
        @rtype: Class
        """
        try:
            mod = __import__(module, globals(), locals(), className, -1)
            clazz = mod.__getattribute__(className)
            return clazz
        except:
            raise
        
    loadClass = classmethod(loadClass)