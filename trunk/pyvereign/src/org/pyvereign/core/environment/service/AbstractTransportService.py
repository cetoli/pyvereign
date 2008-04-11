from org.pyvereign.core.environment.service.TranportService import TransportService
from org.pyvereign.core.platform.CoreService import CoreService
from org.pyvereign.util.Constants import Constants

class AbstractTransportService(TransportService, CoreService):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def init(self):
        CoreService.init(self)
        self._protocols = {}
        self._streamListeners = {}
        self._name = Constants.TRANSPORT_SERVICE