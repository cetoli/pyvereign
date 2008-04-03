from org.pyvereign.core.environment.instrumentation.dto.hardware.Hardware import Hardware

class AbstractHardware(Hardware):
    """
    Defines the common implementation for Hardware objects.
    
    @author: Fabricio
    @since: 22/03/2008 - 00:26:08
    @version: 0.0.1
    """
    
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
        
    def getDescription(self):
        """
        Gets the description of hardware.
        @return: Returns the description of hardware.
        @rtype: str
        """
        return self._description
    
    def getProduct(self):
        """
        Gets the information of product.
        @return: Returns the information of product.
        @rtype: str
        """
        return self._product
    
    def getVendor(self):
        """
        Gets the vendor of hardware.
        @return: Returns the vendor of hardware.
        @rtype: str
        """
        return self._vendor
    
    def getSerial(self):
        """
        Gets the serial of hardware.
        @return: Returns the serial of hardware.
        @rtype: str
        """
        return self._serial
    
    def getLogicalName(self):
        """
        Gets the logical name of hardware.
        @return: Returns the logical name of hardware.
        @rtype: str
        """
        return self._logicalName
    
    def getHardwareId(self):
        """
        Gets the identifier of hardware.
        @return: Returns the identifier of hardware.
        @rtype: str
        """
        return self._hardwareId