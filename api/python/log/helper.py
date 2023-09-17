import inspect


class CallerHelper:
    def __init__(self):
        self.stack = inspect.stack()
        self.caller_globals = self.stack[1].frame.f_globals
        self.id16 = "0x0000000000000000"

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
