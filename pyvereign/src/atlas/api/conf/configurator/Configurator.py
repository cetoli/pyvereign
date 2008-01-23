class Configurator(object):
    """
    Define the interface of configurator component.
    
    @author: Fabricio
    @since: 16/01/2008 - 18:00:47
    @version: version
    """
    
    def __init__(self):
        """
        This method ensures which IDevice class is not instanciated.
        @raise NotImplementedError: if developer tries to instanciate the Configurator class.
        @attention: This method must be overrides in IDevice concrete subclasses. 
        """
        raise NotImplementedError("Configurator class can not be intanciated.")
    
    def loadConfiguration(self):
        """
        Loads configurations from a configuration file.
        
        @rtype: L{None}
        """
        pass
    
    def createObjects(self):
        """
        Creates objects from configuration properties.
        
        @rtype: L{None}
        """
        pass
    
    def getObjectRepository(self):
        """
        Gets the object repository of configurator.
        
        @return: an instance of IObjectRepository.
        @rtype: L{IObjectRepository}
        """
        pass
        
    
    def setFilename(self, filename):
        """
        Sets the name of configuration file.
        
        @param filename: pdesc
        @type filename: L{type}
        @return: the name of configuration file
        @rtype: L{str}
        """
        pass
    
    def getFilename(self):
        """
        Gets the configuration filename.
        
        @return: the configuration filename
        @rtype: L{str}
        """
        pass
    
    def setObjectRepository(self, repository):
        """
        Sets the object repository of configurator.
        
        @param repository: an instance of IObjectRepository
        @type repository: L{IObjectRepository}
        @return: an instance of IObjectRepository
        @rtype: L{IObjectRepository}
        """
        pass
    
    def getConfiguration(self):
        """
        Returns the configuration of configurator.
        
        @return: the configuration of configurator
        @rtype: L{Configuration}
        """
        pass
    
    def configureObject(self, obj, configurationType):
        pass