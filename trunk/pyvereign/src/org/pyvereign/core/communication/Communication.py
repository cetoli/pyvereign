from org.pyvereign.core.microkernel.InternalServer import InternalServer
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.microkernel.CoreServiceContext import CoreServiceContext
from org.pyvereign.core.communication.CommunicationConfigurator import CommunicationConfigurator

class Communication(InternalServer):
    
    def __init__(self):
        self.init()
        
    def init(self):
        InternalServer.init(self)
        self._name = Constants.COMMUNICATION
        
    def initialize(self, owner, id, context):
        InternalServer.initialize(self, owner, id, context)
        for service in self._coreServices.values():
            id = IDFactory().createCoreServiceID(self, service.getName())
            service.initialize(self, id, CoreServiceContext(service))
    
    
    def _getConfigurator(self):
        """
        Returns the appropriated configurator for configuring the composite module.
        
        @return: a Configurator object.
        @rtype: L{int}
        """
        return CommunicationConfigurator()
    
    def _getConfigurationFilename(self):
        """
        Gets the name of configuration file.
        
        @return: Return the name of configuration file.
        @rtype: L{str}
        """
        return Constants.COMMUNICATION_CONFIG_FILE
    
    def _getObjectRepository(self):
        """
        Gets the specific object repository for configuration process.
        
        @return: Returns the specific object repository for configuration process..
        @rtype: L{str}
        """
        return Constants.DEFAULT_OBJECT_REPOSITORY_CLASS()