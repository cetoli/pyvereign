from sets import ImmutableSet

class CoreServiceResponse(object):
    """
    Implements the request of core service.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self, coreServiceID, action):
        self._coreServiceID = coreServiceID
        """
        @ivar: identifier of Core Service
        @type: L{CoreServiceID} 
        """
        self._action = action
        """
        @ivar: the name of action
        @type: str  
        """
        self._parameters = {}
        """
        @ivar: parameters of request.
        @type: dict  
        """
    
    def getAction(self):
        """
        Gets the action of request.
        @return: Returns the action of request.
        @rtype: str
        """
        return self._action
    
    def getCoreServiceID(self):
        """
        Gets the identifier of CoreServiceID.
        @return: Returns the identifier of CoreServiceID.
        @rtype: L{CoreServiceID}
        """
        return self._coreServiceID
    
    def addParameter(self, name, value):
        """
        Adds a parameter in request.
        @param name: name of parameter
        @type name: str
        @param value: value of parameter
        @type value: object
        @return: Returns the added value.
        @rtype: object
        """
        if not isinstance(name, str):
            raise TypeError("name parameter is not an instance of str.")
        if not value:
            raise RuntimeError("value parameter is none.")
        self._parameters[name] = value
        return self._parameters[name]
    
    def getParameter(self, name):
        """
        Gets the value of parameter.
        @param name: the name of parameter.
        @type name: str
        @return: Returns the value of parameter.
        @rtype: object
        """
        if not isinstance(name, str):
            raise TypeError("name parameter is not an instance of str.")
        return self._parameters[name]
    
    def removeParameter(self, name):
        """
        Removes a parameter by using its name.
        @param name: the name of parameter.
        @type name: str
        @return: Returns removed parameter.
        @rtype: object
        """
        if not isinstance(name, str):
            raise TypeError("name parameter is not an instance of str.")
        
        parameter = self._parameters[name]
        del self._parameters[name]
        return parameter
    
    def getParameters(self):
        """
        Gets the map of parameters.
        @return: Returns the map of parameters.
        @rtype: dict
        """
        return ImmutableSet(self._parameters.iteritems())
         
    