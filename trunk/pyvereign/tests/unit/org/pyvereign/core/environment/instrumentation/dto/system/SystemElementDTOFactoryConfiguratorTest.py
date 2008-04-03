from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.DefaultObjectRepository import DefaultObjectRepository
from org.pyvereign.core.environment.instrumentation.dto.system.SystemElementDTOFactoryConfigurator import SystemElementDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.system.ProcessImpl import ProcessImpl
from org.pyvereign.core.environment.instrumentation.dto.system.SystemElementDTOFactory import SystemElementDTOFactory
import unittest

class SystemElementDTOFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(SystemElementDTOFactoryConfigurator())
        
    def test_load_configuration_and_create_objects(self):
        conf = SystemElementDTOFactoryConfigurator()
        conf.setFilename(Constants.SYSTEM_ELEMENTS_CONFIG_FILE)
        conf.setObjectRepository(DefaultObjectRepository())
        
        conf.loadConfiguration()
        conf.createObjects()
        
        self.assertTrue(conf.getObjectRepository())
        repository = conf.getObjectRepository()
        
        self.assertTrue(repository.getObject(Constants.PROCESS))
        self.assertEquals(ProcessImpl, repository.getObject(Constants.PROCESS))
        
    def test_configure_object(self):
        conf = SystemElementDTOFactoryConfigurator()
        conf.setFilename("system_elements.json")
        conf.setObjectRepository(DefaultObjectRepository())
        conf.loadConfiguration()
        conf.createObjects()
        
        factory = conf.configureObject(SystemElementDTOFactory())
        
        self.assertTrue(factory.createSystemElement(Constants.PROCESS, {}))