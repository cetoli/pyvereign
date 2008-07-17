def return_type(type):
    def make_wrapper(f):
        def wrapper(*args, **kwargs):
            obj = f(*args, **kwargs)
            if not isinstance(obj, type):
                raise TypeError, "Expected '%s' ; was %s." % (type, obj.__class__)
            return obj
        return wrapper
    return make_wrapper