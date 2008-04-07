from org.pyvereign.core.configuration.configurator.Configurator import Configurator
from org.pyvereign.core.configuration.repository.ObjectRepository import ObjectRepository
from org.pyvereign.core.configuration.Configuration import Configuration

class AbstractConfigurator(Configurator):
    """
    Defines the common implementation for configurators.
    
    @author: Fabricio
    @since: 16/01/2008 - 23:59:28
    @version: 0.0.1
    """
    
    def init(self):
        self._filename = ""
        """
        @ivar: name of configuration file.
        @type: str  
        """
        self._repository = None
        """
        @ivar: an repository
        @type: L{ObjectRepository}  
        """
        self._configuration = None
        """
        @ivar: an configuration
        @type: L{Configuration} 
        """
    
    def getObjectRepository(self):
        """
        Gets the object repository of configurator.
        @return: Returns the object repository of configurator.
        @rtype: L{ObjectRepository}
        """
        return self._repository 
        
    def setFilename(self, filename):
        """
        Sets the name of configuration file.
        @param filename: the name of configuration file.
        @type filename: str
        @return: Returns the name of configuration file.
        @rtype: str
        """
        if not filename:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(filename, str):
            raise TypeError()
        self._filename = filename
        return self._filename
    
    def getFilename(self):
        """
        Gets the name of configuration file.
        @return: Returns the name of configuration file.
        @rtype: str
        """
        return self._filename
    
    def setObjectRepository(self, repository):
        """
        Sets the object repository of configurator.
        @param repository: the object repository of configurator.
        @type repository: L{ObjectRepository}
        @return: Returns the object repository of configurator
        @rtype: L{ObjectRepository}
        """
        if not repository:
            raise RuntimeError("Invalid parameter")
        if not isinstance(repository, ObjectRepository):
            raise TypeError("The repository object is not instance of ObjectRepository class.")
        self._repository = repository
        return self._repository
    
    def loadConfiguration(self):
        aux = self._configuration
        try:
            try:
                self._configuration = None
                conf = Configuration()
                conf.load(self._filename)
                aux = conf
                return True
            except:
                raise
        finally:
            self._configuration = aux
    
    def getConfiguration(self):
        return self._configuration
    
    