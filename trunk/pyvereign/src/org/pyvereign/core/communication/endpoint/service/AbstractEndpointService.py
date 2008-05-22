from org.pyvereign.core.communication.endpoint.service.EndpointService import EndpointService
from org.pyvereign.core.platform.CoreService import CoreService
from org.pyvereign.util.Constants import Constants

class AbstractEndpointService(EndpointService, CoreService):

    def init(self):
        CoreService.init(self)
        self._endpointProtocols = {}
        self._endpointListeners = {}
        self._name = Constants.ENDPOINT_SERVICE