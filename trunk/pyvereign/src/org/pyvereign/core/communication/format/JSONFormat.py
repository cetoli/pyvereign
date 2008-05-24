from org.pyvereign.core.communication.format.Format import Format
from org.pyvereign.util.ClassLoader import ClassLoader
from org.pyvereign.core.exception.FormatError import FormatError
from org.pyvereign.core.communication.format.FormatableObject import FormatableObject
from org.pyvereign.util.Constants import Constants
import json

class JSONFormat(Format):
    """
    Defines 
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        return
    
    def getName(self):
        return Constants.JSON
    
    def marshal(self, object):
        """
        Converts an message for a specific message.
        @param object: a formatable object.
        @type object: L{FormatableObject}
        @return: Returns an message for a specific message.
        @rtype: str
        """
        if not isinstance(object, FormatableObject):
            raise TypeError()
        values = object.getValues()
        values["class"] = object.__class__.__name__
        values["module"] = object.__class__.__module__
        stream = json.write(values) + ";" + self.getName()
        return stream
    
    def unmarshal(self, stream):
        """
        Converts an stream for a EndpointMessage object.
        @return: Returns an stream for a EndpointMessage object.
        @rtype: L{EndpointMessage}
        """
        if not isinstance(stream, str):
            raise TypeError()
        values = json.read(stream)
        if (not values.has_key("class")) or (not values.has_key("module")):
            raise FormatError("invalid format.")
        clazz = None
        try:
            clazz = ClassLoader.loadClass(values["module"], values["class"])
        except:
            raise FormatError()
        object = clazz()
        object.setValues(values)
        return object
        
        
