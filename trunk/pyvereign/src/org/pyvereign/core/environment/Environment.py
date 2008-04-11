from org.pyvereign.core.microkernel.InternalServer import InternalServer
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.EnvironmentConfigurator import EnvironmentConfigurator

class Environment(InternalServer):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def __init__(self):
        self.init()
        
    def init(self):
        InternalServer.init(self)
        self._name = Constants.ENVIRONMENT
        
        try:
            configurator = EnvironmentConfigurator()
            configurator.setFilename(Constants.ENVIRONMENT_CONFIG_FILE)
            configurator.setObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY_CLASS())
            configurator.loadConfiguration()
            configurator.createObjects()
            configurator.configureObject(self) 
        except:
            raise
        
    def initialize(self, owner, id, context):
        InternalServer.initialize(self, owner, id, context)
    
    
    