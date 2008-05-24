from org.pyvereign.core.configuration.repository.AbstractObjectRepository import AbstractObjectRepository

class DefaultObjectRepository(AbstractObjectRepository):
    """
    Default implementation of AbstractObjectrepository class.
    
    @author: Fabricio
    @since: 16/01/2008 - 23:51:35
    @version: 0.0.1
    """
    
    def __init__(self):
        self.initialize()
    