from org.pyvereign.util.ClassLoader import ClassLoader
from org.pyvereign.util.Constants import Constants

class MessageSenderCreator:
    
    def __init__(self):
        raise NotImplementedError()
    
    def createMessageSender(self, endpointAddress, kernel):
        clazz = ClassLoader.loadClass(Constants.MESSAGE_SENDER_MODULE, Constants.MESSAGE_SENDER_CLASS)
        return clazz(endpointAddress, kernel)
    
    createMessageSender = classmethod(createMessageSender)