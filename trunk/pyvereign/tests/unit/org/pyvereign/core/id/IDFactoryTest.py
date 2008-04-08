from org.pyvereign.core.id.IDFactory import IDFactory
from org.pyvereign.core.environment.Environment import Environment
from org.pyvereign.core.environment.DefaultTransportService import DefaultTransportService
from org.pyvereign.core.id.CoreServiceID import CoreServiceID
from org.pyvereign.util.Constants import Constants
import unittest

class IDFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(IDFactory())
        self.assertEquals(IDFactory(), IDFactory())
        
    def test_create_core_service_id_for_transport_service(self):
        self.assertTrue(IDFactory().createCoreServiceID(Environment(), Constants.TRANSPORT_SERVICE))
        self.assertEquals(CoreServiceID, IDFactory().createCoreServiceID(Environment(), Constants.TRANSPORT_SERVICE).__class__)
        
        coreServiceID1 = IDFactory().createCoreServiceID(Environment(), Constants.TRANSPORT_SERVICE)
        coreServiceID2 = IDFactory().createCoreServiceID(Environment(), Constants.TRANSPORT_SERVICE)
        
        self.assertEquals(coreServiceID1.getIDFormated(), coreServiceID2.getIDFormated())