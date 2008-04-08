class Module(object):
    """
    Defines the common interface of platform components.
    
    @author: Fabricio
    @since: 18/03/2008 - 09:38:41
    @version: 0.0.1
    """
    
    NON_INITIALIZED = 0
    """
    @cvar: Defines the status value when a module was not initialized.
    @type: L{int}  
    """
    INITIALIZED = 1
    """
    @cvar: Defines the status value when a module was initialized.
    @type: L{int}  
    """    
    STARTED = 2
    """
    @cvar: Defines the status value when a module was started.
    @type: L{int}  
    """    
    STOPED = 3
    """
    @cvar: Defines the status value when a module was stoped.
    @type: L{int}  
    """    
    
    def __init__(self):
        """
        This method is implemented to raise an L{NotImplementedError}, because the Module class denotes an
        interface.
        
        @return: returns an instance of L{NotImplementedError}
        @rtype: L{NotImplementedError}
        """
        raise NotImplementedError()
    
    def initialize(self, owner, id, context):
        """
        Initializes the module.
        @param owner: Owner of module.
        @type owner: L{Module}
        @param id: Identifier of module.
        @type id: L{ID}
        @param context: Context information of module.
        @type context: L{Context}
        @rtype: L{None}
        """
        pass
    
    def start(self, args):
        """
        Completes the modulule initialization.
        
        @param args: Argument list.
        @type args: L{list}
        @rtype: L{None}
        """
        pass
    
    def stop(self):
        """
        Stops the module.
        
        @rtype: L{None}
        """
        pass
    
    def getStatus(self):
        """
        Returns the status of module.
        
        @return: The status of module.
        @rtype: L{int}
        """
        pass
    
    def getID(self):
        """
        Return the identifier object of module.
        
        @return: The identifier object of module.
        @rtype: L{ID}
        """
        pass
    
    def getInterface(self, type):
        """
        Gets an specific interface of module.
        
        @param type: Type of interface.
        @type type: L{str}
        @return: Returns an specific interface of module.
        @rtype: L{Module}    
        """
        pass
    
    def addModule(self, id, module):
        """
        Adds a module.
        
        @param id: Identifier of module.
        @type id: L{str}
        @param module: a module
        @type module: L{Module}
        @return: Returns the module that was added.
        @rtype: L{Module}
        """
        pass
    
    def removeModule(self, id):
        """
        Removes a module.
        
        @param id: Identifier of module.
        @type id: L{str}
        @return: Returns the module that was removed.
        @rtype: L{Module}
        """
        pass
    
    def countModules(self):
        """
        Counts the number of modules.
        
        @return: Returns the number of modules.
        @rtype: L{int}
        """
        pass
    
    def clearModules(self):
        """
        Removes all modules.
        
        @rtype: L{None}
        """
        pass
    
    def getOwner(self):
        """
        Gets the owner of module.
        
        @return: Returns the owner of module.
        @rtype: L{Module}
        """
        pass
    
    def isComposite(self):
        """
        Returns if module is composite.
        
        @return: Return true if module is composite.
        @rtype: L{bool}
        """
        pass
    
    def getName(self):
        """
        Gets the name of module.
        @return: Returns the name of module.
        @rtype: str
        """
        pass
        
        
    
    
    
        
    