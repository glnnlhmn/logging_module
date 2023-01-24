"""
Create a custom logger as well as some handlers that will represent output destinations

We are using Logger, LogRecord, Handlers and Formatter classes because
a custom logger can’t be configured using basicConfig().

Loggers create LogRecords.  Handlers send LogRecords to a destination.
"""
import logging

# Create a custom logger
logger = logging.getLogger(__name__)    # __name__ = 08_logging

# Create handlers
c_handler = logging.StreamHandler()    # Console handler
f_handler = logging.FileHandler('file.log')    # File handler

# Set level for handlers - different logging levels
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatters to handlers
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

"""Console output:
__main__ - WARNING - This is a warning
__main__ - ERROR - This is an error
"""

"""File output:
2023-01-13 12:13:57,568 - __main__ - ERROR - This is an error
"""