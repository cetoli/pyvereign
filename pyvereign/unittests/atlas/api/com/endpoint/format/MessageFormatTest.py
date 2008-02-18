from atlas.api.com.endpoint.format.MessageFormat import MessageFormat
import unittest

class MessageFormatTest(unittest.TestCase):
    
    def test_try_create_instance(self):
        self.assertRaises(NotImplementedError, MessageFormat)