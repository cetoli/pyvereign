from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.configuration.repository.ObjectRepositoryFactory import ObjectRepositoryFactory
from org.pyvereign.core.communication.format.FormatFactory import FormatFactory
from org.pyvereign.core.communication.format.FormatFactoryConfigurator import FormatFactoryConfigurator
from org.pyvereign.core.communication.format.JSONFormat import JSONFormat
from org.pyvereign.core.exception.FormatFactoryError import FormatFactoryError
import unittest

class MessageFormatFactoryTest(unittest.TestCase):
    
    def test_create_instance(self):
        self.assertTrue(FormatFactory())
        self.assertEquals(FormatFactory(), FormatFactory())
    
    def test_create_message_format(self):
        configurator = FormatFactoryConfigurator()
        self.assertEquals(Constants.MESSAGE_FORMATS_CONFIG_FILE, configurator.setFilename(Constants.MESSAGE_FORMATS_CONFIG_FILE))
        repository = ObjectRepositoryFactory().createObjectRepository(Constants.DEFAULT_OBJECT_REPOSITORY)
        self.assertEquals(repository, configurator.setObjectRepository(repository))
        
        configurator.loadConfiguration()
        configurator.createObjects()
        
        factory = configurator.configureObject(FormatFactory())
        
        self.assertEquals(JSONFormat, factory.createMessageFormat(Constants.JSON).__class__)
    
    def test_try_create_message_format_with_none_type(self):
        self.assertRaises(TypeError, FormatFactory().createMessageFormat, None)
        
    def test_try_create_message_format_with_invalid_type(self):
        self.assertRaises(TypeError, FormatFactory().createMessageFormat, 123)
        
    def test_try_create_message_format_with_non_existent_name(self):
        self.assertRaises(FormatFactoryError, FormatFactory().createMessageFormat, "test")
        
    def test_register_message_format_class(self):
        FormatFactory()._clearMessageFormatClasses()
        self.assertEquals(0, FormatFactory()._countMessageFormatClasses())
        
        self.assertEquals(JSONFormat, FormatFactory()._registerMessageFormatClass(Constants.JSON, JSONFormat))
        self.assertEquals(1, FormatFactory()._countMessageFormatClasses())
        
    def test_try_register_message_format_with_none_name(self):
        self.assertRaises(TypeError, FormatFactory()._registerMessageFormatClass, None, JSONFormat)
    
    def test_try_register_message_format_with_none_class_object(self):
        self.assertRaises(TypeError, FormatFactory()._registerMessageFormatClass, Constants.JSON, None)
        
    def test_try_register_message_format_with_invalid_name(self):
        self.assertRaises(TypeError, FormatFactory()._registerMessageFormatClass, 111, JSONFormat)
    
    def test_try_register_message_format_with_invalid_class_object(self):
        self.assertRaises(TypeError, FormatFactory()._registerMessageFormatClass, Constants.JSON, "JSONFormatMessage")
    
    def test_unregister_message_format(self):
        FormatFactory()._clearMessageFormatClasses()
        self.assertEquals(0, FormatFactory()._countMessageFormatClasses())
        
        self.assertEquals(JSONFormat, FormatFactory()._registerMessageFormatClass(Constants.JSON, JSONFormat))
        self.assertEquals(1, FormatFactory()._countMessageFormatClasses())
        self.assertEquals(JSONFormat, FormatFactory()._unregisterMessageFormatClass(Constants.JSON))
        self.assertEquals(0, FormatFactory()._countMessageFormatClasses())
    
    def test_try_unregister_message_format_with_non_existent_name(self):
        self.assertRaises(FormatFactoryError, FormatFactory()._unregisterMessageFormatClass, "test")
        
    def test_try_unregister_message_format_with_none_name(self):
        self.assertRaises(TypeError, FormatFactory()._unregisterMessageFormatClass, None)
        
    def test_try_unregister_message_format_with_invalid_name(self):
        self.assertRaises(TypeError, FormatFactory()._unregisterMessageFormatClass, 123)
        