from org.pyvereign.core.platform.Module import Module
from org.pyvereign.core.id.ID import ID
from org.pyvereign.core.exception.ModuleError import ModuleError

class AbstractModule(Module):
    """
    Defines common implementations for platform modules.
    
    @author: Fabricio
    @since: 18/03/2008 - 10:35:42
    @version: 0.0.1
    """
    def init(self):
        """
        Initializes the module object when it is created. This operation must be invoked in constructor of
        Module concrete subclass.
        
        @rtype: L{None}
        """
        self._status = AbstractModule.NON_INITIALIZED
        """
        @ivar: the status of module.
        @type: L{int}  
        """
        self._name = ""
        """
        @ivar: the name of module.
        @type: str  
        """
    
    def initialize(self, owner, id, context):
        if not isinstance(owner, Module):
            raise TypeError("owner is not an instance of Module class.")
        if not isinstance(id, ID):
            raise TypeError("id is not an instance of ID class.")
        if self._status == AbstractModule.STARTED:
            raise ModuleError(self.__class__.__name__ + "is running.")
        self._owner = owner
        """
        @ivar: the owner of module.
        @type: L{Module}  
        """
        self._id = id
        """
        @ivar: the id of module.
        @type: L{ID}  
        """
        self._context = context
        """
        @ivar: the information context of module.
        @type: L{Context}  
        """
        self._status = AbstractModule.INITIALIZED
        
    def start(self, args):
        if not isinstance(args, list):
            raise TypeError("args is not an instance of list class.")
        if (self._status < AbstractModule.INITIALIZED):
            raise ModuleError(self.__class__.__name__ + " was not initialized.")
        if (self._status == AbstractModule.STARTED):
            raise ModuleError(self.__class__.__name__ + " is already started.")
        self._status = AbstractModule.STARTED
        
    def stop(self):
        self._status = AbstractModule.STOPED
        
    def getStatus(self):
        return self._status
    
    def getID(self):
        return self._id
    
    def getOwner(self):
        return self._owner
    
    def addModule(self, id, module):
        raise RuntimeError("Unsupported operation.")
        
    def removeModule(self, id):
        raise RuntimeError("Unsupported operation.")
    
    def countModules(self):
        return 0
    
    def clearModules(self):
        raise RuntimeError("Unsupported operation.")
    
    def getModule(self, name):
        raise RuntimeError("Unsupported operation.")
    
    def getModules(self):
        raise RuntimeError("Unsupported operation.")
    
    def isComposite(self):
        return False
    
    def getName(self):
        return self._name