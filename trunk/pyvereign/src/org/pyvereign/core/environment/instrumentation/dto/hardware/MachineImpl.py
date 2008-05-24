from org.pyvereign.core.environment.instrumentation.dto.hardware.AbstractMachine import AbstractMachine

class MachineImpl(AbstractMachine):
    """
    Default implementation for user machine.
    
    @author: Fabricio
    @since: 22/03/2008 - 15:24:40
    @version: 0.0.1
    """
    
    def __init__(self, values):
        self.init(values)
    