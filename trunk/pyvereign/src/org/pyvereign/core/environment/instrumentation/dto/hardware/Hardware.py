class Hardware(object):
    """
    Defines the common interface for user hardware.
    
    @author: Fabricio
    @since: 21/03/2008 - 23:22:24
    @version: 0.0.1
    """
    def __init__(self):
        raise NotImplementedError()
    
    def getDescription(self):
        """
        Gets the description of hardware.
        @return: Returns the description of hardware.
        @rtype: str
        """
        pass
    
    def getProduct(self):
        """
        Gets the information of product.
        @return: Returns the information of product.
        @rtype: str
        """
        pass
    
    def getVendor(self):
        """
        Gets the vendor of hardware.
        @return: Returns the vendor of hardware.
        @rtype: str
        """
        pass
    
    def getSerial(self):
        """
        Gets the serial of hardware.
        @return: Returns the serial of hardware.
        @rtype: str
        """
        pass
    
    def getLogicalName(self):
        """
        Gets the logical name of hardware.
        @return: Returns the logical name of hardware.
        @rtype: str
        """
        pass
    
    def getHardwareId(self):
        """
        Gets the identifier of hardware.
        @return: Returns the identifier of hardware.
        @rtype: str
        """
        pass
    