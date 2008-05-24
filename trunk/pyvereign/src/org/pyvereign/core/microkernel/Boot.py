from org.pyvereign.core.microkernel.Microkernel import Microkernel
class Boot:
    """
    Implements the boot process of platform.
    
    @author: Fabricio
    @since: 18/03/2008 - 11:22:00
    @version: 0.0.1
    """
    
    def __init__(self):
        self._microkernel = Microkernel()
    
    def initialize(self):
        """
        Performs the initialization process.
        
        @rtype: L{None}
        """
        self._microkernel.initialize()
    
    def start(self, args):
        """
        Starts the platform.
        
        @param args: List of arguments.
        @type args: L{list}
        @rtype: L{None}
        """
        self._microkernel.start(args)
    
    def stop(self):
        """
        Stops the platform.
        
        @rtype: L{None}
        """
        pass
    
if __name__ == '__main__':
    boot = Boot()
    boot.initialize()
    boot.start([5052])