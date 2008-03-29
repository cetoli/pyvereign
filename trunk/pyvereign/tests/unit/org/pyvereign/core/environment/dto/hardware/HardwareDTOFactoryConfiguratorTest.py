from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.configuration.repository.DefaultObjectRepository import DefaultObjectRepository
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.dto.hardware.MachineImpl import MachineImpl
from org.pyvereign.core.environment.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
from org.pyvereign.core.environment.dto.hardware.ProcessorImpl import ProcessorImpl
from org.pyvereign.core.environment.dto.hardware.DiskDriveImpl import DiskDriveImpl
from org.pyvereign.core.environment.dto.hardware.PhysicalMemoryImpl import PhysicalMemoryImpl
import unittest

class HardwareDTOFactoryConfiguratorTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(HardwareDTOFactoryConfigurator())
    
    def test_load_configuration_create_objects(self):
        conf = HardwareDTOFactoryConfigurator()
        conf.setFilename("hardwares.json")
        conf.setObjectRepository(DefaultObjectRepository())
        conf.loadConfiguration()
        conf.createObjects()
        
        self.assertTrue(conf.getObjectRepository())
        repository = conf.getObjectRepository()
        self.assertTrue(repository.getObject(Constants.MACHINE))
        self.assertEquals(MachineImpl, repository.getObject(Constants.MACHINE))
    
    def test_configure_factory(self):
        conf = HardwareDTOFactoryConfigurator()
        conf.setFilename("hardwares.json")
        conf.setObjectRepository(DefaultObjectRepository())
        conf.loadConfiguration()
        conf.createObjects()
        
        factory = conf.configureObject(HardwareDTOFactory())
         
        self.assertTrue(MachineImpl, factory.createHardware(Constants.MACHINE, {}).__class__)
        self.assertTrue(ProcessorImpl, factory.createHardware(Constants.PROCESSOR, {}).__class__)
        self.assertTrue(DiskDriveImpl, factory.createHardware(Constants.DISK_DRIVE, {}).__class__)
        self.assertTrue(PhysicalMemoryImpl, factory.createHardware(Constants.PHYSICAL_MEMORY, {}).__class__)
        
        
        
