from org.pyvereign.core.microkernel.InternalServer import InternalServer
from org.pyvereign.util.Constants import Constants

class Environment(InternalServer):
    """
    Defines environment service provider of microkernel.
    
    @author: Fabricio
    @since: 31/03/2008 - 15:05:58
    @version: 0.0.1
    """
    
    def __init__(self):
        self.init()
    
    def init(self):
        InternalServer.init(self)
        self._name = Constants.ENVIRONMENT
    