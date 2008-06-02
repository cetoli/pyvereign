from org.pyvereign.core.communication.ipc.event.Event import Event
from sets import ImmutableSet

class AbstractEvent(Event):
    
    def init(self, handle, origin, destination):
        self._handle = handle
        self._attributes = {}
        self._origin = origin
        self._destination = destination
    
    def getHandle(self):
        return self._handle
    
    def getOrigin(self):
        return self._origin
    
    def getDestination(self):
        return self._destination
    
    def setAttribute(self, name, value):
        if not isinstance(name, str):
            raise TypeError()
        self._attributes[name] = value
        return self._attributes[name]
    
    def getAttribute(self, name):
        if not isinstance(name, str):
            raise TypeError()
        return self._attributes[name]
    
    def removeAttribute(self, name):
        if not isinstance(name, str):
            raise TypeError()
        value = self._attributes[name]
        del self._attributes[name]
        return value
    
    def getNumberOfAttributes(self):
        return len(self._attributes)
    
    def getAttributeNames(self):
        return ImmutableSet(self._attributes.keys())
    
    def getAttributeValues(self):
        return ImmutableSet(self._attributes.values())
    
    def getValues(self):
        values = {"handle": self._handle, "attributes": self._attributes}
        return values
    
    def setValues(self, values):
        if not values.has_key("handle"):
            raise StandardError()
        if not values.has_key("attributes"):
            raise StandardError()
        self._handle = values["handle"]
        self._attributes = values["attributes"]