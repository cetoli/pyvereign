from atlas.api.com.ipc.dispatcher.DefaultDispatcher import DefaultDispatcher
import unittest

class DefaultDispatcherTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(DefaultDispatcher())