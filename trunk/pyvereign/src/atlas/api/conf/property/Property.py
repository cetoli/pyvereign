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
        pass
    
    def isComposite(self):
        pass
    
    def addProperty(self, property):
        pass
    
    def removeProperty(self, name):
        pass
    
    def getProperty(self, name):
        pass
    
    def setLevel(self, level):
        pass
    
    def getLevel(self):
        pass
    
    def hasProperty(self, name):
        pass
    
    def getNumberOfProperties(self):
        pass
    
    def getProperties(self):
        pass
    
    def getValues(self):
        pass