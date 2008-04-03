from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactory import HardwareDTOFactory
from org.pyvereign.core.environment.instrumentation.dto.hardware.HardwareDTOFactoryConfigurator import HardwareDTOFactoryConfigurator
from org.pyvereign.core.environment.instrumentation.dto.hardware.BatteryImpl import BatteryImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.DiskDriveImpl import DiskDriveImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.MachineImpl import MachineImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.NetworkAdapterImpl import NetworkAdapterImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.PhysicalMemoryImpl import PhysicalMemoryImpl
from org.pyvereign.core.environment.instrumentation.dto.hardware.ProcessorImpl import ProcessorImpl
import unittest

class HardwareDTOFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(HardwareDTOFactory())
        self.assertEquals(HardwareDTOFactory(), HardwareDTOFactory())
        
    def test_create_hardware(self):
        configurator = HardwareDTOFactoryConfigurator()
        configurator.setFilename(Constants.HARDWARES_CONFIG_FILE)
        configurator.setObjectRepository(ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY))
        configurator.loadConfiguration()
        configurator.createObjects()
        
        factory = configurator.configureObject(HardwareDTOFactory())
        
        self.assertEquals(BatteryImpl, factory.createHardware(Constants.BATTERY, {}).__class__)
        self.assertEquals(DiskDriveImpl, factory.createHardware(Constants.DISK_DRIVE, {}).__class__)
        self.assertEquals(MachineImpl, factory.createHardware(Constants.MACHINE, {}).__class__)
        self.assertEquals(NetworkAdapterImpl, factory.createHardware(Constants.NETWORK_ADAPTER, {}).__class__)
        self.assertEquals(PhysicalMemoryImpl, factory.createHardware(Constants.PHYSICAL_MEMORY, {}).__class__)
        self.assertEquals(ProcessorImpl, factory.createHardware(Constants.PROCESSOR, {}).__class__)