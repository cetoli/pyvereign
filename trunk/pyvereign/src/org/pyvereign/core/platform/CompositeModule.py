from org.pyvereign.core.platform.AbstractModule import AbstractModule

class CompositeModule(AbstractModule):
    """
    Defines the implementation for platform composite module.
    
    @author: Fabricio
    @since: 18/03/2008 - 16:50:34
    @version: 0.0.1
    """
    
    def init(self):
        AbstractModule.init(self)
        """
        @ivar: the map of modules.
        @type: L{dict}  
        """
    
    def initialize(self, owner, id, context):
        try:
            configurator = self._getConfigurator()
            configurator.setFilename(self._getConfigurationFilename())
            configurator.setObjectRepository(self._getObjectRepository())
            configurator.loadConfiguration()
            configurator.createObjects()
            configurator.configureObject(self)
        except:
            raise
        AbstractModule.initialize(self, owner, id, context)
    
    def _getConfigurator(self):
        """
        Returns the appropriated configurator for configuring the composite module.
        
        @return: a Configurator object.
        @rtype: L{int}
        """
        pass
    
    def _getConfigurationFilename(self):
        """
        Gets the name of configuration file.
        
        @return: Return the name of configuration file.
        @rtype: L{str}
        """
        pass
    
    def _getObjectRepository(self):
        """
        Gets the specific object repository for configuration process.
        
        @return: Returns the specific object repository for configuration process..
        @rtype: L{str}
        """
        pass
    
    
    
    