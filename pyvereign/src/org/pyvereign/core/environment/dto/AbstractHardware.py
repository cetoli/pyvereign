from org.pyvereign.core.environment.dto.Hardware import Hardware

class AbstracHardware(Hardware):
    """
    Defines the common implementation for Hardware objects.
    
    @author: Fabricio
    @since: 22/03/2008 - 00:26:08
    @version: 0.0.1
    """
    
    def __init__(self, values):
        self.init(values)
    
    def init(self, values = {}):
        """
        Initializes objects with values which are keeped in values dict.
        
        @param values: dictionary of values
        @type values: L{dict}
        @rtype: L{None}
        """
        if not isinstance(values, dict):
            raise TypeError("values parameter is not an instance of dict class.")
        self._description = ""
        """
        @ivar: the description of hardware
        @type: str
        """
        self._product = ""
        """
        @ivar: the information product of hardware
        @type: str
        """
        self._hardwareId = ""
        """
        @ivar: the identifier of hardware
        @type: str
        """
        self._logicalName = ""
        """
        @ivar: the logical name of hardware
        @type: str
        """
        self._serial = ""
        """
        @ivar: the serial of hardware
        @type: str
        """
        self._vendor = ""
        """
        @ivar: the vendor of hardware
        @type: str
        """
        
        for k in values.keys():
            if not "_" + k in self.__dict__:
                raise RuntimeError("_" + k + " not exists in " + self.__class__.__name__ + " object.")
        
        if values.has_key("description"):
            self._description = values["description"]
        
        if values.has_key("product"):
            self._product = values["product"]
            
        if values.has_key("hardwareId"):
            self._hardwareId = values["hardwareId"]
            
        if values.has_key("logicalName"):
            self._logicalName = values["logicalName"]
            
        if values.has_key("serial"):
            self._serial = values["serial"]
            
        if values.has_key("vendor"):
            self._vendor = values["vendor"]
        
    