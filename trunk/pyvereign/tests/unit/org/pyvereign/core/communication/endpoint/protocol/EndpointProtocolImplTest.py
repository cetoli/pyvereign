from org.pyvereign.core.communication.endpoint.protocol.EndpointProtocolImpl import EndpointProtocolImpl
from org.pyvereign.core.environment.instrumentation.dto.networking.NetworkProtocol import NetworkProtocol
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
import pmock
import unittest

class EndpointProtocolImplTest(unittest.TestCase):
    
    def test_create_instance(self):
        protocol = pmock.Mock()
        service = pmock.Mock()
        self.assertTrue(EndpointProtocolImpl(protocol, 5050, service))
        
    def test_get_public_address(self):
        protocol = pmock.Mock()
        service = pmock.Mock()
        communication = pmock.Mock()
        microkernel = pmock.Mock()
        environment = pmock.Mock()
        networkingService = pmock.Mock()
        service.expects(pmock.once()).getOwner().will(pmock.return_value(communication))
        communication.expects(pmock.once()).getOwner().will(pmock.return_value(microkernel))
        microkernel.expects(pmock.once()).getModule(pmock.eq(Constants.ENVIRONMENT)).will(pmock.return_value(environment))
        environment.expects(pmock.once()).getModule(pmock.eq(Constants.NETWORKING_SERVICE)).will(pmock.return_value(networkingService))
        networkingService.expects(pmock.once()).getHostAddress().will(pmock.return_value("192.168.1.5"))
        protocol.expects(pmock.once()).getName().will(pmock.return_value("TCP"))
        endpointProtocol = EndpointProtocolImpl(protocol, 5050, service)
        self.assertEquals(EndpointAddress, endpointProtocol.getPublicAddress().__class__)
        