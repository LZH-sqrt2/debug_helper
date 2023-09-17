import collections
import helper
import traceback
import datetime
from lib.colorama import Fore, Back, Style

class Logger:
    def __init__(self):
        self.level = "null"
        self.information = "null"
        self.helper = helper.CallerHelper()
        self.caller_name = "null"

    def __reset__(self):
        self.__init__()

    def log_msg(self, level: str, information: str, caller_name: str):
        if level == "DEBUG":
            print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + Fore.BLACK + Back.BLUE + level + Fore.RESET + Back.RESET + "  " + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.BLUE + information + Back.RESET + Style.RESET_ALL + Fore.RESET)
        if level == "INFO":
            print(Fore.GREEN + str(
                datetime.datetime.now()) + Fore.RESET + "|" + self.level + Fore.RESET + Back.RESET + "   " + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + self.information + Back.RESET + Style.RESET_ALL + Fore.RESET)
        if level == "WARNING":
            print(Fore.GREEN + str(
                datetime.datetime.now()) + Fore.RESET + "|" + Fore.YELLOW + Style.ITALIC + Style.BOLD + self.level + Style.RESET_ALL + Fore.RESET + Back.RESET + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.YELLOW + self.information + Back.RESET + Style.RESET_ALL + Fore.RESET)
        if level == "ERROR":
            print(Fore.GREEN + str(
                datetime.datetime.now()) + Fore.RESET + "|" + Fore.RED + Style.BOLD + self.level + Style.RESET_ALL + "  " + Fore.RESET + Back.RESET + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.RED + Style.BOLD + Style.ITALIC + self.information + Back.RESET + Style.RESET_ALL + Fore.RESET)

        self.__reset__()

    def debug(self, information: str):
        self.level = "DEBUG"
        self.information = information
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        # print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + Fore.BLACK + Back.BLUE + self.level + Fore.RESET + Back.RESET + "  " + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.BLUE + self.information + Back.RESET + Style.RESET_ALL + Fore.RESET)
        self.log_msg(self.level, self.information, caller_name)
        self.__reset__()

    def info(self, information: str):
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        self.level = "INFO"
        self.information = information
        print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + self.level + Fore.RESET + Back.RESET + "   " + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + self.information + Back.RESET + Style.RESET_ALL + Fore.RESET)
        self.__reset__()

    def warning(self, information: str):
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        self.level = "WARNING"
        self.information = information
        print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + Fore.YELLOW + Style.ITALIC + Style.BOLD + self.level + Style.RESET_ALL + Fore.RESET + Back.RESET + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.YELLOW + self.information + Back.RESET + Style.RESET_ALL + Fore.RESET)
        self.__reset__()

    def error(self, information: str):
        caller_name = traceback.extract_stack()[-2][2]
        if caller_name == "<module>":
            caller_name = "<Not in void>"
        self.level = "ERROR"
        self.information = information
        print(Fore.GREEN + str(datetime.datetime.now()) + Fore.RESET + "|" + Fore.RED + Style.BOLD + self.level + Style.RESET_ALL + "  " + Fore.RESET + Back.RESET + "|" + Fore.CYAN + caller_name + Fore.RESET + "|" + Fore.RED + Style.BOLD + Style.ITALIC + self.information + Back.RESET + Style.RESET_ALL + Fore.RESET)
        self.__reset__()
