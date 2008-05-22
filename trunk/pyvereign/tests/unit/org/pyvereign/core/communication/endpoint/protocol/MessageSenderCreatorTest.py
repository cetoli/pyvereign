from org.pyvereign.core.communication.endpoint.protocol.MessageSenderCreator import MessageSenderCreator
from org.pyvereign.core.communication.endpoint.address.EndpointAddress import EndpointAddress
from org.pyvereign.util.Constants import Constants
from org.pyvereign.core.microkernel.Microkernel import Microkernel
from org.pyvereign.core.communication.format.JSONFormat import JSONFormat
import unittest

class MessageSenderCreatorTest(unittest.TestCase):
    
    def test_create_message_sender(self):
        endpointAddress = EndpointAddress("TCP", "192.068.1.5", 5050)
        microkernel = Microkernel()
        microkernel.initialize()
        self.assertTrue(MessageSenderCreator.createMessageSender(endpointAddress, microkernel))
        self.assertEquals(Constants.MESSAGE_SENDER_CLASS, MessageSenderCreator.createMessageSender(endpointAddress, microkernel).__class__.__name__)