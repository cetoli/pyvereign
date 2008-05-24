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
from org.pyvereign.core.exception.HardwareDTOFactoryError import HardwareDTOFactoryError
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
    
    def test_try_create_hardware_with_none_type(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory.createHardware, None, {})
        
    def test_try_create_hardware_with_invalid_type_for_name_parameter(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory.createHardware, 123, {})
        
    def test_try_create_hardware_with_unregistered_name_of_class(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(HardwareDTOFactoryError, factory.createHardware, "Teste", {})
        
    def test_registerHardwareClass(self):
        factory = HardwareDTOFactory()
        
        self.assertEquals(0, factory._clearHardwareClasses())
        self.assertEquals(MachineImpl, factory._registerHardwareClass(Constants.MACHINE, MachineImpl))
        self.assertEquals(1, factory._countHardwareClasses())
        self.assertEquals(NetworkAdapterImpl, factory._registerHardwareClass(Constants.NETWORK_ADAPTER, NetworkAdapterImpl))
        self.assertEquals(2, factory._countHardwareClasses())
        
    def test_try_register_hardware_class_none_name(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory._registerHardwareClass, None, MachineImpl)
        
    def test_try_register_hardware_class_none_class_object(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory._registerHardwareClass, Constants.MACHINE, None)
        
    def test_try_register_hardware_class_with_invalid_type_for_name_parameter(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory._registerHardwareClass, 123, MachineImpl)
        
    def test_try_register_hardware_class_with_invalid_type_for_clazz_parameter(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory._registerHardwareClass, Constants.MACHINE, 123)
    
    def test_unregisterHardwareClass(self):
        factory = HardwareDTOFactory()
        
        self.assertEquals(0, factory._clearHardwareClasses())
        self.assertEquals(MachineImpl, factory._registerHardwareClass(Constants.MACHINE, MachineImpl))
        self.assertEquals(1, factory._countHardwareClasses())
        self.assertEquals(NetworkAdapterImpl, factory._registerHardwareClass(Constants.NETWORK_ADAPTER, NetworkAdapterImpl))
        self.assertEquals(2, factory._countHardwareClasses())
        
        self.assertEquals(MachineImpl, factory._unregisterHardwareClass(Constants.MACHINE))
        self.assertEquals(1, factory._countHardwareClasses())
        self.assertEquals(NetworkAdapterImpl, factory._unregisterHardwareClass(Constants.NETWORK_ADAPTER))
        self.assertEquals(0, factory._countHardwareClasses())
    
    def test_try_unregister_hardware_class_with_none_name(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory._unregisterHardwareClass, None)
        
    def test_try_unregister_hardware_class_with_invalid_type_for_name(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(TypeError, factory._unregisterHardwareClass, 123) 
        
    def test_try_create_hardware_with_none_values(self):
        factory = HardwareDTOFactory()
        
        self.assertEquals(0, factory._clearHardwareClasses())
        self.assertEquals(MachineImpl, factory._registerHardwareClass(Constants.MACHINE, MachineImpl))
        
        self.assertRaises(TypeError, factory.createHardware, Constants.MACHINE, None)
        
    def test_try_create_hardware_with_invalid_type_for_values(self):
        factory = HardwareDTOFactory()
        
        self.assertEquals(0, factory._clearHardwareClasses())
        self.assertEquals(MachineImpl, factory._registerHardwareClass(Constants.MACHINE, MachineImpl))
        
        self.assertRaises(TypeError, factory.createHardware, Constants.MACHINE, "123") 
        
    def test_try_unregister_non_existent_hardware_class(self):
        factory = HardwareDTOFactory()
        
        self.assertRaises(HardwareDTOFactoryError, factory._unregisterHardwareClass, "TESTE")
    
    def test_clearHardwareClasses(self):
        factory = HardwareDTOFactory()
        
        self.assertEquals(0, factory._clearHardwareClasses())
        self.assertEquals(MachineImpl, factory._registerHardwareClass(Constants.MACHINE, MachineImpl))
        self.assertEquals(1, factory._countHardwareClasses())
        self.assertEquals(NetworkAdapterImpl, factory._registerHardwareClass(Constants.NETWORK_ADAPTER, NetworkAdapterImpl))
        self.assertEquals(2, factory._countHardwareClasses())
        
        self.assertEquals(0, factory._clearHardwareClasses())
        self.assertEquals(0, factory._countHardwareClasses())
    