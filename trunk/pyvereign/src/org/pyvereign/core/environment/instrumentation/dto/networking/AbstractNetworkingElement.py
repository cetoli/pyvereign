from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkingElement import NetworkingElement

class AbstractNetworkingElement(NetworkingElement):
    """
    Defines the common implementation for networking elements.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self, values):
        """
        Initializes objects with values which are keeped in values dict.
        
        @param values: dictionary of values
        @type values: L{dict}
        @rtype: L{None}
        """
        if not isinstance(values, dict):
            raise TypeError("values parameter is not an instance of dict class.")
        
        self._name = ""
        """
        @ivar: the name of process.
        @type: str 
        """
        
        for k in values.keys():
            if not "_" + k in self.__dict__:
                raise RuntimeError("_" + k + " not exists in " + self.__class__.__name__ + " object.")
        
        if values.has_key("name"):
            self._name = values["name"]
    
    def getName(self):
        """
        Gets the name of system element.
        @return: Returns the name of system element.
        @rtype: str
        """
        return self._name
    