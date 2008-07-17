def pre_condition(arg_name, closure, errorClass, message = ""):
    def make_wrapper(f):
        if hasattr(f, "wrapped_args"):
            wrapped_args = getattr(f, "wrapped_args")
        else:
            code = f.func_code
            wrapped_args = list(code.co_varnames[:code.co_argcount])

        try:
            arg_index = wrapped_args.index(arg_name)
        except ValueError:
            raise NameError, arg_name
        
        def wrapper(*args, **kwargs):
            if not closure(args[arg_index]):
                raise errorClass(message)
            return f(*args, **kwargs)
        return wrapper
    return make_wrapper