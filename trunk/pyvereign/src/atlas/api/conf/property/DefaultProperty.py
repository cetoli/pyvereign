from atlas.api.conf.property.AbstractProperty import AbstractProperty

class DefaultProperty(AbstractProperty):
    
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