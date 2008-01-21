from sets import ImmutableSet
from atlas.api.conf.Property import Property

class AbstractProperty(Property):
    
    def initialize(self):
        self.__name = ""
        self.__value = None
        self.__level = 0
    
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setValue(self, value):
        self.__value = value
        
    def getValue(self):
        return self.__value
    
    def isComposite(self):
        return False
    
    def addProperty(self, property):
        raise RuntimeError("Invalid operarion.")
    
    def removeProperty(self, name):
        raise RuntimeError("Invalid operarion.")
    
    def getProperty(self, name):
        raise RuntimeError("Invalid operarion.")
    
    def setLevel(self, level):
        self.__level = level
        
    def getLevel(self):
        return self.__level
    
    def __str__(self):
        return self.__name + ": " + str(self.__value) + "\n"
    
    def hasProperty(self, name):
        return False
    
    def getNumberOfProperties(self):
        return 0
    
    def getProperties(self):
        return ImmutableSet([])