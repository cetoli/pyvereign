from sets import ImmutableSet
from org.pyvereign.core.configuration.property.Property import Property

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
        """
        The implementation of this method does not allow the addition of properties. Thus, this
        method must be overrided in composite property classes.
        @raise RuntimeError: Raises to try add a property.
        """ 
        raise RuntimeError("Invalid operarion.")
    
    def removeProperty(self, name):
        """
        The implementation of this method does not allow the removal of properties. Thus, this
        method must be overrided in composite property classes.
        @raise RuntimeError: Raises to try remove a property.
        """ 
        raise RuntimeError("Invalid operarion.")
    
    def getProperty(self, name):
        """
        The implementation of this method does not allow the obtainment of properties. Thus, this
        method must be overrided in composite property classes.
        @raise RuntimeError: Raises to try get a property.
        """ 
        raise RuntimeError("Invalid operarion.")
    
    def setLevel(self, level):
        self.__level = level
        
    def getLevel(self):
        return self.__level
    
    def hasProperty(self, name):
        return self.__name == name
    
    def getNumberOfProperties(self):
        return 0
    
    def getProperties(self):
        return ImmutableSet([])
    
    def getValues(self):
        return {self.__name : self.__value}