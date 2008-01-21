from atlas.api.conf.AbstractProperty import AbstractProperty
from sets import ImmutableSet
from atlas.api.conf.Property import Property

class CompositeProperty(AbstractProperty):
    
    def __init__(self, name):
        self.initialize()
        self.setName(name)
        self.setLevel(0)
    
    def initialize(self):
        AbstractProperty.initialize(self)
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
        if not name:
            raise RuntimeError("Invalid parameter")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter")
        property = self.__properties[name]
        del self.__properties[name]
        return property
    
    def getProperty(self, name):
        if not name:
            raise RuntimeError("Invalid parameter")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter")
        return self.__properties[name]
    
    def __str__(self):
        res = self._name + ":\n"
        s = ""
        for i in range(self._level+1):
            s += " "
        for p in self.__properties.values():
            res += s + p.__str__()
        return res
    
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