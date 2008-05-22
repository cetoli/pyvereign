from org.pyvereign.util.Constants import Constants
from org.pyvereign.util.ClassLoader import ClassLoader
class MessageReceiverCreator:
    
    def __init__(self):
        raise NotImplementedError()
    
    def createMessageReceiver(self, endpointAddress, kernel):
        clazz = ClassLoader.loadClass(Constants.MESSAGE_RECEIVER_MODULE, Constants.MESSAGE_RECEIVER_CLASS)
        return clazz(endpointAddress, kernel)
    
    createMessageReceiver = classmethod(createMessageReceiver)