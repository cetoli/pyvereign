class ObjectRepository(object):
    """
    Define the common interface for object repositories.
    
    @author: Fabricio
    @since: 16/01/2008 - 23:42:12
    @version: 0.0.1
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
        """
        Removes an object by using name of object.
        @param name: the name of object
        @type name: L{str}
        @return: an instance
        @rtype: L{object}
        """
        pass
    
    def getObject(self, name):
        """
        Gets an object by using the name of object.
        @param name: the name of object
        @type name: L{str}
        @return: an instance
        @rtype: L{object}
        """
        pass
    
    def getNumberOfObjects(self):
        """
        Counts the number of objects in map.
        @return: Returns the count of objects.
        @rtype: int
        """
        pass
    
    def clear(self):
        """
        Removes all objects in the map of objects.
        @rtype: None
        """
        pass
    
    def getObjects(self):
        """
        Gets the set of objects.
        @return: a set of objects.
        @rtype: ImmutableSet
        """
        pass
    
    def hasObject(self, name):
        """
        Verifies the existence of object by using the name of object.
        @return: Returns true if property exists.
        @rtype: bool
        """
        pass