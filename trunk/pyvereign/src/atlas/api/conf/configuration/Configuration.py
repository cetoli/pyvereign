from sets import ImmutableSet
from atlas.api.conf.property.Property import Property
from atlas.api.conf.property.CompositeProperty import CompositeProperty
from atlas.api.conf.property.DefaultProperty import DefaultProperty
from json import WriteException
from json import ReadException
import json
import os

class Configuration(object):
    
    def __init__(self):
        self.__properties = {}
    
    def addProperty(self, property):
        if not property:
            raise RuntimeError("Invalid parameter")
        if not isinstance(property, Property):
            raise TypeError("property is not a instance of Property.")
        self.__properties[property.getName()] = property
        return property
    
    def removeProperty(self, name):
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter.")
        property = self.__properties[name]
        del self.__properties[name]
        return property
    
    def getProperty(self, name):
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter.")
        return self.__properties[name]
    
    def save(self, filename):
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
        self.__properties.clear()
        
    def getNumberOfProperties(self):
        return len(self.__properties)
    
    def hasProperty(self, name):
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("Invalid parameter.")
        return self.__properties.has_key(name)

    def getProperties(self):
        return ImmutableSet(self.__properties.values())