from atlas.api.conf.configurator.Configurator import Configurator
from atlas.api.conf.configuration.Configuration import Configuration
from atlas.api.conf.repository.ObjectRepository import ObjectRepository

class AbstractConfigurator(Configurator):
    """
    description
    
    @author: Fabricio
    @since: 16/01/2008 - 23:59:28
    @version: version
    """
    
    def initialize(self):
        self._filename = ""
        self._repository = None
        self._configuration = None
    
    def getObjectRepository(self):
        return self.__repository 
        
    def setFilename(self, filename):
        if not filename:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(filename, str):
            raise TypeError()
        self._filename = filename
        return self._filename
    
    def getFilename(self):
        return self._filename
    
    def setObjectRepository(self, repository):
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
    
    