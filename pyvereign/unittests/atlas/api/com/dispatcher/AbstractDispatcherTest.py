from atlas.api.com.ipc.dispatcher.AbstractDispatcher import AbstractDispatcher
import unittest

class AbstractDispatcherTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractDispatcher)