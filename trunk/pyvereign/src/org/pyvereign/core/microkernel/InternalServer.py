from org.pyvereign.core.platform.CompositeModule import CompositeModule
from org.pyvereign.core.id.CoreServiceID import CoreServiceID
from org.pyvereign.core.platform.CoreService import CoreService
from org.pyvereign.core.microkernel.CoreServiceRequest import CoreServiceRequest

class InternalServer(CompositeModule):
    """
    Defines an internal service provider of microkernel.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def init(self):
        CompositeModule.init(self)
        self._coreServices = {}
        
    def addModule(self, id, module):
        if not isinstance(id, CoreServiceID):
            raise TypeError("id parameter is not an instance of CoreServiceID class.")
        if not isinstance(module, CoreService):
            raise TypeError("module parameter is not an instance of CoreService class.")
        self._coreServices[id.getIDFormated()] = module
        return self._coreServices[id.getIDFormated()]
        
    def removeModule(self, id):
        if not isinstance(id, CoreServiceID):
            raise TypeError("id parameter is not an instance of CoreServiceID class.")
        coreService = self._coreServices[id.getIDFormated()]
        del self._coreServices[id.getIDFormated()]
        return coreService
    
    def countModules(self):
        return len(self._coreServices)
    
    def clearModules(self):
        self._coreServices.clear()
        
    def executeService(self, coreServiceRequest, coreServiceResponse):
        """
        Executes service by using a specific action.
        @param coreServiceRequest: the request for service.
        @type coreServiceRequest: L{CoreServiceRequest}
        @return: Returns the response of service request.
        @rtype: L{CoreServiceResponse}
        """
        if not isinstance(coreServiceRequest, CoreServiceRequest):
            raise TypeError("coreServiceRequest parameter is not an instance of CoreServiceRequest class.")
        
        service = self._coreServices[coreServiceRequest.getCoreServiceID().getIDFormated()]
        function = service.__getattribute__(coreServiceRequest.getAction())
        
        for name, value in coreServiceRequest.getParameters():
            function.func_dict[name] = value
        
        coreServiceResponse.addParameter("return", function())
        return coreServiceResponse
    
        