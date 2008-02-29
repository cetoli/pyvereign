from atlas.api.com.ipc.dispatcher.Dispatcher import Dispatcher
import unittest

class DispatcherTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, Dispatcher)