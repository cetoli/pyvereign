from org.pyvereign.core.context.Context import Context

class CoreServiceContext(Context):
    
    def __init__(self, coreService):
        self._coreService = coreService