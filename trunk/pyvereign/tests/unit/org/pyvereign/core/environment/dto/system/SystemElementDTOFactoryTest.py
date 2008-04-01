from org.pyvereign.core.environment.dto.system.SystemElementDTOFactory import SystemElementDTOFactory
from org.pyvereign.core.environment.dto.system.SystemElementDTOFactoryConfigurator import SystemElementDTOFactoryConfigurator
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.dto.system.ProcessImpl import ProcessImpl
import unittest

class SystemElementDTOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(SystemElementDTOFactory())
        self.assertEquals(SystemElementDTOFactory(), SystemElementDTOFactory())
    
    def test_create_system_element(self):
        configurator = SystemElementDTOFactoryConfigurator()
        configurator.setFilename(Constants.SYSTEM_ELEMENTS_CONFIG_FILE)
        configurator.setObjectRepository(ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY))
        configurator.loadConfiguration()
        configurator.createObjects()
        
        factory = configurator.configureObject(SystemElementDTOFactory())
        
        self.assertEquals(ProcessImpl, factory.createSystemElement(Constants.PROCESS, {}).__class__)