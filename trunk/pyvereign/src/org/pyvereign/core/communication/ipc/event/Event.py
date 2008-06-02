from org.pyvereign.core.communication.format.FormatableObject import FormatableObject

class Event(FormatableObject):
    
    def __init__(self):
        raise NotImplementedError()
    
    def getHandle(self):
        pass
    
    def setAttribute(self, name, value):
        pass
    
    def getAttribute(self, name):
        pass
    
    def removeAttribute(self, name):
        pass
    
    def getNumberOfAttributes(self):
        pass
    
    def getAttributeNames(self):
        pass
    
    def getAttributeValues(self):
        pass
    
    def getOrigin(self):
        pass
    
    def getDestination(self):
        pass
        