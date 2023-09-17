from datetime import datetime

import logger
import datetime
import helper

__version__ = "0.0.1pre"

__author__ = "LZH <https://github.com/LZH-sqrt2>"

if __name__ == "__main__":
    test_logger = logger.Logger()

    def f():
        test_logger.debug("in f")
    f()
    test_logger.debug("This is test debug log.")
    test_logger.info("This is test info log.")
    test_logger.warning("This is test warning log.")
    test_logger.error("This is test error log.")
    test_caller_helper = helper.CallerHelper()
    print(test_caller_helper.getInstanceName())
