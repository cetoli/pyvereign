from atlas.api.conf.repository.ObjectRepository import ObjectRepository

class AbstractObjectRepository(ObjectRepository):
    """
    description
    
    @author: Fabricio
    @since: 16/01/2008 - 23:46:34
    @version: version
    """
    
    def initialize(self):
        self._objects = {}
    
    def addObject(self, name, obj):
        if not name or not obj:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("name is not instance of str.")
        self._objects[name] = obj
        return self._objects[name]
    
    def removeObject(self, name):
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("name is not instance of str.")
        obj = self._objects[name]
        del self._objects[name]
        return obj
    
    def getObject(self, name):
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("name is not instance of str.")
        return self._objects[name]
    
    def getNumberOfObjects(self):
        return len(self._objects)
    
    def clear(self):
        self._objects.clear()
        
    def getObjects(self):
        return self._objects.iteritems()
    
    def hasObject(self, name):
        if not name:
            raise RuntimeError("Invalid parameter.")
        if not isinstance(name, str):
            raise TypeError("name is not instance of str.")
        return self._objects.has_key(name)