from atlas.api.env.networking.DefaultProtocol import DefaultProtocol
import unittest

class DefaultProtocolTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultProtocol())
        
    def test_set_values_in_instance(self):
        protocol = DefaultProtocol()
        self.assertEquals("UDP", protocol.setName("UDP"))
        self.assertEquals(True, protocol.setBroadcastingSupport(True))
        self.assertEquals(True, protocol.setDeliveryGuarantee(True))
        self.assertEquals(True, protocol.setMulticastingSupport(True))
        self.assertEquals(True, protocol.setSequencingGuarantee(True))
        
        self.assertEquals(False, protocol.setBroadcastingSupport(False))
        self.assertEquals(False, protocol.setDeliveryGuarantee(False))
        self.assertEquals(False, protocol.setMulticastingSupport(False))
        self.assertEquals(False, protocol.setSequencingGuarantee(False))