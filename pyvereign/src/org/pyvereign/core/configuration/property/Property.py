class Property(object):
    """
    Define the interface of objects which represent properties of a component configuration.
    
    @author: Fabricio Barros
    @contact: fbarros@gmail.com
    @license: 
    @since: 14/01/2008
    @version: 0.0.1
    @attention: This class is not instanciable, it represents the interface of object group.
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def setName(self, name):
        """
        Sets the name of this property.
        
        @param name: a name of property.
        @type name: C{str}
        @rtype: C{None}
        """
        pass
    
    def getName(self):
        """
        Gets the name of this property.
        
        @return: Return the name of this property.
        @rtype: C{str}
        """
        pass
    
    def setValue(self, value):
        """
        Sets the value of property.
        @param value: the value of property.
        @type value: C{str}
        """
        pass
    
    def getValue(self):
        """
        Gets the value of property.
        @return: Returns an object.
        @rtype: object
        """
        pass
    
    def isComposite(self):
        """
        Verifies if property is composite.
        @return: Returns true if property is composite.
        @rtype: bool
        """
        pass
    
    def addProperty(self, property):
        """
        Adds a property.
        @param property: a property
        @type property: L{Property}
        @return: Returns the added property.
        @rtype: L{Property}
        """
        pass
    
    def removeProperty(self, name):
        """
        Removes a property.
        @param name: the name of property.
        @type name: L{str}
        @return: Returns the removed property.
        @rtype: L{Property}
        """
        pass
    
    def getProperty(self, name):
        """
        Removes a property.
        @param name: the name of property.
        @type name: L{Property}
        @return: Returns a property.
        @rtype: L{Property}
        """
        pass
    
    def setLevel(self, level):
        """
        Sets the level of hierarchy.
        @param level: the level of hierarchy.
        @type level: int
        """
        pass
    
    def getLevel(self):
        """
        Gets the level of hierarchy.
        @return: Returns the level of hierarchy.
        @rtype: int
        """
        pass
    
    def hasProperty(self, name):
        """
        Verifies the existence of property by using name.
        @return: Returns true if property exists.
        @rtype: bool
        """
        pass
    
    def getNumberOfProperties(self):
        """
        Counts the number of properties in map.
        @return: Returns the count of configuration properties.
        @rtype: int
        """
        pass
    
    def getProperties(self):
        """
        Gets the set of properties.
        @return: a set of properties.
        @rtype: ImmutableSet
        """
        pass
    
    def getValues(self):
        pass