from atlas.api.conf.configurator.Configurator import Configurator
from atlas.api.conf.configuration.Configuration import Configuration

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
        self._filename = filename
        return self._filename
    
    def getFilename(self):
        return self._filename
    
    def setObjectRepository(self, repository):
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
    
    