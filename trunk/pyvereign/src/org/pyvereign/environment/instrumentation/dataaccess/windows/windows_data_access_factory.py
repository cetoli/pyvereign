from org.pyvereign.base.object import Object
from org.pyvereign.environment.instrumentation.dataaccess.ibattery_dao import IBatteryDAO
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_battery_dao import WindowsBatteryDAO
from org.pyvereign.util.decorators.public import public
from org.pyvereign.util.decorators.return_type import return_type
from org.pyvereign.util.decorators.require import require
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_disk_drive_dao import WindowsDiskDriveDAO
from org.pyvereign.environment.instrumentation.dataaccess.idisk_drive_dao import IDiskDriveDAO
from org.pyvereign.environment.instrumentation.dataaccess.imachine_dao import IMachineDAO
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_machine_dao import WindowsMachineDAO
from org.pyvereign.environment.instrumentation.dataaccess.inetwork_adapter_dao import INetworkAdapterDAO
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_network_adapter_dao import WindowsNetworkAdapterDAO
from org.pyvereign.environment.instrumentation.dataaccess.iphysical_memory_dao import IPhysicalMemoryDAO
from org.pyvereign.environment.instrumentation.dataaccess.iprocessor_dao import IProcessorDAO
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_physical_memory_dao import WindowsPhysicalMemoryDAO
from org.pyvereign.environment.instrumentation.dataaccess.windows.windows_processor_dao import WindowsProcessorDAO


class WindowsDataAccessFactory(Object):
    
    @public
    @return_type(IBatteryDAO)
    def createBatteryDAO(self):
        return WindowsBatteryDAO()
    
    @public
    @return_type(IDiskDriveDAO)
    def createDiskDriveDAO(self):
        return WindowsDiskDriveDAO()
    
    @public
    @return_type(IMachineDAO)
    def createMachineDAO(self):
        return WindowsMachineDAO()
    
    @public
    @return_type(INetworkAdapterDAO)
    def createNetworkAdapterDAO(self):
        return WindowsNetworkAdapterDAO()
    
    @public
    @return_type(IPhysicalMemoryDAO)
    def createPhysicalMemoryDAO(self):
        return WindowsPhysicalMemoryDAO()
    
    @public
    @return_type(IProcessorDAO)
    def createProcessorDAO(self):
        return WindowsProcessorDAO()

