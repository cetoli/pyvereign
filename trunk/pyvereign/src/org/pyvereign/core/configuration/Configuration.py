from sets import ImmutableSet
from json import WriteException
from json import ReadException
from org.pyvereign.core.configuration.property.Property import Property
from org.pyvereign.core.configuration.property.CompositeProperty import CompositeProperty
from org.pyvereign.core.configuration.property.DefaultProperty import DefaultProperty
import json
import os

class Configuration(object):
    
    def __init__(self):
        """
        Initializes a Configuration object when it is created.
        @return: Returns an instance of Configuration.
        @rtype: L{Configuration}
        """
        self.__properties = {}
        """
        @ivar: map of properties.
        @type: L{dict}  
        """
    
    def addProperty(self, property):
        """
        Adds a property in configuration.
        @param property: a property
        @type property: L{Property}
        @return: Returns the added property.
        @rtype: L{Property}
        """
        if not property:
            raise RuntimeError("Invalid parameter")
        if not isinstance(property, Property):
            raise TypeError("property is not a instance of Property.")
        self.__properties[property.getName()] = property
        return property
    
    def removeProperty(self, name):
        """
        Removes a property by using the name of property.
        @param name: the name of property.
        @type name: L{str}
        @return: Returns the removed property.
        @rtype: L{Property}
        """
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter.")
        property = self.__properties[name]
        del self.__properties[name]
        return property
    
    def getProperty(self, name):
        """
        Gets a property by using the name of property.
        @param name: the name of property.
        @type name: L{str}
        @return: Returns an instance of Property.
        @rtype: L{Property} 
        """
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter.")
        return self.__properties[name]
    
    def save(self, filename):
        """
        Saves a Configuration object.
        @param filename: the name of configuration file.
        @type filename: L{str}
        @rtype: None
        """
        if filename == "" or not filename:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(filename, str):
            raise TypeError("Invalid parameter.")
        file = None
        try:
            try:
                file = open(os.environ["ATLAS_HOME"]+"/config/"+filename, "w")
                obj = {}
                for prop in self.__properties.values():
                    values = prop.getValues()
                    for k, v in values.iteritems():
                        obj[k] = v
                file.write(json.write(obj))
            except IOError, WriteException:
                raise
        finally:
            if file:
                file.close()    
    
    def load(self, filename):
        """
        Saves a Configuration object from a configuration file.
        @param filename: the name of configuration file.
        @type filename: L{str}
        @rtype: None
        """
        def loadProperties(obj, properties, composite):
            for k, v in obj.iteritems():
                if isinstance(v,dict):
                    c = CompositeProperty(k)
                    loadProperties(v, properties, c)
                    if not composite:
                        properties[k] = c
                    else:
                        composite.addProperty(c)
                else:
                    p = DefaultProperty(k, v)
                    if not composite:
                        properties[p.getName()] = p
                    else:
                        composite.addProperty(p)
            return properties
        
        if filename == "" or not filename:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(filename, str):
            raise TypeError("Invalid parameter.")
        
        file = None
        try:
            try:
                file = open(os.environ["ATLAS_HOME"]+"/config/"+filename, "r")
                stream = ""
                for line in file:
                    stream += line
                obj = json.read(stream)
                if not obj:
                    return
                self.__properties = loadProperties(obj, self.__properties, None)
            except IOError, ReadException:
                raise
        finally:
            if file:
                file.close()
    
    def clear(self):
        """
        Removes all properties in the map of properties.
        @rtype: None
        """
        self.__properties.clear()
        
    def getNumberOfProperties(self):
        """
        Counts the number of properties in map.
        @return: Returns the count of configuration properties.
        @rtype: int
        """
        return len(self.__properties)
    
    def hasProperty(self, name):
        """
        Verifies the existence of property by using name.
        @return: Returns true if property exists.
        @rtype: bool
        """
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter.")
        return self.__properties.has_key(name)

    def getProperties(self):
        """
        Gets the set of properties.
        @return: a set of properties.
        @rtype: ImmutableSet
        """
        return ImmutableSet(self.__properties.values())