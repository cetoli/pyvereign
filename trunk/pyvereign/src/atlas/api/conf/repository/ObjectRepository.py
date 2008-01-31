class ObjectRepository(object):
    """
    Define 
    
    @author: Fabricio
    @since: 16/01/2008 - 23:42:12
    @version: version
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def addObject(self, name, obj):
        """
        Adds an object in object repsitory.
        
        @param name: the name of object
        @type name: L{str}
        @param obj: an instance
        @type obj: L{object}
        @return: an instance
        @rtype: L{object}
        """
        pass
    
    def removeObject(self, name):
        pass
    
    def getObject(self, name):
        pass
    
    def getNumberOfObjects(self):
        pass
    
    def clear(self):
        pass
    
    def getObjects(self):
        pass
    
    def hasObject(self, name):
        pass