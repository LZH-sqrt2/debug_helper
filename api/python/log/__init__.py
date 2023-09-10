import logger
import helper

__version__ = "0.0.1"

if __name__ == "__main__":
    test_logger = logger.Logger()
    test_logger.debug("This is test debug log.")
    test_logger.info("This is test info log.")
    test_logger.warning("This is test warning log.")
    test_logger.error("This is test error log.")
    test_helper = helper.Helper()
    print(test_helper.instance_name())
