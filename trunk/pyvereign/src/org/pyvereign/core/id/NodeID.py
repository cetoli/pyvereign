from org.pyvereign.core.id.ID import ID
import sha

class NodeID(ID):
    
    def __init__(self, macaddress):
        self._id = sha.new(macaddress).hexdigest()
        
    def getFormatedID(self):
        return "urn:pyvereign:core:node:" + self._id