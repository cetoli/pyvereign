from org.pyvereign.core.configuration.property.AbstractProperty import AbstractProperty

class DefaultProperty(AbstractProperty):
    """
    Defines a default implementation of Property interface.
    """
    
    def __init__(self, name, value):
        """
        Initialize the DefaultProperty object.
        
        @param name: the name of property
        @type name: L{str}
        @param value: the value of property
        @type value: a object
        @return: a instance of DefaultProperty
        @rtype: L{DefaultProperty}
        """
        self.initialize()
        self.setName(name)
        self.setValue(value)