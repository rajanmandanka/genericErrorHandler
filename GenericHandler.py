 
# custom exception handler

class ExceptionHandler(Exception):
    def __init__(self, message="Handle by Exception handler"):
        self.message = message

    def __str__(self):
        return str(self.message)
    
    @staticmethod
    def handler(func):
        def inner_handler(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                msg = f"Error in the function ` {func.__name__} ` is handle through exception handler"
                raise ExceptionHandler(msg)
        return inner_handler
