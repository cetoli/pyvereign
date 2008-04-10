from org.pyvereign.core.microkernel.InternalServer import InternalServer
from org.pyvereign.util.Constants import Constants

class Environment(InternalServer):
    """
    Description
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: version
    """
    
    def __init__(self):
        self.init()
        
    def init(self):
        InternalServer.init(self)
        self._name = Constants.ENVIRONMENT
    