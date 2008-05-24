from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractProcessor import AbstractProcessor

class ProcessorImpl(AbstractProcessor):
    """
    Default implementation for Process interface.
    
    @author: Fabricio
    @since: 22/03/2008 - 18:53:12
    @version: 0.0.1
    """
    
    def __init__(self, values = {}):
        self.init(values)
    