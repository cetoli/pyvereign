from threading import Semaphore

def return_type():
    def make_wrapper(f):
        def wrapper(*args, **kwargs):
            s = Semaphore()
            s.acquire()
            obj = f(*args, **kwargs)
            s.release()
            return obj
        return wrapper
    return make_wrapper