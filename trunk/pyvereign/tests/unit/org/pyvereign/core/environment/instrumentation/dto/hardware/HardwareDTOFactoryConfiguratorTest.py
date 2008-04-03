from org.pyvereign.core.configuration.repository.DefaultObjectRepository import DefaultObjectRepository
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.hardware.MachineImpl import MachineImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.DiskDriveImpl import DiskDriveImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.PhysicalMemoryImpl import PhysicalMemoryImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.ProcessorImpl import ProcessorImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.BatteryImpl import BatteryImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
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
        self.assertTrue(repository.getObject(Constants.DISK_DRIVE))
        self.assertEquals(DiskDriveImpl, repository.getObject(Constants.DISK_DRIVE))
        self.assertTrue(repository.getObject(Constants.PHYSICAL_MEMORY))
        self.assertEquals(PhysicalMemoryImpl, repository.getObject(Constants.PHYSICAL_MEMORY))
        self.assertTrue(repository.getObject(Constants.PROCESSOR))
        self.assertEquals(ProcessorImpl, repository.getObject(Constants.PROCESSOR))
        self.assertTrue(repository.getObject(Constants.BATTERY))
        self.assertEquals(BatteryImpl, repository.getObject(Constants.BATTERY))
    
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
        self.assertTrue(BatteryImpl, factory.createHardware(Constants.BATTERY, {}).__class__)
        
        
        
