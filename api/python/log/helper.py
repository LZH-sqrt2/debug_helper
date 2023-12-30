import inspect
import functools


class CallerHelper:
    def __init__(self):
        self.stack = inspect.stack()
        self.caller_globals = self.stack[1].frame.f_globals
        self.id_length = len(str(hex(id(self))[2:]))  # This computer id's length
        self.id16_length = len(str(hex(id(self))[2:].upper()))
        self.id16 = "0x" + "0" * (self.id_length - self.id16_length) + str(hex(id(self))[2:].upper())

    def __reset__(self):
        self.__init__()

    def getInstanceName(self):
        for Object in self.caller_globals.items():
            not_have_0x_id16 = str(hex(id(self))[2:].upper())
            not_have_0x_id16_length = len(not_have_0x_id16)
            self.id16 = "0x" + "0" * (16 - not_have_0x_id16_length) + not_have_0x_id16

            if str(Object[1]) == "<helper.CallerHelper object at " + self.id16 + ">":
                return Object[0]

        self.__reset__()


def AccessControlCharacters(level: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            caller_frame = inspect.currentframe().f_back
            caller_module = inspect.getmodule(caller_frame)
            caller__name__ = caller_module.__name__
            print(caller__name__ + level)
            return func(*args, **kwargs)

        return wrapper

    return decorator
