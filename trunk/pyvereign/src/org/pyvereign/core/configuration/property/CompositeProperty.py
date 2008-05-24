from sets import ImmutableSet
from org.pyvereign.core.configuration.property.AbstractProperty import AbstractProperty
from org.pyvereign.core.configuration.property.Property import Property

class CompositeProperty(AbstractProperty):
    
    def __init__(self, name):
        self.init()
        self.setName(name)
        self.setLevel(0)
    
    def init(self):
        AbstractProperty.init(self)
        self.__properties = {}
    
    def setName(self, name):
        self._name = name
        
    def getName(self):
        return self._name
    
    def setValue(self, value):
        raise RuntimeError("Invalid operation.")
        
    def getValue(self):
        raise RuntimeError("Invalid operation.")
    
    def isComposite(self):
        return True
    
    def addProperty(self, property):
        """
        Adds a property.
        @param property: a property
        @type property: L{Property}
        @return: Returns the added property.
        @rtype: L{Property}
        """
        if not property:
            raise RuntimeError("Invalid parameter")
        if not isinstance(property, Property):
            raise TypeError("Invalid parameter")
        if property == self:
            raise RuntimeError("Auto reference.")
        self.__properties[property.getName()] = property
        property.setLevel(self._level + 1)
        return property
    
    def removeProperty(self, name):
        """
        Removes a property.
        @param name: the name of property.
        @type name: L{str}
        @return: Returns the removed property.
        @rtype: L{Property}
        """
        if not name:
            raise RuntimeError("Invalid parameter")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter")
        property = self.__properties[name]
        del self.__properties[name]
        return property
    
    def getProperty(self, name):
        """
        Removes a property.
        @param name: the name of property.
        @type name: L{Property}
        @return: Returns a property.
        @rtype: L{Property}
        """
        if not name:
            raise RuntimeError("Invalid parameter")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter")
        return self.__properties[name]
    
    def setLevel(self, level):
        self._level = level
        for p in self.__properties.values():
            p.setLevel(self._level + 1)
        
    def getLevel(self):
        return self._level
    
    def hasProperty(self, name):
        if not name:
            raise RuntimeError("Invalid parameter")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter")
        return self.__properties.has_key(name)
        
    def getNumberOfProperties(self):
        return len(self.__properties)
    
    def getProperties(self):
        return ImmutableSet(self.__properties.values())
    
    def getValues(self):
        values = {}
        for prop in self.__properties.values():
            aux = prop.getValues()
            for k, v in aux.iteritems():
                values[k] = v
        
        result = {self.getName() : values}
        return result