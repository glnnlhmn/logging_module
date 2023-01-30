import logging
import sys

logger = logging.getLogger("pylog")
logger.setLevel(logging.DEBUG)
handler_1 = logging.FileHandler(filename="/tmp/records.log")
handler_1.setLevel(logging.INFO)
handler_2 = logging.StreamHandler(sys.stderr)
handler_2.setLevel(logging.ERROR)
logger.addHandler(handler_1)
logger.addHandler(handler_2)
logger.info("testing %d.. %d.. %d..", 1, 2, 3)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
