from atlas.api.com.ipc.handler.AbstractEventHandler import AbstractEventHandler
import unittest

class AbstractEventHandlerTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, AbstractEventHandler)