class FormatableObject(object):
    """
    Defines operations of FormatableObject interface.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        raise NotImplementedError()
    
    def getValues(self):
        """
        Gets the all attribute values of object.
        @return: Returns the all attribute values of object.
        @rtype: dict
        """
        pass
    
    def setValues(self, values):
        """
        Sets the attributes values in object.
        @param values: the attribute values.
        @type values: dict
        @return: Returns the attributes values.
        @rtype: dict
        """
        pass
        
    