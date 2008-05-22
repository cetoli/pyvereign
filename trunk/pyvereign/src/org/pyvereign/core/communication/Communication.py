from org.pyvereign.core.microkernel.InternalServer import InternalServer
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.microkernel.CoreServiceContext import CoreServiceContext

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