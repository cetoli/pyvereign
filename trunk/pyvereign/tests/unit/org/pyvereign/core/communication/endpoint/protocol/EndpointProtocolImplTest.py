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
        service.stubs().getOwner().will(pmock.return_value(communication))
        communication.stubs().getOwner().will(pmock.return_value(microkernel))
        microkernel.stubs().getModule(pmock.eq(Constants.ENVIRONMENT)).will(pmock.return_value(environment))
        microkernel.stubs().hasModule(pmock.eq(Constants.ENVIRONMENT)).will(pmock.return_value(True))
        environment.stubs().getModule(pmock.eq(Constants.NETWORKING_SERVICE)).will(pmock.return_value(networkingService))
        environment.stubs().hasModule(pmock.eq(Constants.NETWORKING_SERVICE)).will(pmock.return_value(True))
        networkingService.stubs().getHostAddress().will(pmock.return_value("192.168.1.5"))
        protocol.stubs().getName().will(pmock.return_value("TCP"))
        endpointProtocol = EndpointProtocolImpl(protocol, 5050, service)
        self.assertEquals(EndpointAddress, endpointProtocol.getPublicAddress().__class__)
        self.assertEquals("TCP://192.168.1.5:5050/", endpointProtocol.getPublicAddress().toURI())
        
    def test_try_get_public_address_with_none_owner_of_service(self):
        protocol = pmock.Mock()
        service = pmock.Mock()
        communication = pmock.Mock()
        microkernel = pmock.Mock()
        environment = pmock.Mock()
        networkingService = pmock.Mock()
        service.stubs().getOwner().will(pmock.return_value(None))
        protocol.stubs().getName().will(pmock.return_value("TCP"))
        endpointProtocol = EndpointProtocolImpl(protocol, 5050, service)
        self.assertRaises(RuntimeError, endpointProtocol.getPublicAddress)
    
    def test_try_get_public_address_with_none_owner_of_communication(self):
        protocol = pmock.Mock()
        service = pmock.Mock()
        communication = pmock.Mock()
        microkernel = pmock.Mock()
        environment = pmock.Mock()
        networkingService = pmock.Mock()
        service.stubs().getOwner().will(pmock.return_value(communication))
        communication.stubs().getOwner().will(pmock.return_value(None))
        protocol.stubs().getName().will(pmock.return_value("TCP"))
        endpointProtocol = EndpointProtocolImpl(protocol, 5050, service)
        self.assertRaises(RuntimeError, endpointProtocol.getPublicAddress)
        
    def test_try_get_public_address_with_false_return_in_has_module_of_microkernel(self):
        protocol = pmock.Mock()
        service = pmock.Mock()
        communication = pmock.Mock()
        microkernel = pmock.Mock()
        environment = pmock.Mock()
        networkingService = pmock.Mock()
        service.stubs().getOwner().will(pmock.return_value(communication))
        communication.stubs().getOwner().will(pmock.return_value(microkernel))
        microkernel.stubs().getModule(pmock.eq(Constants.ENVIRONMENT)).will(pmock.return_value(environment))
        microkernel.stubs().hasModule(pmock.eq(Constants.ENVIRONMENT)).will(pmock.return_value(False))
        protocol.stubs().getName().will(pmock.return_value("TCP"))
        endpointProtocol = EndpointProtocolImpl(protocol, 5050, service)
        self.assertRaises(RuntimeError, endpointProtocol.getPublicAddress)
    
    def test_try_get_public_address_with_false_return_in_has_module_of_environment(self):
        protocol = pmock.Mock()
        service = pmock.Mock()
        communication = pmock.Mock()
        microkernel = pmock.Mock()
        environment = pmock.Mock()
        networkingService = pmock.Mock()
        service.stubs().getOwner().will(pmock.return_value(communication))
        communication.stubs().getOwner().will(pmock.return_value(microkernel))
        microkernel.stubs().getModule(pmock.eq(Constants.ENVIRONMENT)).will(pmock.return_value(environment))
        microkernel.stubs().hasModule(pmock.eq(Constants.ENVIRONMENT)).will(pmock.return_value(True))
        environment.stubs().getModule(pmock.eq(Constants.NETWORKING_SERVICE)).will(pmock.return_value(networkingService))
        environment.stubs().hasModule(pmock.eq(Constants.NETWORKING_SERVICE)).will(pmock.return_value(False))
        protocol.stubs().getName().will(pmock.return_value("TCP"))
        endpointProtocol = EndpointProtocolImpl(protocol, 5050, service)
        self.assertRaises(RuntimeError, endpointProtocol.getPublicAddress)
        