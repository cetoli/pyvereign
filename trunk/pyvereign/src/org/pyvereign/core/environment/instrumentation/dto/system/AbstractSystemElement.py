from org.pyvereign.core.environment.instrumentation.dto.system.SystemElement import SystemElement

class AbstractSystemElement(SystemElement):
    """
    Define the common implementation  
    
    @author: Fabricio
    @since: 28/03/2008 - 14:31:05
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
    