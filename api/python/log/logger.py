import collections
import traceback
import datetime
from lib.colorama import Fore, Back, Style


class Logger:
    def __init__(self):
        self.level = "null"
        self.information = "null"

    def reset(self):
        self.level = "null"
        self.information = "null"

    def debug(self, information: str):
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        self.level = "DEBUG"
        self.information = information
        print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + Fore.BLACK + Back.BLUE + self.level + Fore.RESET + Back.RESET + "  " + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.BLUE + self.information + Back.RESET)
        self.reset()

    def info(self, information: str):
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        self.level = "INFO"
        self.information = information
        print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + self.level + Fore.RESET + Back.RESET + "   " + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + self.information + Back.RESET)
        self.reset()

    def warning(self, information: str):
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        self.level = "WARNING"
        self.information = information
        print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + Fore.YELLOW + Style.ITALIC + Style.BOLD + self.level + Style.RESET_ALL + Fore.RESET + Back.RESET + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.YELLOW + self.information + Back.RESET)
        self.reset()

    def error(self, information: str):
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        self.level = "ERROR"
        self.information = information
        print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + Fore.RED + Style.BOLD + self.level + Style.RESET_ALL + "  " + Fore.RESET + Back.RESET + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.RED + Style.BOLD +Style.ITALIC + self.information + Back.RESET)
        self.reset()

