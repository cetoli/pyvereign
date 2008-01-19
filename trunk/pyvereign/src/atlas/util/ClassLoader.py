class ClassLoader:
    
    def loadClass(self, module, className):
        try:
            mod = __import__(module, globals(), locals(), className, -1)
            clazz = mod.__getattribute__(className)
            return clazz
        except:
            raise
        
    loadClass = classmethod(loadClass)