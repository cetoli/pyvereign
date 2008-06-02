from org.pyvereign.core.communication.topology.service.TopologyControlService import TopologyControlService
from org.pyvereign.core.platform.CoreService import CoreService
from org.pyvereign.util.Constants import Constants

class AbstractTopologyControlService(TopologyControlService, CoreService):
    
    def init(self):
        CoreService.init(self)
        self._name = Constants.TOPOLOGY_CONTROL_SERVICE