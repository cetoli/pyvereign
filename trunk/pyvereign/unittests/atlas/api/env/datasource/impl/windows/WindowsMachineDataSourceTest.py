from atlas.api.env.datasource.impl.windows.WindowsMachineDataSource import WindowsMachineDataSource
import unittest

class WindowsMachineDataSourceTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(WindowsMachineDataSource())
        self.assertEquals("WindowsMachineDataSource", WindowsMachineDataSource().getName())
    
    def test_retrive_object(self):
        dataSource = WindowsMachineDataSource()
        machine = dataSource.retrieveMachine()
        self.assertTrue(machine)
