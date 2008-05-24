from org.pyvereign.core.environment.instrumentation.dto.system.AbstractProcess import AbstractProcess

class ProcessImpl(AbstractProcess):
    """
    Defines the default implementation of AbstractProcess. 
    
    @author: Fabricio
    @since: 28/03/2008 - 16:43:14
    @version: 0.0.1
    """
    
    def __init__(self, values):
        self.init(values)
    