from org.pyvereign.core.microkernel.InternalServer import InternalServer
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.EnvironmentConfigurator import EnvironmentConfigurator
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.microkernel.CoreServiceContext import CoreServiceContext

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
        return EnvironmentConfigurator()
    
    def _getConfigurationFilename(self):
        """
        Gets the name of configuration file.
        
        @return: Return the name of configuration file.
        @rtype: L{str}
        """
        return Constants.ENVIRONMENT_CONFIG_FILE
    
    def _getObjectRepository(self):
        """
        Gets the specific object repository for configuration process.
        
        @return: Returns the specific object repository for configuration process..
        @rtype: L{str}
        """
        return Constants.DEFAULT_OBJECT_REPOSITORY_CLASS()
    
    def sendStream(self, protocolName, inetAddress, stream, broadcasting = False, timeout = 0):
        id = IDFactory().createCoreServiceID(self, Constants.TRANSPORT_SERVICE)
        service = self._coreServices[id.getIDFormated()]
        try:
            service.sendStream(protocolName, inetAddress, stream, broadcasting, timeout)
        except:
            raise
    
    def getNetworkProtocols(self):
        id = IDFactory().createCoreServiceID(self, Constants.NETWORKING_SERVICE)
        service = self._coreServices[id.getIDFormated()]
        try:
            return service.getNetworkProtocols()
        except:
            raise
        
    def addTransportListener(self, protocolName, uri, listener):
        id = IDFactory().createCoreServiceID(self, Constants.TRANSPORT_SERVICE)
        service = self._coreServices[id.getIDFormated()]
        try:
            return service.addTransportListener(protocolName, uri, listener)
        except:
            raise
        
    def removeTransportListener(self, protocolName, uri):
        id = IDFactory().createCoreServiceID(self, Constants.TRANSPORT_SERVICE)
        service = self._coreServices[id.getIDFormated()]
        try:
            return service.removeTransportListener(protocolName, uri)
        except:
            raise
    